# %%
import time
class timefn:
    def __enter__(self):
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        end_time = time.time()
        execution_time = end_time - self.start_time
        
        # print(f"Execution time: {execution_time} seconds")
        # return execution_time
        self.execution_time = execution_time

# %%
import cytorch
import torch
a = torch.tensor([1,2,3])
cytorch.process_tensor(a)

# %%
import cytorch
import torch

a = torch.tensor([1,2,3])
b = torch.tensor([1,2,3])

n = 100

with timefn() as timer_c:
    cytorch.process_tensor(a,b, n)
time_c = timer_c.execution_time

with timefn() as timer_py:
    for _ in range(n):
        a = a+b
time_py = timer_c.execution_time

print(f"cython is {time_py/time_c} times faster than python")
# torch.mul(a,b)

# %%
import numpy as np

    