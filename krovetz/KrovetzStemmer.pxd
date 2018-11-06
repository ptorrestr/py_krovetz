cdef extern from "lib/KrovetzStemmer.hpp" namespace "stem":
    cdef cppclass KrovetzStemmer:
        KrovetzStemmer() except +
        int MAX_WORD_LENGTH
        char* kstem_stemmer(char *)
        int kstem_stem_tobuffer(char *, char *)
        void kstem_add_table_entry(const char*, const char*, bool)

