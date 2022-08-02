import setuptools
from pathlib import Path

setuptools.setup(
    # set to a unique name, so it doesn't conflict with another name in repository
    name="nikushapdf",
    version=1.0,
    # Set long_description to content of README file
    long_description=Path("README.md").read_text(),
    # indicate which packages to be distributed. Array = what to be excluded (since they don't include source code)
    packages=setuptools.find_packages(exclude=["tests", "data"])
)
