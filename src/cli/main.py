"""Main CLI entry point for GitScribe."""

import click

from .configure import configure
from .post import post
from .commit import commit


@click.group()
def gitscribe():
    """GitScribe - Transform your git history into shareable content."""


gitscribe.add_command(configure)
gitscribe.add_command(post)
gitscribe.add_command(commit)


if __name__ == "__main__":
    gitscribe()
