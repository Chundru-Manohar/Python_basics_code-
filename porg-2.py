#pizza order program
size =input("What size pizza you want(S,M,L)? ")
bill = 0
if size =='s' or size=="S":
  bill += 100
  print('Small pizza price is 100 R.S')
elif size =="l" or size=="L":
  bill += 200
  print('Small pizza price is 100 R.S')
else:
  bill += 300
  print('Large pizza price is 500 r.s')
 
add_peppor = input('do you want peppor? y or n ')
if add_peppor == 'y' or add_peppor == "Y":
  if size =='S' or size=="s":
     bill += 30
     print('small pizza peppare wiil be 30')
  else:
    bill +=50
    print('M or L pizza peppare wiil be 50')
extra = input('Do you want extra chease? y or n')
if extra =='y' or extra=='Y':
        bill += 20       
print(f'total bill will be {bill} ,')