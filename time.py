import time
print(time.ctime(0))
print(time.time())
print(time.ctime(time.time()))

a = time.localtime()
print(a)
b = '20 April, 2023'
c = time.strptime(b,"%d %B, %Y")
print(c)