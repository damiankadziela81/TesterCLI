import typer

app = typer.Typer()


@app.command()
def person(
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
