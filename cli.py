import click


@click.group()
def cli():
    """My CLI Tool"""
    pass


@cli.command()
@click.option("--last", prompt="Last N commits", help="")
@click.option("--since", prompt="Date since", help="")
@click.option("--until", prompt="Date until", help="")
def commit2content(last, since, until):
    click.echo(f"LAST ({last}), SINCE ({since}), UNTIL ({until})")


if __name__ == "__main__":
    cli()
