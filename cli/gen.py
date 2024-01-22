import typer
import pyperclip
from faker import Faker

app = typer.Typer()
faker = Faker()


@app.command()
def first_name():
    random_first_name = faker.first_name()
    typer.echo(random_first_name)
    pyperclip.copy(random_first_name)


@app.command()
def last_name():
    random_last_name = faker.last_name()
    typer.echo(random_last_name)
    pyperclip.copy(random_last_name)


@app.command()
def name():
    random_name = faker.name()
    typer.echo(random_name)
    pyperclip.copy(random_name)


if __name__ == '__main__':
    app()
