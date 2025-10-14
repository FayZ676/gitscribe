import sys
import subprocess
from datetime import datetime
from string import Template

import click

from config import require_api_key, set_api_key, prompt_for_openai_api_key
from llm import OpenAILLM


def validate_value_type(value, accept_type):
    """Validates that a value is of the expected type, returning the value if valid or None if invalid."""
    if not isinstance(value, accept_type):
        click.echo("Error: Foo")
        return None
    return value


def validate_date_string_format(value: str, accept_format: str):
    """Validates that a date string matches the specified format and returns the value if valid, otherwise None."""
    try:
        datetime.strptime(value, accept_format)
        return value
    except ValueError:
        click.echo(
            f"Error: Value '{value}' does not match expected format '{accept_format}'"
        )
        return None


def build_git_log_command(last, since, until):
    """Build git log command with optional filters."""
    cmd = ["git", "log", "--oneline"]

    if last is not None and validate_value_type(value=last, accept_type=int):
        cmd.extend(["-n", str(last)])

    if since is not None and validate_date_string_format(
        value=since, accept_format="%Y-%m-%d"
    ):
        cmd.extend([f"--since={since}"])

    if until is not None and validate_date_string_format(
        value=until, accept_format="%Y-%m-%d"
    ):
        cmd.extend([f"--until={until}"])

    return cmd


def run_git_command(cmd) -> str:
    """Execute a git command and handle errors."""
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        if result.stdout:
            return result.stdout.strip()
        else:
            return ""

    except subprocess.CalledProcessError as e:
        click.echo(f"Error running git command: {e.stderr.strip()}", err=True)
        sys.exit(1)
    except FileNotFoundError:
        click.echo(
            "Error: git command not found. Make sure git is installed and in your PATH.",
            err=True,
        )
        sys.exit(1)
    except Exception as e:
        click.echo(f"An unexpected error occurred: {str(e)}", err=True)
        sys.exit(1)


def get_git_diff() -> str:
    """Get git diff of staged changes, or all changes if nothing is staged."""
    # First, check if there are staged changes
    staged_diff = run_git_command(["git", "diff", "--cached"])
    
    if staged_diff:
        return staged_diff
    
    # If no staged changes, get all unstaged changes
    return run_git_command(["git", "diff"])


def get_style(file_path: str | None = None, default_file: str = "content_style.txt") -> str:
    """Get style content from file. Returns empty string if file doesn't exist."""
    if file_path is None:
        file_path = default_file

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""


def save_content_to_file(content: str, file_path: str) -> None:
    """Save generated content to a file."""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    click.echo(f"\n✅ Content saved to: {file_path}")


@click.group()
def gitscribe():
    """GitScribe - Transform your git history into shareable content."""


@gitscribe.command()
def configure():
    """Configure GitScribe settings (API keys, etc.)."""
    api_key = prompt_for_openai_api_key()
    set_api_key(api_key=api_key, key_name="OPENAI_API_KEY")
    click.echo(
        "\n✅ Configuration complete! You can now use the commands `gitscribe content` and `gitscribe message`."
    )


@gitscribe.command()
@click.option("--last", default=1, help="Number of commits to fetch (default: 1)")
@click.option("--since", default=None, help="Include commits since date (YYYY-MM-DD)")
@click.option("--until", default=None, help="Include commits until date (YYYY-MM-DD)")
@click.option(
    "--style",
    default=None,
    help="Style file for the LLM to reference when generating content (default: content_style.txt)",
)
@click.option(
    "--output",
    "-o",
    default=None,
    help="Output file path to save generated content (default: gitscribe_output.txt)",
)
def content(last, since, until, style, output):
    """Generate content from git commits."""
    cmd = build_git_log_command(last, since, until)
    commits = run_git_command(cmd)
    style_content = get_style(file_path=style)

    if not commits:
        click.echo("No commits found matching the criteria.")
        return

    click.echo(f"💬 Commits:\n{commits}")
    api_key = require_api_key("OPENAI_API_KEY")
    response = OpenAILLM(api_key=api_key).generate(
        prompt=prompt.substitute(commits=commits, style=style_content)
    )
    click.echo(f"\n📝 Generated Content:\n{response}")
    
    output_file = output if output else "gitscribe_output.txt"
    save_content_to_file(response, output_file)


@gitscribe.command()
@click.option(
    "--style",
    default=None,
    help="Style file for the LLM to reference when generating commit messages (default: message_style.txt)",
)
def message(style):
    """Generate a commit message from git diff."""
    diff = get_git_diff()
    
    if not diff:
        click.echo("No changes found. Make some changes or stage them with 'git add' first.")
        return
    
    click.echo("📊 Analyzing changes...")
    style_content = get_style(file_path=style, default_file="message_style.txt")
    
    api_key = require_api_key("OPENAI_API_KEY")
    response = OpenAILLM(api_key=api_key).generate(
        prompt=message_prompt.substitute(diff=diff, style=style_content)
    )
    click.echo(f"\n💬 Generated Commit Message:\n{response}")


prompt = Template(
    """
## Instructions:
Your job is to transform commit messages into meaningful content in the style of other provided content.
    
## Commits:
$commits

## Style References
$style

Return only the transformed text content and nothing else.
"""
)


message_prompt = Template(
    """
## Instructions:
Your job is to generate a clear, concise commit message based on the git diff provided below.
The commit message should follow best practices and accurately describe the changes made.

$style

## Git Diff:
$diff

Return only the commit message text and nothing else.
"""
)


if __name__ == "__main__":
    gitscribe()
