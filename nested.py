'''b = 33 
if b%2 == 0:
    print('number is even')
    if b>20:
        print('number is greaterthan 20')
print('bye')'''
'''
height = int(input('Enter you are height?'))

if height>=3:
    print('Can you ride')
    age = int(input('Enter you are age '))
    if age<=18:
        print('please 250 Rupees')
    else:
        print('please pay 500 rupees')
else:
    print('you can\'t ride')
print('bye')'''

'''height = int(input('Enter you are height? '))

if height>=3:
    print('can you ride...')
    age = int(input('Enter you are age? '))
    if age<12:
        print('you can pay 150 R.S')
    elif age<=18:
        print('you can pay 250 R.S')
    else:
        print('you acn pay 500 R.s')
else:
    print('You can\'t ride')'''

#Boy_height = int(input("Enter you are height for men/'s ?"))

#Take input of age of 3 people by user and determine oldest and youngest among them.
print('Enter you are age ')
a = int(input('Enter you are age? '))
b = int(input('Enter you are age? '))
c = int(input('Enter you are age? '))
if a>b and a>c:
    print("youngest age a")
elif b>a and b>c:
    print("youngest age b")
elif c>a and c>b:
    print("youngest age c")

else:
  print('Bye')


#leap year 
year = int(input("Enter a year "))
if year % 4==0:
    if year %100 ==0:
        if year %400 ==0:
            print('it is a leap year')
        else:
            print('it is not a leap year')
    else:
        print('its is a leap year')
else:
    print("Its is not leap year")
