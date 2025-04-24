# CSV

## Description
Use the "csv" command to read and write, CSV files. It's good for changing CSV dialects. Also in this package is a "CSV" module that operates as a wrapper for Python's standard "csv" module.

## Installation
If you don't have pipx installed either run `pip3 install pipx`, or if that gives you an "externally-managed-environment" complaint, use whatever package manager is right for your operating system.

* [Debian](https://www.debian.org/doc/manuals/debian-faq/pkgtools.en.html): `apt-get install pipx`
* [Red Hat](https://www.redhat.com/en/blog/how-manage-packages): `yum install pipx`
* [HomeBrew](https://brew.sh): `brew install pipx`

Once pipx is installed, run `pipx install jc-CSV` to install the "csv" command to your `~/.local` directory. (Or run `pipx --global install jc-CSV` to install it for all users on your system.)

## Usage
```

... coming "soon" ...

```

## Using This Project's CSV Wrapper in Your Own Project
If you want to use the CSV wrapper module for Python's native csv module, include "jc-CSV" in your requirements.txt. Or if your project uses setup.py, you can tell your project to require the jc-CSV package in setup.py like this.
```python
from setuptools import setup, find_packages

setup(
...
    install_requires=[
        'jc-CSV',
    ],
...
)
```
