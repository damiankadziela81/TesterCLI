import typer
import pyperclip
from functools import wraps
from faker import Faker

app = typer.Typer()
faker = Faker()


def clipboard(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        typer.echo(result)
        pyperclip.copy(result)
        return result
    return wrapper


@app.command()
@clipboard
def first_name():
    return faker.first_name()


@app.command()
@clipboard
def last_name():
    return faker.last_name()


@app.command()
@clipboard
def name():
    return faker.name()


if __name__ == '__main__':
    app()
