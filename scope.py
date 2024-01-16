#scope  

name = 'manohar'
a = 'ravi'

def Display_name():
    name = 'code'
    print(name)
    print(a)
    b = 'lion'
    print(b)


Display_name()
print(name)

def add(num1,num2):
    sum = num1+num2
    return sum

print(add(2,5))

def Add(*args):
    sum = 0
    for i in args:
        sum += i 
    return sum

print(Add(1,2,3,4,5))
#kwargs  

def hello(**jk):
  #  print('hi bro '+jk['first']+jk['last']+jk['middle'])
  for key,value in jk.items():
        print(value,end='')
    
        
hello(title = 'Mr ',first='chundru ',last='Manohar ',middle='Going ') 

# string format 
