a =(1,2,3)*5
b = ('mani','ravi','hion','open')*5
c = ('manu',1.0,True,2,"manu")
d = (10,)
e = (10)
print(type(d))
print(type(e))
print(c[0])
print(c[-1])
print(c)
print(c[1:5])
o = (b,c)
print(o)
print(o[1])
print(len(o))
print(max(a))
print(min(a))
print(c.count('manu'))
print(c.index('manu'))

jol = [1,2,3,4,5,6,7,8,9]
print(tuple(jol))

m = ['manu','ravi']
print(tuple(m))
print(a)
print(b)