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


@click.group()
def gitscribe():
    """GitScribe - Transform your git history into shareable content."""


@gitscribe.command()
def configure():
    """Configure GitScribe settings (API keys, etc.)."""
    api_key = prompt_for_openai_api_key()
    set_api_key(api_key=api_key, key_name="OPENAI_API_KEY")
    click.echo("\n✅ Configuration complete! You can now use gitscribe content.")


@gitscribe.command()
@click.option("--last", default=1, help="Number of commits to fetch (default: 1)")
@click.option("--since", default=None, help="Include commits since date (YYYY-MM-DD)")
@click.option("--until", default=None, help="Include commits until date (YYYY-MM-DD)")
def content(last, since, until):
    """Generate content from git commits."""
    cmd = build_git_log_command(last, since, until)
    commits = run_git_command(cmd)

    if not commits:
        click.echo("No commits found matching the criteria.")
        return

    click.echo(f"💬 Commits:\n{commits}")
    api_key = require_api_key("OPENAI_API_KEY")
    response = OpenAILLM(api_key=api_key).generate(
        prompt=prompt.substitute(commits=commits)
    )
    click.echo(f"\n📝 Generated Content:\n{response}")


prompt = Template(
    """
$commits
                  
Summarize the above commits.
"""
)


if __name__ == "__main__":
    gitscribe()
