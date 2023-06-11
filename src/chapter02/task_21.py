import numpy as np

a = np.arange(12)
print(a)

print(type(a))
print(a.shape)
a.shape = 3, 4
print(a)
print(a[2])
a.transpose()
print(a)

