r"""
Useful decorators.
"""


def static(**kwargs):
    r"""
    key value pairs to add as static variables.
    """
    def wrap(func):
        for key, value in kwargs.items():
            setattr(func, key, value)
        return func
    return wrap
