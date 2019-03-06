from setuptools import setup
from setuptools import Extension
import subprocess
import os

root_path = os.path.dirname(os.path.realpath(__file__))
readme_file_path = os.path.join(root_path, 'README.md')
version_file_path = os.path.join(root_path, 'VERSION')
NAME_APP = "krovetz"
src_path = NAME_APP

def readme():
  with open(readme_file_path) as f:
    return f.read()

def version():
  # default version
  version = "0.0.1"
  # Get version from git if any
  out = subprocess.Popen(['git','describe','--tags'],
    stdout = subprocess.PIPE, universal_newlines = True)
  out.wait()
  # If version is available
  if out.returncode == 0:
    m_version = out.stdout.read().strip()
    m_version = m_version.split("-")
    if len(m_version) > 0:
      version = m_version[0]
      # Save to a file for futher readings
      with open(version_file_path,'w') as f:
        f.write(version)
  else:
    # When git is not available, we check the file
    # This is the case when the code is distributed
    with open(version_file_path) as f:
      version = f.read()
  print(version)
  return version

try:
  import Cython
  USE_CYTHON = True
except:
  USE_CYTHON = False

ext = ".pyx" if USE_CYTHON else ".cpp"

import platform
extra_compile_args = ["-std=c++11"]
extra_link_args = []
if platform.system() == 'Darwin':
    extra_compile_args.append("-stdlib=libc++")
    extra_compile_args.append("-mmacosx-version-min=10.9")
    extra_link_args.append("-mmacosx-version-min=10.9")

ext_modules = [
  Extension(src_path + ".wrapped",
    sources = [ src_path + "/wrapped" + ext, src_path + "/lib/KrovetzStemmer.cpp"],
    include_dirs = [src_path + "/lib"],
    libraries = [],
    extra_compile_args = extra_compile_args,
    extra_link_args = extra_link_args
    )
]

if USE_CYTHON:
  from Cython.Build import cythonize
  ext_modules = cythonize(ext_modules,
    compiler_directives = {'language_level': '3',
      'c_string_type': 'unicode',
      'c_string_encoding':'default'
    }
  )

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
  license = 'MIT',
  packages = [NAME_APP],
  ext_modules = ext_modules,
  setup_requires = ['pytest-runner'],
  install_requires = [],
  tests_require = ['pytest','pytest-benchmark'],
  test_suite = 'tests',
)
