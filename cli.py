import click
from library.methods import add, subtract


@click.group()
def cli():
    """Command line interface for math operations."""
    # Group for math operations


@cli.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
def addition(a, b):
    """Add two numbers and display the result.

    Example: python cli.py addition 2 3
    For negative numbers, use: python cli.py addition -- -1 1
    """
    result = add(a, b)
    click.echo(result)


@cli.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
def subtraction(a, b):
    """Subtract two numbers and display the result.

    Example: python cli.py subtraction 5 3
    For negative numbers, use: python cli.py subtraction -- -5 -3
    """
    result = subtract(a, b)
    click.echo(result)


if __name__ == "__main__":
    cli()
