#map = apples a function to each iteam in an iterable(list tuple etc)

#map(function ,iterable)

store = [('shirt',20.00),
         ('pants',25.00),
         ('jeans',30.00),
         ('socks',50.00)]

to_euros = lambda data:(data[0],data[1]*0.82)
store_euros = list(map(to_euros,store))
to_doller = lambda data : (data[0],data[1]/0.82)
store_doller = list(map(to_doller,store))
for i in store_doller:
    print(i)

for i in store_euros:
    print(i)