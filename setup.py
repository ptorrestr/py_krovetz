from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

#ext_modules = [
#  Extension("demo",
#    sources = ["krovetz.pyx"],
#    libraries = ["m"]
#    )
#]

#setup(ext_modules = cythonize(ext_modules, gdb_debug=True))
setup(ext_modules=cythonize("krovetz.pyx"))
