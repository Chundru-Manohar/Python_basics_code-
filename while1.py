'''count =100
while count>0:
    print(count)
    count -= 1
    if count == 3:
        break
else:
   print("it is a else block ")

print("out of the loop ")'''

'''count = 0
while True:
    print(count)
    count += 1
    if count == 5:
      break
else:
   print('in else block ')

print("out of loop ")'''

count = 0
numb = int(input("enter 0 to 9 enter o it will ne quit? "))
while numb != 0:
    count += 1
    numb = int(input("enter 0 to 9 enter o it will ne quit? "))
print('Total is', count)


