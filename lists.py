food = ['a','b','c','d','e']
print(food)
print(type(food))
print(food[2])
food[1]='ravi'
print(food)
for x in food:
    print(x,end='')

food.append('manu')
print(food)
food.append('Donga')
print(food)
food.insert(0,'cake')
food.insert(1,'dad')
print(food)
food.remove('dad')
print(food)
food.pop()
print(food)
food.sort()
print(food)
food.clear()
print(food)