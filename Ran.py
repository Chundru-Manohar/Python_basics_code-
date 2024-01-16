import random

x = random.randint(1,6)
y = random.random()
#print(y)

mylist = ['rock','paper','scissors']
z = random.choice(mylist)
print(z)

a = ['manu','lion','tiger','liger','home']
b = random.choice(a)
print(b)

cards = [1,2,3,4,5,6,7,8,9,'M','N','G','H']

random.shuffle(cards)
print(cards)