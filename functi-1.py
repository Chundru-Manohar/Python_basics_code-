def greet():
    print('hi')
    print("good morning manohar")

greet()
greet()
greet()
greet()

def add(a,b):
    c = a+b
    print(f"sum of {c}")

add(100,500)

def ra(*numbers):
  c = 0
  for i in numbers:
   c = c + i
   print(f'sum is {c}')
ra(1,2,3,4,5,6)

'''def mom(name,age,colour='red'):
   print(f"my name is {name}")
   print(f"my age is {age}")        #position
   print(f"my colour is {colour}")

mom(25,'mom')'''
'''
def mom(name,age,colour='red'):
    print(f"my name is {name}")
    print(f"my age is {age}")        #keyword Arrgument
    print(f"my colour is {colour}")

mom(age='26',name="manu")'''


'''def mom(name='ravi',age='26',colour='red'):
    print(f"my name is {name}")
    print(f"my age is {age}")        #Default Arrgument
    print(f"my colour is {colour}")

mom()'''

def tiger(*red):
   for i in red:
      print(f'hi bro how are you {i}')
    
tiger(1,2,3,4,5,6,7,8,9)

#args Kwargs;

def employee(*num,**details,):
   for m,n in details.items():
        print(m,n)
        print(num)
employee(1,2,3,name='manu',age=25,dept='python developer')
employee(2,6,name='rosie',dept="javadeveloper")

def sum(*nums):
   c=0
   for i in nums:
        c = c+i
        print(f'sum of the nums {c}')
sum(2,3,4)
   
def mu(*gold):
   for h in gold:
      print(h)
mu('hi','bro','how','are','you')

def Hd(mom, *raa):
   print("first arg is: ", mom)
   for t in raa:
      print(f"next arg  in {t}")
Hd('manu','is','a','good','boy')

def fun(**Kwargs):
   for k,l in Kwargs.items():
      print("%s == %s" % (k,l))
fun(first = 'manu',last='chundru',lucky='darling')