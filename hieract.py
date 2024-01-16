class Manohar:
    def __init__(self,name,age,heart):
        self.eyes = 2
        self.noise = 1
        self.heart = heart
        self.name = name
        self.age = age 
        
    def eat(self):
        print("i can eat")

class Manoja(Manohar):
    def __init__(self,name,age,location,heart):
        Manohar.__init__(self,name,age,heart)
        self.location = location
    def food(self):
        print("I can prepared the food daily")

class Ravi(Manohar):
    def walk(self):
        print("i can walk daily")



'''
ravi_1 = Ravi(1)
ravi_1.eat()
ravi_1.walk()

print(ravi_1.heart)
Manoja_1 = Manoja(1)
Manoja_1.food()
Manoja_1.eat()'''

jk = Manoja("manu","25","Vijayawada","1")
print(jk.name)