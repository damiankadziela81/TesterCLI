import typer

app = typer.Typer()


@app.command()
def pang():
    typer.echo("pong")


if __name__ == '__main__':
    app()
