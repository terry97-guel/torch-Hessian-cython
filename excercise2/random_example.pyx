# distutils: language = c
# distutils: sources = random_example.c
# cython: cdivision = True

from libc.stdlib cimport rand


# Function to generate a random number between min_val and max_val (inclusive)
def generate_random_number(int min_val, int max_val):
    cdef int random_num = rand() % (max_val - min_val + 1) + min_val
    return random_num
