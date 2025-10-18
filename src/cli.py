import click
import pyperclip

from src.config import (
    require_api_key,
    set_api_key,
    prompt_for_openai_api_key,
    get_default_style_path,
    set_default_style_path,
    prompt_for_style_file,
)
from src.llm import OpenAILLM
from src.prompts import post_prompt, commit_prompt
from src.git_utils import build_git_log_command, run_git_command, get_git_diff
from src.file_utils import get_style, save_content_to_file, ensure_style_file_exists


@click.group()
def gitscribe():
    """GitScribe - Transform your git history into shareable content."""


@gitscribe.command()
def configure():
    """Configure GitScribe settings (API keys, etc.)."""
    api_key = prompt_for_openai_api_key()
    set_api_key(api_key=api_key, key_name="OPENAI_API_KEY")
    
    # Prompt for default commit style file
    commit_style_path = prompt_for_style_file("commit")
    if commit_style_path:
        ensure_style_file_exists(commit_style_path)
        set_default_style_path("commit", commit_style_path)
        click.echo(f"✅ Default commit style file set to: {commit_style_path}")
    
    # Prompt for default post style file
    post_style_path = prompt_for_style_file("post")
    if post_style_path:
        ensure_style_file_exists(post_style_path)
        set_default_style_path("post", post_style_path)
        click.echo(f"✅ Default post style file set to: {post_style_path}")
    
    click.echo(
        "\n✅ Configuration complete! You can now use the commands `gitscribe post` and `gitscribe commit`."
    )


@gitscribe.command()
@click.option("--last", default=1, help="Number of commits to fetch (default: 1)")
@click.option("--since", default=None, help="Include commits since date (YYYY-MM-DD)")
@click.option("--until", default=None, help="Include commits until date (YYYY-MM-DD)")
@click.option(
    "--style",
    default=None,
    help="Style file for the LLM to reference when generating post content (optional)",
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
    
    # Use default style file from config if no style option provided
    style_file = style
    if not style_file:
        style_file = get_default_style_path("post")
    
    style_content = get_style(file_path=style_file)

    if not commits:
        click.echo("❌ No commits found matching the criteria.")
        return

    click.echo(f"💬 Commits:\n{commits}")
    api_key = require_api_key("OPENAI_API_KEY")
    response = OpenAILLM(api_key=api_key).generate(
        prompt=post_prompt.substitute(commits=commits, style=style_content)
    )

    if not response:
        click.echo("❌ Failed to generate content")
        return

    pyperclip.copy(response)
    click.echo(f"\n📝 Generated Content:\n{response}")
    click.echo("\n📋 Content copied to clipboard!")

    output_file = output if output else "gitscribe_output.txt"
    save_content_to_file(response, output_file)


@gitscribe.command()
@click.option(
    "--style",
    default=None,
    help="Style file for the LLM to reference when generating commit messages (optional)",
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
    
    # Use default style file from config if no style option provided
    style_file = style
    if not style_file:
        style_file = get_default_style_path("commit")
    
    style_content = get_style(file_path=style_file)
    api_key = require_api_key("OPENAI_API_KEY")
    response = OpenAILLM(api_key=api_key).generate(
        prompt=commit_prompt.substitute(diff=diff, style=style_content)
    )

    if not response:
        click.echo("❌ Failed to generate content")
        return

    pyperclip.copy(response)
    click.echo(f"\n✅ Generated Commit Message:\n{response}")
    click.echo("\n📋 Commit message copied to clipboard!")


if __name__ == "__main__":
    gitscribe()
