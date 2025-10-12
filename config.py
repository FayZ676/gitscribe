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
