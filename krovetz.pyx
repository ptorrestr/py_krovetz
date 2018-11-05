#cython: language_level=3,
#distutils: language = c++

from KrovetzStemmer cimport KrovetzStemmer

cdef class PyKrovetzStemmer:
    cdef KrovetzStemmer c_krovetz

    def __cinit__(self):
        self.c_krovetz = KrovetzStemmer()

    def kstem_stemmer(self, char* s):
        return self.c_rect.k_stem_stemmer(s)
