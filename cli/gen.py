import typer
from faker import Faker

app = typer.Typer()
faker = Faker()


@app.command()
def first_name():
    typer.echo(faker.first_name())


@app.command()
def last_name():
    typer.echo(faker.last_name())


@app.command()
def name():
    typer.echo(faker.name())


if __name__ == '__main__':
    app()
