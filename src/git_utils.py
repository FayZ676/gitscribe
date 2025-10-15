"""Git utilities for GitScribe."""

import sys
import subprocess
import click

from src.validators import validate_value_type, validate_date_string_format


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
    staged_diff = run_git_command(["git", "diff", "--cached"])

    if staged_diff:
        return staged_diff

    return run_git_command(["git", "diff"])
