
import cython

cpdef int point_calculate(unicode screet_word, int rights) except? -1:

    rights = rights if rights>0 else 0
    return len(screet_word)*rights

cpdef bint is_word_guessed(unicode screet_word, unicode letters_guessed) except? -1:

    for i in set(screet_word):
        if i not in list(letters_guessed):
            return 0
    
    return 1
