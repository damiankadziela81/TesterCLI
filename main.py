import typer


def print_hi(name: str = typer.Argument("John Doe", help="Enter name for greetings")):
    ''' Greeting program '''
    print(f'Hi {name}')


if __name__ == '__main__':
    typer.run(print_hi)
