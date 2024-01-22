import typer
import platform
import subprocess

app = typer.Typer()


@app.command()
def ping(
        count: int = typer.Option(4, help="Count (0=infinite)"),
        host: str = typer.Option("google.pl", help="Host name"),
):
    cmd = ['ping']
    if platform.system() == "Darwin" and count > 0:
        cmd.extend(['-c', str(count)])
    elif platform.system() == "Windows":
        if count == 0:
            cmd.append("/t")
        elif count > 0:
            cmd.extend(['/n', str(count)])
    cmd.append(host)
    typer.echo(f"CMD: {cmd} PLATFORM: {platform.system()}")
    subprocess.run(cmd)