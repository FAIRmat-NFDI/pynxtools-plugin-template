[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
![](https://github.com/FAIRmat-NFDI/pynxtools-{{{{cookiecutter.reader_name}}}}/actions/workflows/pytest.yml/badge.svg)
![](https://github.com/FAIRmat-NFDI/pynxtools-{{cookiecutter.reader_name}}/actions/workflows/pylint.yml/badge.svg)
![](https://github.com/FAIRmat-NFDI/pynxtools-{{cookiecutter.reader_name}}/actions/workflows/publish.yml/badge.svg)
![](https://img.shields.io/pypi/pyversions/pynxtools-{{cookiecutter.reader_name}})
![](https://img.shields.io/pypi/l/pynxtools-{{cookiecutter.reader_name}})
![](https://img.shields.io/pypi/v/pynxtools-{{cookiecutter.reader_name}})
![](https://coveralls.io/repos/github/FAIRmat-NFDI/pynxtools-{{cookiecutter.reader_name}}/badge.svg?branch=main)
<!-- [![DOI](https://zenodo.org/badge/759916501.svg)](https://doi.org/10.5281/zenodo.reader) -->


# A reader for XPS data

## Installation

It is recommended to use python 3.12 with a dedicated virtual environment for this package.
Learn how to manage [python versions](https://github.com/pyenv/pyenv) and
[virtual environments](https://realpython.com/python-virtual-environments-a-primer/).

This package is a reader plugin for [`pynxtools`](https://github.com/FAIRmat-NFDI/pynxtools) and thus should be installed together with `pynxtools`:

```shell
uv pip install pynxtools[{{cookiecutter.reader_name}}]
```

for the latest released version.

## Purpose

## Docs

You can more information about this pynxtools plugin in the [documentation](https://fairmat-nfdi.github.io/pynxtools-{{cookiecutter.reader_name}}/).
You can find information about getting started, how-to guides, the supported file
formats, how to get involved, and much more there.

## Contact person in FAIRmat for this reader

{{cookiecutter.author_name}}

## How to cite this work