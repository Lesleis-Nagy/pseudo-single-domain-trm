r"""
Retrieve configuration information.
"""
import os

from basecmd.exceptions import UnsetEnvironmentVariableException

from basecmd import GLOBAL_VARS


def get_db_file_from_env():
    r"""
    Retrieve the database file from the environment variable.
    :return: the database file (or None)
    """
    cli_env_variable_value = os.environ.get(GLOBAL_VARS.CLI_ENV_VARIABLE)

    if cli_env_variable_value is None:
        raise UnsetEnvironmentVariableException(GLOBAL_VARS.CLI_ENV_VARIABLE)

    return cli_env_variable_value
