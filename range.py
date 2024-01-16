'''a = range(2,16,2)

for i in a:
    print(i)'''

'''total = 0
for i in range(1,20):
    total += i
print(i)
'''
for i in range(-1,-10,-1):
    print(i)

#Sum of even numbers 1,100

sum = 0
for i in range(1,101):
    if i%2 == 0:
        sum += i
print(sum)

#fizz and buzz Job interview question

for i in range(1,101):
    if i%3==0 and i%5==0:
        print('Fizzbuzz')
    elif i%3==0:
        print('fizz')
    elif i%5 ==0:
        print('buzz')
    else:
        print(i)