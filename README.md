# CSV

## Description
Use the `csvtool` command to read and write, CSV files. It's good for converting CSV between dialects. Also in this package is a `CSV` module that operates as a wrapper for Python's standard `csv` module.

## Installation
If you don't have pipx installed either run `pip3 install pipx`, or if that gives you an "externally-managed-environment" complaint, use whatever package manager is right for your operating system.

* [Debian](https://www.debian.org/doc/manuals/debian-faq/pkgtools.en.html): `apt-get install pipx`
* [Red Hat](https://www.redhat.com/en/blog/how-manage-packages): `yum install pipx`
* [HomeBrew](https://brew.sh): `brew install pipx`

Once pipx is installed, run `pipx install jc-CSV` to install the `csvtool` command to your `~/.local` directory. (Or run `pipx --global install jc-CSV` to install it for all users on your system.)

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

Once that's done, you can use the CSV module in your own code by replacing `import csv` (which just gively you Python's standard module) to `import CSV as csv` (which means you're using CSV as if it were Python's standard module, but you have access to `CSV`'s dialect handling features as well).

See the `CSV` docs below for more information.

<a id="CSV"></a>

# CSV

The CSV module is a wrapper around Python's standard csv module that
simplifies specifying and handling dialects. This makes them easy to
store in config file or read from the command line. Everything else is
just like Python's standard csv module.

## Formatting the Dialect String
CSV formatting is a loose standard with dialectic flexability. These are
the parameters involved:

* SEP: Field separator character. (default: ,)
* Q: Quote character. (default: ")
* END: Line ending. This can be C for carraige return (\r), N for
       newline (\n), or B for both (\r\n). L for linefeed is the same
       as N for newline (\n). Any other character is taken litterally
       and will be interpreted as end-of-line in an input file and will
       terminate each row written to an output file.
* QSTYLE: Quoting style. One of 'A' (all), 'M' (minimal, the default),
          'N' (non-numeric), or 'X' (none).
* DQUOTE: Represent a literal quote as two consecutive quotes. Either
          'T' (for True, the default) or 'F' (for False).
* ESC: The escape charater, which makes the next character a literal
       Use 'N' for no escaping. (default: None)
* SKIPWS: Skip whitespace immediately following a field separator. Either
          'T' (for True, the default) or 'F' (for False).
* STRICT: Raise exceptions on any little problem with the data. Either 'T'
          (for True) or 'F' (for False, the default).

The syntax of the string is SEP[Q[END[QSTYLE[DQUOTE[ESC[SKIPWS[STRICT]]]]]]].
Any values you don't specify take their default values.

<a id="CSV.__init__.dialect_string"></a>

#### dialect\_string

```python
def dialect_string(dialect, style='spec')
```

Return a string that describes the given dialect as either a
specification string (the default) or in a long, multi-line format.

<a id="CSV.__init__.parse_dialect"></a>

#### parse\_dialect

```python
def parse_dialect(dialect_name, dialect_spec)
```

Parse a dialect string, register the dialect by name, and
return the parsed dialect. See "Formatting the Dialect String" above
for what dialect_spec looks like.
