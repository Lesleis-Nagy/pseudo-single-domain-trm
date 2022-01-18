r"""
Routines for database creation.
"""

import typer

from rich.console import Console
from rich.table import Table

from basecmd.orm.schema import Base
from basecmd.db import create_database


app = typer.Typer()


@app.command()
def create(file_name: str, echo: bool = False):
    r"""
    Create a new SQLite file.
    :param file_name: the name of the database file used by our program.
    :param echo: echo database creation commands.
    :return: None.
    """

    print(f"Creating database, {file_name}")
    create_database(file_name, echo=echo)


@app.command()
def tables(file_name: str = None, echo: bool = False):
    r"""
    Retrieve list of tables from the database.
    :param file_name: the name of the database file used by the program.
    :param echo: echo database commands.
    :return: None
    """

    metadata = getattr(Base, "metadata")

    print("The following tables were found ...")
    for table in metadata.sorted_tables:
        print(f"   * {table.name}")


@app.command()
def table(table_name: str, file_name: str = None, echo: bool = False):
    r"""
    Retrieve information about a table in the databse.
    :param table_name: the name of the table.
    :param file_name: the name of the database file used by the program.
    :param echo: echo database commands.
    :return: None
    """

    metadata = getattr(Base, "metadata")

    selected_table = metadata.tables.get(table_name)

    if selected_table is None:
        print(f"Table {table_name} could not be found.")
        return

    table = Table(title=f"[blue]{table_name}[/blue]")
    table.add_column("Column", justify="left")
    table.add_column("Type", justify="left")

    for col_name, col in selected_table._columns.items():
        table.add_row(str(col.name), str(col.type))

    console = Console()
    console.print(table)
