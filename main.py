import typer
from cli.greeting import app as greeting
from cli.ping import app as ping

# Run from terminal, use --help for more info
# how to run after structure changes:
# python main.py ping pang
# python main.py greeting person

app = typer.Typer()
app.add_typer(greeting, name="greeting")
app.add_typer(ping, name='ping')


if __name__ == '__main__':
    app()
