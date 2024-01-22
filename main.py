import typer
from cli.greeting import app as greeting
from cli.gen import app as gen


app = typer.Typer()
app.add_typer(greeting, name="greeting")
app.add_typer(gen, name="gen", help="Data generator")


if __name__ == '__main__':
    app()
