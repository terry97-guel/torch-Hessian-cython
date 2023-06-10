cpdef int sum_numbers(long n):
    cdef long total = 0
    # cdef int i
    for i in range(1, n + 1):
        total += i
    return total