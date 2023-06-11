from array import array

octets = array('B', range(6))
m1 = memoryview(octets)
print(m1.tolist())
m2 = m1.cast('B', [2, 3])
print(m2.tolist())
m3 = m1.cast('B', [3, 2])
print(m3.tolist())
m2[1, 1] = 22
m3[1, 1] = 33
print(octets)
