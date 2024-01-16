#filter() create a collection of element from an iterable for which a function returns true 
#filter(function, iterable)

friends = [('emul',38),
           ('monica',17),
           ('ravi',20),
           ('roossi',26),
           ('joey',40)]

age = lambda data:data[1]>=18
Drink = list(filter(age,friends))
for i in Drink:
    print(i)