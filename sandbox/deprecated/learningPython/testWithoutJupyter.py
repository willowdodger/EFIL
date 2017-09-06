import numpy as np
import matplotlib.pyplot


a=np.zeros([3,2])


a[0, 0] = 1
a[0, 1] = 2
a[1, 0] = 9
a[2, 1] = 12
print(a)




# %matplotlib inline

matplotlib.pyplot.imshow(a, interpolation="nearest")
matplotlib
