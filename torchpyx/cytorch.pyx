import torch
from torch.autograd.functional import jacobian
from cython.parallel cimport prange

cpdef process_tensor(a, b, n):
    assert isinstance(torch.Tensor, a)
    assert isinstance(torch.Tensor, b)


    length = len(motor_control)
    cdef object motor_control_ = motor_control[0]
    for i in prange(length, nogil=True):
        motor_control_ = motor_control[i]
        jac = jacobian(model, motor_control_)

    return jac_ls
    