from setuptools import setup, find_packages

setup(
    name="basecmd",
    version="0.0.0",
    packages=find_packages(
        where="lib",
        include="basecmd/*"
    ),
    package_dir={"": "lib"},
    install_requires=[
        "typer",
        "sqlalchemy",
        "rich"
    ],
    entry_points="""
    [console_scripts]
    my_script=basecmd.my_script:main
    """
)
