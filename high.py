fruits = ["orange","banana","lion"] # unpacking
x,y,z = fruits
'''print(x)
print(y)'''
print(z)

def Iam_back():
    print(x)
    print(y)


Iam_back()

a = "manohar"
b = " is a"
c = " good boy "
d = 100
print(a,b,c)


h = 'home'
def Manu():
    global h
    h = "Don"

Manu()

print(h)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

import random

print(random.randrange(1,10))

j = "Manohar"
print(len(j))
print(j[6])

for a in j:
   print(a)

for k in range(len(j)):
   print(k)

for fruits in "lion":
   print(fruits)


txt = "hi bro goodmorning how are you"

print("how" in txt)

message = " hi dad How are you what are you doing"
if  "doing" in message:
   print("yes doing is present ")


txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

txt = "The best things in life are free!"
print("expensive" not in txt)

b = "Hello, World!"
print(b[-5:-2])


b = "Hello, World!"
print(b[7:])
print(b[-1:-6])
print(b[:5])

c = "manohar"
print(c[0:])
print(c[4:]) 
print(c[-7:])
print(c[-7:])
o = ' mnohar is a good boy '
print(o.upper())
print(o.capitalize())
print(o.strip())
print(o.replace("ar","Dnd"))
print(o.split('*'))

a = "mr"
b ="lion"
print(a+" "+b)

'''f = 25
tf = "hi joke how are you iam " + f

print(tf)'''
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

m = 2024
new = "welcome to the new year of {}"
print(new.format(m))

name = "mummy"
n = 25
message = "my name is {0}.Iam {1} years old"
print(message.format(n,name))


going = " iam going to \"kolkata\" It is a famous places "
print(going)

width = 15
height = 12.0
print(height/3)


temp = 5
cel = 0
fahr = float(temp)
cel = (fahr - 32.0) * 5.0 / 9.0
print(cel)

for n in "banana":
   print(n)


#What is the value of i in the following code?

word = "bananana"
i = word.find("na")
print(i)

words = 'His e-mail is q-lar@freecodecamp.org'
pieces = words.split()
parts = pieces[3].split('-')
n = parts[1]
print(n)
counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
print(counts.get('kris', 0))

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key])


d = dict()
d['quincy'] = 1
d['beau'] = 5
d['kris'] = 9
for (k,i) in d.items():
    print(k, i)

import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)

f = {"manu","lion","opo"}
print(f)
print(type(f))
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set3)
set1 = {"abc", 34, True,1, 40, "male"}
print(set1)

m = set(("manu","ramu","tocabo","bamboo"))

if "manu" in m:
      print('its is present')

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")
print(thisset)
print("banana" in thisset)
      
num1 = {"red","blue"}
num2 = {"green","you are"}
num1.update(num2)
num2.update(num1)
print(num1)
print(num2)

thisset = {"apple", "banana", "cherry"}
mylist = ("kiwi", "orange")

thisset.update(mylist)

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)


thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

thisset = {"apple", "banana", "cherry"}

del thisset

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["colour"]="red"
print(thisdict["model"])
print(thisdict)
thisdict = dict(name = "John", age = 36, country = "Norway")
thisdict["colour"]="red"
l = thisdict.keys()
print(l)
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
b = thisdict["year"]
print(b)
k = thisdict.get("brand")
print(k)

v = thisdict.keys()
print(v)
f = thisdict.values()
print(f)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

car.update({"color":"blue"})
print(x) 


z = thisdict.items()
h = thisdict.keys()
j = thisdict.values()

print(z)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["brand"]="manu"
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

for x,y in thisdict.items():
   print(x,y)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

x = 14

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")



i = 0
while i <10:
   print(i)
   if i ==6:
        break
   i += 1

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1