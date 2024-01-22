import typer
import pyperclip
import json
from datetime import datetime
from pprint import pprint
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


@app.command()
def person(
        save: bool = typer.Option(True, help="Save to file"),
        filename: str = typer.Option("person.json", help="JSON filename")
):
    profile = faker.profile()
    # convert DECIMAL in json, bc it's not serializable
    profile['current_location'] = (str(profile['current_location'][0]),
                                   str(profile['current_location'][1]))
    # convert non serializable datetime.date format (needs datetime import)
    profile['birthdate'] = profile['birthdate'].strftime("%Y.%m.%d")
    pprint(profile)

    # when run 'python main.py gen person --no-save' it will not create the file
    if save:
        with open(filename, 'w') as json_file:
            json.dump(profile, json_file, indent=4)


if __name__ == '__main__':
    app()
