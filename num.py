import numpy as np

import time

import sys

a = np.array([(1,2,3,4,5,6),(7,8,9,10,25,26)])
'''print(a)
a = a .reshape(6,2)
print(a)
print(a.size)
print(a.shape)'''
print(a[1][5])

b = np.linspace(1,3,5)
print(b)
c = np.linspace(1,26,6)
print(c)
d = np.array([(1,2,3),(3,4,5)])
print(np.sqrt(d))
print(np.std(d))
print(d.max())
print(d.min())
print(d.sum())


'''a = np.array((1,2,3))
b = np.array([(1,2,3),(4,5,6)])
print(a.ndim)
print(a.itemsize)
print(a.dtype)
print(b.dtype)
print(b.itemsize)
print(b.ndim)'''



'''
SIZE = 100000

L1 = range(SIZE)
L2 = range(SIZE)

a1 = np.arange(SIZE)
a2 = np.arange(SIZE)


start = time.time()

result = [(x,y) for x,y in zip(L1,L2)]
print((time.time()-start)*1000)
start=time.time()
print(result)
result = a1+a2
print((time.time()-start)*1000)



'''


'''s = range(1000)

print(sys.getsizeof(3)*len(s))

m = np.arange(1000)

print(m.size*m.itemsize)'''

'''a = np.array([(1,2,3),(4,5,6)])
print(a)
print(type(a))'''