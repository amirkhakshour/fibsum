import click
from flask.cli import FlaskGroup

from fibsum.app import create_app


def create_fibsum(info):
    return create_app()


@click.group(cls=FlaskGroup, create_app=create_fibsum)
def cli():
    """Main entry point"""
    pass


if __name__ == "__main__":
    cli()
