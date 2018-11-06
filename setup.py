from setuptools import setup
from setuptools import Extension
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

try:
  import Cython
  USE_CYTHON = True
except:
  USE_CYTHON = False

ext = ".pyx" if USE_CYTHON else ".cpp"

ext_modules = [
  Extension(SRC_DIR + ".wrapped",
    sources = [ SRC_DIR + "/wrapped" + ext, SRC_DIR + "/lib/KrovetzStemmer.cpp"],
    include_dirs = [SRC_DIR + "/lib"],
    libraries = [],
    extra_compile_args = ["-std=c++11"]
    )
]

if USE_CYTHON:
  from Cython.Build import cythonize
  ext_modules = cythonize(ext_modules)

setup(
  name = NAME_APP,
  version = version(),
  description = "Krovetz Stemmer",
  long_description = readme(),
  long_description_content_type = 'text/markdown',
  classifiers = [
    'Programming Language :: Python :: 3.6',
    'Programming Language :: C++',
  ],
  url = 'http://github.com/ptorrestr/py_krovetz',
  author = 'Pablo Torres',
  author_email = 'pablo.torres.t@gmail.com',
  license = 'GNU',
  packages = [NAME_APP],
  ext_modules = ext_modules,
  setup_requires = [],
  install_requires = [],
  test_requires = ['pytest','pytest-runner'],
)
