import random

a = random.randint(1,3) 
print(a)
b = random.randrange(1,3)
print(b)
c = random.random()
print(c)
d = random.uniform(1,3)
print(d)
e = [2,5,15,25,30,38,50]
#f = random.choice(e)
#print(f)
g = random.shuffle(e)
print(g)

side = random.randint(0,1)
print(side)
if side ==1:
    print('heads')
else:
    print('Tails')