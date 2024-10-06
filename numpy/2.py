import numpy as np
from numpy import random
a = np.zeros(17, dtype=np.int64)
print(a)

print(np.empty(4))

print(np.arange(4, 10, 2))

b = np.ones(14, dtype = np.int64)

c = np.concatenate((a, b), axis = 0)

print(c)

b = b.reshape(7, 2)
print(b)
print(b.shape)


print(c[c==0].size)


a = np.empty(5, dtype=np.int64)
b = np.empty(5, dtype=np.int64)

x=zip(a, b)

for a in x:
    print(a)

np.save('x', x)

a=np.load('x.npy')
print(a)