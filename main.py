import typer
from cli.greeting import app as greeting
from cli.gen import app as gen
from cli.system import app as system
import cli.rest


app = typer.Typer()
app.add_typer(greeting, name="greeting")
app.add_typer(gen, name="gen", help="Data generator")
app.add_typer(system, name="system", help="System commands")
app.add_typer(cli.rest.app, name="rest", help="REST API")


if __name__ == '__main__':
    app()
