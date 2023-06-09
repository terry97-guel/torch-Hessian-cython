import torch

def elementwise_multiply(torch.Tensor a, torch.Tensor b):
    cdef torch.Tensor result = torch.empty_like(a)
    '''
    cdef int numel = a.numel()
    
    cdef double* a_data = <double*>a.data_ptr()
    cdef double* b_data = <double*>b.data_ptr()
    cdef double* result_data = <double*>result.data_ptr()
    
    for i in range(numel):
        result_data[i] = a_data[i] * b_data[i]
    '''
    return result
