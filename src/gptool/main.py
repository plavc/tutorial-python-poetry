"""Gp tools main module"""
import typer

from __init__ import __version__

app = typer.Typer()


@app.command()
def main(name: str):
    """
    Main method.
    :param name:
    :param verbose:
    :return:
    """
    typer.echo(f"Hello {name}!")


@app.command()
def version():
    typer.echo(__version__)


def run():
    typer.__version__


if __name__ == "__main__":
    run()
