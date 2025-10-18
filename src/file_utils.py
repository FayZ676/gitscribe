"""File I/O utilities for GitScribe."""

import click
from pathlib import Path


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


def ensure_style_file_exists(file_path: str) -> None:
    """Create an empty style file if it doesn't exist."""
    if not file_path:
        return
    
    path = Path(file_path)
    if not path.exists():
        # Create parent directories if they don't exist
        path.parent.mkdir(parents=True, exist_ok=True)
        # Create empty file
        path.touch()
        click.echo(f"✅ Created empty style file: {file_path}")
