"""Configure command for GitScribe."""

import click

from src.config import (
    set_api_key,
    prompt_for_openai_api_key,
    set_default_style_path,
    prompt_for_style_file,
)
from src.file_utils import ensure_style_file_exists


@click.command()
def configure():
    """Configure GitScribe settings (API keys, etc.)."""
    api_key = prompt_for_openai_api_key()
    set_api_key(api_key=api_key, key_name="OPENAI_API_KEY")

    commit_style_path = prompt_for_style_file("commit")
    if commit_style_path:
        ensure_style_file_exists(commit_style_path)
        set_default_style_path("commit", commit_style_path)
        click.echo(f"✅ Default commit style file set to: {commit_style_path}")

    post_style_path = prompt_for_style_file("post")
    if post_style_path:
        ensure_style_file_exists(post_style_path)
        set_default_style_path("post", post_style_path)
        click.echo(f"✅ Default post style file set to: {post_style_path}")

    click.echo(
        "\n✅ Configuration complete! You can now use the commands `gitscribe post` and `gitscribe commit`."
    )
