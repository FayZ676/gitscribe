import click
import subprocess
import sys


@click.group()
def cli():
    """My CLI Tool"""


@cli.command()
@click.option("--last", prompt="Last N commits", help="")
# @click.option("--since", prompt="Date since", help="")
# @click.option("--until", prompt="Date until", help="")
def commit2content(last):
    """Fetch git commits and display their content."""
    cmd = ["git", "log", "--oneline"]
    if last and last.strip():
        try:
            int(last)
            cmd.extend([f"-{last}"])
        except ValueError:
            click.echo(
                f"Error: '{last}' is not a valid number for --last option", err=True
            )
            return

    # if since and since.strip():
    #     cmd.extend([f"--since={since}"])

    # if until and until.strip():
    #     cmd.extend([f"--until={until}"])

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        if result.stdout:
            click.echo(result.stdout.strip())
        else:
            click.echo("No commits found matching the criteria.")

    except subprocess.CalledProcessError as e:
        click.echo(f"Error running git command: {e.stderr.strip()}", err=True)
        sys.exit(1)
    except FileNotFoundError:
        click.echo(
            "Error: git command not found. Make sure git is installed and in your PATH.",
            err=True,
        )
        sys.exit(1)


if __name__ == "__main__":
    cli()
