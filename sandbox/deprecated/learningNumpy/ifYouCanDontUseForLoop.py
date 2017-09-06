import numpy as np
from datetime import datetime

a = np.random.randn(100)
b = np.random.randn(100)
T = 100000

#python method
def slow_dot_product(a, b):
    result = 0
    for e, f in zip(a, b):
        result += e * f
    return result


t0 = datetime.now()
for t in range(T):
    slow_dot_product(a, b)

dt1 = datetime.now() - t0


#numpy method
t0 = datetime.now()
for t in range(T):
    a.dot(b)
dt2 = datetime.now() - t0

#comparing witch is faster
print("dt1 / dt2:", dt1.total_seconds() / dt2.total_seconds())


#conclusion numpy dot function is a lot faster then for loop
