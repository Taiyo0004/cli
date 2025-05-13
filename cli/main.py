import click


@click.command()
@click.option("--name", help="Displays the name of the owner")
def cli(name="Aditya Naidu"):
    click.echo(f"The owner of the Laptop is {name}")
