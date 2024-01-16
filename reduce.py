#reduce(function , iterable)


import functools

letters= ['m','a','n','o','h','a','r']
ma = ['manoja','i','love','you']
ha = lambda x,y :x+y
mn = functools.reduce(ha,ma)
print(mn)
go = lambda x,y:x+y
world = functools.reduce(go,letters)
print(world)

factorial = [5,4,3,2,1]
result = functools.reduce(lambda x,y:x+y,factorial)
print(result)
