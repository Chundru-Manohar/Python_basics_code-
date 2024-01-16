#lameda  parameter : Expession

def double(x):
    return x * 2

a = double(2) 
print(a)

Double = lambda x: x**x
print(Double(3))

name = lambda first_name, last_name : first_name+" "+last_name
print(name('chundru','manohar'))

A = lambda x,y: x+y
print(A(5,5))

B = lambda x,y,z : x+y+z
print(B(2,4,6))

age_ch = lambda age :True if age>=18 else False
print(age_ch(20))