#!/bin/bash

set -x -e

# Install anything need (non-python tools) by this package
# Nothing to install

# Make sure no build from the system is kept. This can link
# the wheel to the host libraries.
rm -rf /io/build
rm -rf /io/tests/__pycache__

# Compile wheels
for PYBIN in /opt/python/cp3[5-7]*/bin; do
	"${PYBIN}/pip" install -r /io/requirements.txt
	"${PYBIN}/pip" wheel /io/ -w wheelhouse/
done

# Bundle external shared libraries into the wheels
for whl in wheelhouse/*.whl; do
	auditwheel show "$whl"
	auditwheel repair "$whl" -w /io/wheelhouse/
done

# Install packages and test
for PYBIN in /opt/python/cp3[5-7]*/bin/; do
	"${PYBIN}/pip" install krovetz --no-index -f /io/wheelhouse
	(cd "$HOME"; "${PYBIN}/pytest" /io/tests --benchmark-skip)
done
