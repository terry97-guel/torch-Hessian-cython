import torch

cpdef process_tensor(a, b, n):
    cdef object a_ = a
    cdef object b_ = b

    cdef int i = 0

    for i in range(n):
        a_ = a_ + b_

    return a_