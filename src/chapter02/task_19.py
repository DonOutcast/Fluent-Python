from array import array
from random import random

floats = array('d', (random() for _ in range(10**7)))
print(floats[-1])

with open("floats.bin", "wb") as f:
    floats.tofile(f)

floats2 = array('d')

with open("floats.bin", "rb") as f:
    floats2.fromfile(f, 10**7)

floats2[-1]

assert floats2 == floats

