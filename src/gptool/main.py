"""Gp tools main module"""
import typer


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
    typer.echo("0.0.0")


def run():
    typer.__version__


if __name__ == "__main__":
    run()
