numbers = [10,0,-1,7,2,6,9,3,2]
names = ['manu','sai','ravi']
Mix_List = [1,'hm',True,10.01]
print(Mix_List)
'''print(numbers)
print(names[2])
print(numbers[0:4])
print(names[-1])
print(names)
print(type(numbers))
print(len(names))
print(numbers[1:3])'''
'''print(numbers)
print(numbers[1])
print(numbers[3])
print(numbers[0:])
print(numbers[:4])'''
'''print(numbers[:])
print(numbers[1:3])
print(numbers[1:4])'''
#print(numbers[0:4:2])
print(numbers)
#numbers.sort()
numbers.reverse()
print(numbers)
numbers.append('manu')
numbers.append('ravi')
numbers.insert(2,10)
numbers.insert(0,26)
numbers.extend(['kiran','joke','koli','uv-rays'])
numbers.extend(['lion','tiger','kingkong'])
numbers.pop()
numbers.remove('lion')
print(numbers.count(3))

'''for i in numbers:
    print(i)'''
'''for r in range(len(numbers)):
    print(r(numbers))'''
numbers[5]='yuvaraj'
numbers[1:4]=['ganesh','sairam','gopi','lion']
numbers.insert(6,'raju')
numbers.append('love')
numbers.extend(['pop','plion','oli','vong','sriram'])
numbers.remove('manu')
print(numbers.pop(5))
#print(numbers.clear())
del numbers[6]
print(numbers)

a = [ "ravi",'mummy','chandu','kumar','lakshman','likitha']
for i in a:
    print(i)

'''for g in range(len(a)):
    print(g[a])'''

x = [1,2,3,4,5]
y = []
for g in x:
    y.append(g*2)
print(y)

li = [g*2 for g in x]
print(li)

k = [g*2 for g in x]

d=['home','milk','lion','kingmaker']
h = []
for t in d:
    h.append(t)
print(h)

kl = [J for J in d]
print(kl)