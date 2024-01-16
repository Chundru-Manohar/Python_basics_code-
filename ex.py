#exception 
try:
    numerator= int(input('Enter a number numerator '))
    denominator=int(input('Enter a number denominator '))
    result= numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print('you cant divided zero')
except ValueError as e:
    print(e)
    print('Enter only numbers plz')
except Exception as e:
    print(e)
    print('Something went wrong: (')  
else:
    print(result)
finally:
    print('this will always execuite')
    