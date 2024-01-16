'''count = 0
while count<10:
    print(count)
    count += 1
    if count == 8:
     continue
     print("hi")
print("out of loop")'''
for i in range(0,10):
    print(i)

a = ['hi','bye','goodnight']
b = ['ramu','ravi','manu']
for i in a:
    for j in b:
        print(i,j)
        if  i =="bye" and j=="manu":
         break
    print("out from inner loop")
print("out from outer loop ")

for u in range(1,11):
   if u == 8:
      continue
      print("hi")
   else:
      print(u)
    