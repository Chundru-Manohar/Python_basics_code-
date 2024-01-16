'''a = 25
def display():
    b = 15
    print(a)
display()
'''

#print(b)
a = 30
def first():
    #a = 10
    #print(a)
    def second():
        print(a)
    second()
first()

a,b = 5,6
if a<b:
    c = a + b
print(c)

import random

v = ["manu","ravi","mummy","Dad","gold","dollar","home"]
r = random.randint(0,6)
print(v[r])