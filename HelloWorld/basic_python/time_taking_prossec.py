import numpy as np
import timeit
a = np.arange(100000)
t = timeit.timeit('a**2', globals=dict(a=a))
print(t)