import click
import pyperclip

from src.config import require_api_key, set_api_key, prompt_for_openai_api_key
from src.llm import OpenAILLM
from src.prompts import post_prompt, commit_prompt
from src.git_utils import build_git_log_command, run_git_command, get_git_diff
from src.file_utils import get_style, save_content_to_file


@click.group()
def gitscribe():
    """GitScribe - Transform your git history into shareable content."""


@gitscribe.command()
def configure():
    """Configure GitScribe settings (API keys, etc.)."""
    api_key = prompt_for_openai_api_key()
    set_api_key(api_key=api_key, key_name="OPENAI_API_KEY")
    click.echo(
        "\n✅ Configuration complete! You can now use the commands `gitscribe post` and `gitscribe commit`."
    )


@gitscribe.command()
@click.option("--last", default=1, help="Number of commits to fetch (default: 1)")
@click.option("--since", default=None, help="Include commits since date (YYYY-MM-DD)")
@click.option("--until", default=None, help="Include commits until date (YYYY-MM-DD)")
@click.option(
    "--style",
    default="styles/post_style.txt",
    help="Style file for the LLM to reference when generating post content (default: post_style.txt)",
)
@click.option(
    "--output",
    default=None,
    help="Output file path to save generated content (default: gitscribe_output.txt)",
)
def post(last, since, until, style, output):
    """Generate post content from git commits."""
    cmd = build_git_log_command(last, since, until)
    commits = run_git_command(cmd)
    style_content = get_style(file_path=style)

    if not commits:
        click.echo("❌ No commits found matching the criteria.")
        return

    click.echo(f"💬 Commits:\n{commits}")
    api_key = require_api_key("OPENAI_API_KEY")
    response = OpenAILLM(api_key=api_key).generate(
        prompt=post_prompt.substitute(commits=commits, style=style_content)
    )
    pyperclip.copy(response)
    click.echo(f"\n📝 Generated Content:\n{response}")
    click.echo("\n📋 Content copied to clipboard!")

    output_file = output if output else "gitscribe_output.txt"
    save_content_to_file(response, output_file)


@gitscribe.command()
@click.option(
    "--style",
    default="styles/commit_style.txt",
    help="Style file for the LLM to reference when generating commit messages (default: commit_style.txt)",
)
def commit(style):
    """Generate a commit message from git diff."""
    diff = get_git_diff()

    if not diff:
        click.echo(
            "❌ No changes found. Make some changes or stage them with 'git add' first."
        )
        return

    click.echo("📊 Analyzing changes...")
    style_content = get_style(file_path=style)
    api_key = require_api_key("OPENAI_API_KEY")
    response = OpenAILLM(api_key=api_key).generate(
        prompt=commit_prompt.substitute(diff=diff, style=style_content)
    )
    click.echo(f"\n✅ Generated Commit Message:\n{response}")

    # Copy to clipboard
    try:
        pyperclip.copy(response)
        click.echo("\n📋 Commit message copied to clipboard!")
    except Exception as e:
        click.echo(f"\n⚠️  Could not copy to clipboard: {e}")


if __name__ == "__main__":
    gitscribe()
