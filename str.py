# str format method that gives users more control when displaying output 

#str.format


a = 'hero'
b = 'good'
#print('hi '+a+' '+'how are you '+'iam '+b)
print('hi {} how are you im {}'.format('hero','good'))
print('hi {} how are you bro  iam {}'.format(b,a))
print('hi {d} how are you bro  iam {d}'.format(c='lion',d='liger'))

text = 'hi {} how are you bro  iam {}'
print(text.format(a,b))

name = 'manohar'
print('hello,my name is {}'.format(name))
print('hello,my name is {:10}, Nice to meet you'.format(name))
print('hello,my name is {:<10}, Nice to meet you'.format(name))
print('hello,my name is {:>10}, Nice to meet you'.format(name))
print('hello,my name is {:^10}, Nice to meet you'.format(name))

number = 1000
print('the number pi is {:.2f}'.format(number)) # floating point 
print('the number pi is {:,}'.format(number))
print('the number pi is {:b}'.format(number))# binary number 
print('the number pi is {:o}'.format(number)) #oct
print('the number is {:x}'.format(number)) #hex
print('the number is scientific notation {:E}'.format(number))