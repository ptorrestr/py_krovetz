#!/bin/bash

set -x -e

# Install anything need (non-python tools) by this package
# Nothing to install

# Compile wheels
for PYBIN in /opt/python/cp37*/bin; do
    "${PYBIN}/pip" install -r /io/requirements.txt
    "${PYBIN}/pip" wheel /io/ -w wheelhouse/
done

# Bundle external shared libraries into the wheels
for whl in wheelhouse/*.whl; do
	auditwheel show "$whl"
  auditwheel repair "$whl" -w /io/wheelhouse/
done

# Install packages and test
for PYBIN in /opt/python/cp37*/bin/; do
    "${PYBIN}/pip" install krovetz --no-index -f /io/wheelhouse
    (cd "$HOME"; "${PYBIN}/pytest" /io/tests --benchmark-skip)
done
