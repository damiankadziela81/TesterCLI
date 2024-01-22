import typer

# Run from terminal, use --help for more info


def print_hi(
        yell: bool = typer.Option(False, help="Yell"),
        greet: str = typer.Option("Hi", help="Greeting"),
        name: str = typer.Option("John Doe", help="Enter name for greetings")):
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
    typer.run(print_hi)
