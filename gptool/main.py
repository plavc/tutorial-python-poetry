import typer


def main(name: str, verbose: bool = False):
    typer.echo(f"Hello {name}!")

    if verbose:
        typer.echo("Program Finished.")


if __name__ == "__main__":
    typer.run(main)
