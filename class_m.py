'''class Manohar:
    pass

manu_1 = Manohar()
print(type(manu_1))
manu_2 = Manohar()
print(type(manu_2))

class Car_Design:
    pass

new_car = Car_Design()
print(type(new_car))'''

class Employee:
    def __init__(self,names,address):
        self.ra = names
        self.add = address
        self.gold = 0

Am = Employee("manohar","rama krishna puram")
print(Am.ra)
print(Am.add)
print(Am.gold)

class Group_Members:
 contact = 0
 def __init__(self,name,Dance,Timepass,):
        self.name = name
        self.DanceA = Dance
        self.Cool = Timepass

 def Eating(self,subject_Name,):
    print(f"hi bro Iam a {self.name} and i teach {subject_Name}")
 def Update_Follwers(self,contact):
        self.contact += 1

'''
Ravi = Group_Members("Western","Hardwork",)

Ravi.Eating()
print(Ravi.DanceA)
print(Ravi.Cool)
print(Ravi.contact)
    '''
'''Manu = Group_Members("fklok","Timepass",)
print(Manu.Cool)
print(Manu.DanceA)'''
#Manu.Eating()
Manu = Group_Members("jk",'hero',"love")
Don = Group_Members("manu","Villan","Manoja")
Don.Eating("python")
Don.Update_Follwers("payal")
print(Don.contact)
Manu.Update_Follwers("sai")
Manu.Update_Follwers("kiran")
Manu.Update_Follwers("roja")
print(Manu.contact)
