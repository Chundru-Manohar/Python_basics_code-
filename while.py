'''name = ''
while len(name) == 0:
    name = input('Enter you are name: ')
    
print('Hello '+name)

#for loop
for i in range(10):
    print(i+1)'''

for i in range(26,36+1,2):
    print(i)

a='Manohar'
for i in a:
    print(i)

import time

for i in range(10,0,-1):
    print(i)
    time.sleep(2)
print('Happy new year')

a = int(input('Enter a rows'))
b = int(input('Enter a columns'))
c = input('Enter a symbol')

for i in range(a):
    for j in range(b):
        print(c,end='')
    print()


