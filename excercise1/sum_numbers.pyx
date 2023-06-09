cpdef int sum_numbers(int n):
    cdef int total = 0
    cdef int i
    for i in range(1, n + 1):
        total += i
    return total