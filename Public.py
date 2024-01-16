'''class Student:
    def __init__(self,name,rollno,age):
        self.name = name
        self._rollno = rollno #protected Instance variable
        self.__age = age # private

    def display(self):
        print(f"hi bro my name is {self.name} Iam vey {self._rollno} bad boy ")

s1 = Student("Rahual",25,26)
print(s1.name)
s1.display()
'''

'''a = [2,10,6,4,3,8,9,0,20]

x = 25

n = len(a)

def linearSearch(a,n,x):
    for i in range(0,n):
        if a[i] == x:
            return i 
    return -1

result = linearSearch(a,n,x)

if result == -1:
    print("Eement is not present ")
else:
    print(f"Element index:{result}" )'''
'''
list = [2,4,5,6,2,3,10,25,26,80,40]

target = 10

f = len(list)

def linerSearch(list,f,target):
    for i in range(0,f):
        if list[i] == target:
            return i
    return -1
result = linerSearch(list,f,target)

if  result == -1:
    print("element is not found")
else:
    print(f"element is present {result}")'''

#       0 1 2 3 4 5 6 7 8  9 10 11
list = [1,5,6,2,1,4,3,8,70,2,26,30]

target = 1

def linearsearch(list,target):
    for i in range(0,len(list)):
        if list[i] == target:
            return i
    return -1
result = linearsearch(list,target)
if result == -1:
    print("Element is not found")
else:
    print(f"Element is present {result}")

