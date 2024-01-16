'''def add(a,b):
    return a + b

fg = add(5,6)
print(fg)'''

'''def add(a,b):
    c = a + b
    print(c)

add(1,3)'''

def Namw(f_name,l_name):
    a =f_name.title()
    b = l_name.title()
    return(f'my name is {a},{b}')
z = Namw('chundru','manohar')
print(z)

import statistics

def mean_median_mode(list1):
    return statistics.mean(list1),statistics.median(list1),statistics.mode(list1)
    print("iam back")

k = mean_median_mode([3,5,10,25,26,90,70,100])
print(k)

def add(a,b):
    if a==0 and b ==0:
        return "you have enter without zero"
    else:
        return a+b
    
var1 = int(input("Enter the number:\n"))
var2 = int(input("Enter the number:\n"))
d =  add(var1,var2)
print(d)