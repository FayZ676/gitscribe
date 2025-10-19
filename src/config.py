"""Configuration management for GitScribe."""

import os
import json
from pathlib import Path
import click


CONFIG_DIR = Path.home() / ".gitscribe"
CONFIG_FILE = CONFIG_DIR / "config.json"


def get_config_dir() -> Path:
    """Get the config directory, creating it if it doesn't exist."""
    CONFIG_DIR.mkdir(exist_ok=True)
    return CONFIG_DIR


def load_config() -> dict:
    """Load configuration from file."""
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {}


def save_config(config: dict) -> None:
    """Save configuration to file."""
    get_config_dir()
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)


def get_api_key(key_name: str) -> str | None:
    """Get API key from environment variable or config file."""
    api_key = os.environ.get(key_name)
    if api_key:
        return api_key

    config = load_config()
    return config.get(key_name)


def require_api_key(key_name: str) -> str:
    """Get API key or raise error if not found."""
    api_key = get_api_key(key_name)
    if not api_key:
        click.echo(f"❌ No {key_name} found!", err=True)
        click.echo("\nYou can either:", err=True)
        click.echo("  1. Run: gitscribe configure", err=True)
        click.echo(f"  2. Set the {key_name} environment variable", err=True)
        raise click.Abort()
    return api_key


def set_api_key(api_key: str, key_name: str) -> None:
    """Save API key to config file."""
    config = load_config()
    config[key_name] = api_key
    save_config(config)
    click.echo(f"API key saved to {CONFIG_FILE}")


def prompt_for_openai_api_key() -> str:
    """Interactively prompt user for API key."""
    click.echo("\n🔑 OpenAI API Key Required")
    click.echo("\nYou can get your API key from: https://platform.openai.com/api-keys")
    click.echo("\nYou have two options for storing your API key:")
    click.echo("  1. Store in config file (this command)")
    click.echo("  2. Set the OPENAI_API_KEY environment variable")
    click.echo(
        "\nThis command will store the key securely in your home directory (~/.gitscribe/config.json)"
    )

    api_key = click.prompt("\nEnter your OpenAI API key", hide_input=True)
    return api_key.strip()


def get_default_style_path(style_type: str) -> str | None:
    """Get the default style file path for a given style type (commit or post)."""
    config = load_config()
    key = f"default_{style_type}_style"
    return config.get(key)


def set_default_style_path(style_type: str, file_path: str) -> None:
    """Save default style file path to config."""
    config = load_config()
    key = f"default_{style_type}_style"
    config[key] = file_path
    save_config(config)


def prompt_for_style_file(style_type: str) -> str:
    """Interactively prompt user for style file path."""
    click.echo(f"\n📄 Default {style_type.capitalize()} Style File")
    click.echo(
        f"\nSpecify the path to your default {style_type} style file."
    )
    click.echo(
        f"This file will be used when you run 'gitscribe {style_type}' without the --style option."
    )
    click.echo("If the file doesn't exist, GitScribe will create it as an empty file.")
    
    file_path = click.prompt(
        f"\nEnter the path to your default {style_type} style file",
        default="",
        show_default=False
    )
    return file_path.strip()
