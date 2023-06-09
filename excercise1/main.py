# %%
from sum_numbers import sum_numbers
import time


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

def run_c(n):
    res = sum_numbers(n)
    print(res)


def run_py(n):
    res = 0
    for i in range(1,n+1):
        res = res + i
    print(res)


# %%

time_ls = []
n_max = 7
for i in range(n_max):
    n = 10 ** i
        
    with timefn() as timer_c:
        run_c(n)
    time_c = timer_c.execution_time
    
    with timefn() as time_py:
        run_py(n)
    time_py = time_py.execution_time
    
    time_ls.append(time_py/time_c)

# %%
import matplotlib.pyplot as plt
plt.plot(list(map(lambda x: 10**x, range(n_max))), time_ls)
plt.xscale('log')

