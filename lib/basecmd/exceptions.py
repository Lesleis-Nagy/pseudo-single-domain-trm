r"""
A collection of exceptions thrown by parts of project-putz.
"""


class UnsetEnvironmentVariableException(Exception):
    r"""
    Exception raised for unset environment variables.
    """
    def __init__(self, variable):
        self.variable = variable
        self.message = f"The environment variable {self.variable} was not set."
        super().__init__(self.message)

    def __str__(self):
        return self.message


class FileAlreadyExistsException(Exception):
    r"""
    Exception raised if a new file already exists.
    """
    def __init__(self, file_name):
        self.file_name = file_name
        self.message = f"The file '{self.file_name}' already exists."
        super().__init__(self.message)

    def __str__(self):
        return self.message


class ProjectNotFoundException(Exception):
    r"""
    Exception raised if a project was not found.
    """
    def __init__(self, project_name):
        self.project_name = project_name
        self.message = f"The project '{self.project_name} was not found."
        super().__init__(self.message)

    def __str__(self):
        return self.message


class ProjectDirectoryMissing(Exception):
    r"""
    Exception raised if a project directory is not present on the local machine.
    """
    def __init__(self, directory):
        self.directory = directory
        self.message = f"The project directory '{self.directory}' is missing."
        super().__init__(self.message)

    def __str__(self):
        return self.message


class DestinationNotFoundException(Exception):
    r"""
    Exception raised if a the destination was not found on the remote machine.
    """

    def __init__(self, index):
        self.index = index
        self.message = f"The destination '{self.index} was not found."
        super().__init__(self.message)

    def __str__(self):
        return self.message


class PrimaryDestinationNotFoundException(Exception):
    r"""
    Exception raised if a primary destination was not found.
    """

    def __init__(self):
        self.message = "A primary destination could not be found."
        super().__init__(self.message)

    def __str__(self):
        return self.message


class DestinationsListIsEmptyException(Exception):
    r"""
    Exception raised if a poject contains no destinations.
    """

    def __init__(self):
        self.message = "The destinations list is empty."
        super().__init__(self.message)

    def __str__(self):
        return self.message


class ExcludedItemNotFoundException(Exception):
    r"""
    Exception raised if an excluded item was not found.
    """

    def __init__(self, index):
        self.index = index
        self.message = f"The excluded item '{self.index} was not found."
        super().__init__(self.message)

    def __str__(self):
        return self.message
