[![Build Status](https://travis-ci.org/ptorrestr/py_krovetz.svg?branch=master)](https://travis-ci.org/ptorrestr/py_krovetz)

# Py Krovetz

This is a Python wrapper for [Krovetz Stemmer C++ library](https://sourceforge.net/p/lemur/wiki/KrovetzStemmer). It uses Cython to build a wrapper and allow access to the cpp object in python.

## Installation

### Pypi

`pip install -i https://test.pypi.org/simple/ krovetz`

### Git

It requires `cython` to be installed.

`pip install git+https://github.com/ptorrestr/py_krovetz.git`

## Development

## Import
`git clone https://github.com/ptorrestr/py_krovetz.git`

### Environment setup
It requires `pipenv` to be installed.
`pipenv install`

### Testing
`pienv run python setup.py test`

## Usage

```python
import krovetz
ks = krovetz.PyKrovetzStemmer()
ks.stem('walked')
```
