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
import torch
from torch.nn import Sequential, Linear


layers = []
layers.append(Linear(3,2))

model = Sequential(*layers)

# %%
motor_control = torch.rand([4,3])
model(motor_control)
# %%
from torch.autograd.functional import jacobian

with timefn() as timer:
    jac_ls = []
    for motor_control_ in motor_control:
        jac = jacobian(model, motor_control_)
        jac_ls.append(jac)

    temp1 = torch.stack(jac_ls)
    
time_ele = timer.execution_time

# %%
with timefn() as timer:
    jac = jacobian(model, motor_control)
    index = torch.tile(torch.eye(4, dtype=torch.bool),(2,3,1,1)).permute([2,0,3,1])
    temp2 = jac[index].reshape(4,2,3)
    
time_total = timer.execution_time

assert (temp1 == temp2).all()
# %%
from matplotlib import pyplot as plt

plt.bar(["elementwise", "total"], [time_ele, time_total])
# %%



# %%

selected_elements = torch.tensor[:, :, torch.arange(N), :]

# %%
from torch.autograd.functional import hessian

def model_elementwise(motor_control):
    return model(motor_control)[i]
hessian(model, motor_control[:1,:])