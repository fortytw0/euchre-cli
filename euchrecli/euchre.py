import click

from euchrecli.game import setup


@click.group()
@click.version_option()
def cli():
    pass


@cli.command()
def play():
    setup()


if __name__ == "__main__":
    cli()
