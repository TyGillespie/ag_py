"""Setup script.

Call with
pip install .
"""

from setuptools import setup, find_packages


__version__: float = 0.12

with open("readme.md", "r") as f:
    long_description: str = f.read()

setup(
    name="ag_py",
    version=__version__,
    author="Ty Gillespie",
    author_email="turret1226@gmail.com",
    description="A basic Audiogame Engine.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/tygillespie/agpy",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
    ],
    python_requires=">=3",
)
