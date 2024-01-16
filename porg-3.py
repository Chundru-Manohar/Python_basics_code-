name1 = input("Enter your are name? ")
name2 = input("Enter your are name? ")
add = name1+name2
Lower = add.lower()
t = Lower.count('t')
r = Lower.count('r')
u = Lower.count('u')
e = Lower.count('e')

ture = t+r+u+e

l = Lower.count('l')
o = Lower.count('o')
v = Lower.count('v')
e = Lower.count('e')

love = l+o+v+e

love_score = int(str(ture)+str(love))
if love_score<10 or love_score>90:
    print(f"you are score {love_score} and you go togrther like coke and mentoes ")
else:
    print(f"your love score is {love_score}")