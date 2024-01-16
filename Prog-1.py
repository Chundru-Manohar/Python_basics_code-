height = int(input('please enter you are height? '))
if height>=3:
    bill = 0
    print('you can ride')
    age = int(input('please enter you are age? '))
    if age<=12:
        bill = 150
        print('your ticket prize is 150 R.S....')
    elif age<=18:
        bill = 250
        print('your ticket prize is 250 R.s.....')
    else:
        bill = 500
        print('your ticket prize is 500 R.S.....')
    photo = input('if you want take a photo Y/N ?')
    if photo =='Y' or photo == 'y':
        bill = bill+50
        print(f'total bill is {bill}')
else:
    print('you can\'t ride')
print('Thank you ... Enjoy the ride')

