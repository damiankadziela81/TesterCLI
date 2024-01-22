import typer

# Run from terminal, use --help for more info

app = typer.Typer()


@app.command()
def ping():
    typer.echo("pong")


# now to access 'greeting' specific help run 'python main.py greeting --help' in terminal
@app.command()
def greeting(
        yell: bool = typer.Option(False, help="Yell", prompt="Yell?"),
        greet: str = typer.Option("Hi", help="Greeting",prompt="Enter greeting"),
        name: str = typer.Option("John Doe", help="Enter name for greetings", prompt="Enter name")
):
    """ Greeting program """
    if yell:
        typer.echo(typer.style(
            f'{greet} {name} !!!',
            fg=typer.colors.BRIGHT_WHITE,
            bg=typer.colors.BRIGHT_RED
        ))
    else:
        print(f'{greet} {name}')


if __name__ == '__main__':
    app()
