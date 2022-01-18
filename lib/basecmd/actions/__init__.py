import typer

app = typer.Typer()


@app.command()
def create_db(file_name):
    r"""
    Create a new SQLite file.
    :param file_name: the name of the database file used by our program.
    :return: None.
    """

    print(f"Creating database, {file_name}")
