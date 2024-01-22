import typer

# Run from terminal, use --help for more info


def print_hi(
        greet: str = typer.Option("Hi", help="Greeting"),
        name: str = typer.Option("John Doe", help="Enter name for greetings")):
    """ Greeting program """
    print(f'{greet} {name}')


if __name__ == '__main__':
    typer.run(print_hi)
