import typer
import requests
from http import HTTPStatus
from pprint import pprint
from functools import wraps
from faker import Faker

app = typer.Typer()
faker = Faker()


BASE_URL = "https://jsonplaceholder.typicode.com"
JSON_HEADERS = {'Content-type': 'application/json; charset=UTF-8'}

def print_response(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        resp: requests.Response = func(*args, **kwargs)
        pprint(resp.json())
        status_code = resp.status_code
        typer.echo(f"Response status code: {status_code} ({HTTPStatus(status_code).phrase})")
        return resp
    return wrapper

@app.command()
@print_response
def get(
        id: int or None = typer.Option(None, help="Post id (get all if not det)")
):
    url = f"{BASE_URL}/posts" if id is None else f"{BASE_URL}/posts/{id}"
    resp: requests.Response = requests.get(url=url)
    return resp


@app.command()
@print_response
def post():
    resp: requests.Response = requests.post(url=f"{BASE_URL}/posts",
                                            headers=JSON_HEADERS,
                                            json={
                                                "userId": "1",
                                                "title": faker.sentences(nb=1),
                                                "body": faker.paragraphs(nb=2),
                                            })
    return resp