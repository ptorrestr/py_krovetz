#distutils: language = c++

from .KrovetzStemmer cimport KrovetzStemmer

cdef class PyKrovetzStemmer:
    cdef KrovetzStemmer* c_krovetz

    def __cinit__(self):
        self.c_krovetz = new KrovetzStemmer()

    def __dealloc__(self):
        del self.c_krovetz

    def stem(self, s):
        return self.c_krovetz.kstem_stemmer(s.encode('UTF-8')).decode('UTF-8')
