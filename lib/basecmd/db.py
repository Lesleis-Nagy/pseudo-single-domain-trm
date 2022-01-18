r"""
Routines to load database session.
"""

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.pool import NullPool

from basecmd.decorators import static

from basecmd.exceptions import FileAlreadyExistsException

from basecmd.configuration import get_db_file_from_env

from basecmd import GLOBAL_VARS

from basecmd.orm.schema import Base


@static(engine=None, Session=None)
def get_session(file_name=None, echo=False):
    r"""
    Retrieve a session to the database, which is either explicitly  located in `file_name`, otherwise,
    try to use the GLOBALS.CLI_ENV_VARIABLE variable, if this is not available then there is an error.
    :param file_name: an optional file name (by default none is given).
    :param echo: echo connection details (by default this is not set).
    :return:
    """
    if file_name is not None:
        if not os.path.isfile(file_name):
            raise FileNotFoundError(f"Could not find database file {file_name}")
    else:
        file_name = get_db_file_from_env()

    # Check that the file exists
    if not os.path.isfile(file_name):
        raise FileNotFoundError(f"The database file '{file_name}' was not found.")

    if get_session.engine is None:
        uri = GLOBAL_VARS.SQLITE_FILE_URI.format(file_name=file_name)
        get_session.engine = create_engine(uri, echo=echo)

    if get_session.Session is None:
        get_session.Session = sessionmaker(
            bind=get_session.engine,
            autoflush=True,
            autocommit=False
        )

    return get_session.Session()


def create_database(file_name, echo=False):
    r"""
    Create a new database.
    :param file_name: the file name of the new database.
    :param echo: set to True to echo SQL statements.
    :return: None.
    """
    # Check that the file already exists.
    if os.path.isfile(file_name):
        raise FileAlreadyExistsException(file_name)

    uri = GLOBAL_VARS.SQLITE_FILE_URI.format(file_name=file_name)

    engine = create_engine(uri, echo=echo)

    if hasattr(Base, "metadata"):
        metadata = getattr(Base, "metadata")
        metadata.create_all(engine)
    else:
        raise AssertionError("Fatal, Base class as no attribute 'metadata'.")
