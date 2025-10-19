"""Commit command for GitScribe."""

import click
import pyperclip

from src.config import require_api_key, get_default_style_path
from src.llm import OpenAILLM
from src.prompts import commit_prompt
from src.git_utils import get_git_diff
from src.file_utils import get_style


@click.command()
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
