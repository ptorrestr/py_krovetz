from setuptools import setup
from setuptools import Extension
from Cython.Build import cythonize
import subprocess

def readme():
  with open('README.md') as f:
    return f.read()

def version():
  out = subprocess.Popen(['git','describe','--tags'], stdout = subprocess.PIPE, universal_newlines = True)
  out.wait()
  version = "0.0.1" # default version
  if out.returncode == 0:
    m_version = out.stdout.read().strip()
    m_version = m_version.split("-")
    if len(m_version) > 0:
      version = m_version[0]
  print(version)
  return version

NAME_APP = "krovetz"
SRC_DIR = NAME_APP

ext_modules = [
  Extension(SRC_DIR + ".wrapped",
    sources = [ SRC_DIR + "/wrapped.pyx"],
    libraries = []
    )
]

setup(
  name = NAME_APP,
  version = version(),
  description = "Krovetz Stemmer",
  long_description = readme(),
  classifiers = [
    'Programming Language :: Python :: 3.6',
    'Programming Language :: C++',
  ],
  url = 'http://github.com/ptorrestr/py_krovetz',
  author = 'Pablo Torres',
  author_email = 'pablo.torres.t@gmail.com',
  license = 'GNU',
  packages = [NAME_APP],
  ext_modules = cythonize(ext_modules, compiler_directives={'embedsignature': True})
)
