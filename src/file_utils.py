"""File I/O utilities for GitScribe."""

import click


def get_style(file_path: str | None) -> str:
    """Get style content from file. Returns empty string if no file provided or file doesn't exist."""
    if not file_path:
        return ""

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        click.echo(f"⚠️  Style file '{file_path}' not found.", err=True)
        return ""


def save_content_to_file(content: str, file_path: str) -> None:
    """Save generated content to a file."""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    click.echo(f"\n✅ Content saved to: {file_path}")
