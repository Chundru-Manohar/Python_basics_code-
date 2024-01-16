temp = int(input('What is temparature outside? '))

if temp>0 and temp<30:
    print('good climate')
    print('you can go outside')
elif temp<0 or temp>30:
    print('Very hot climate')
    print('you cannot go outside')