class Human(object):
    can_Dance = True
    def __init__(self):
        self.Heart = 1
        self.eyes = 2

    def eat(self):
        print("I can eat food")

    def Work(self):
        print("he is a time pass")

class Male(Human):
    def __init__(self,name):
        self.name = name
    
    def sleep(self):
        print("I can sleep whole day")

class Ravi(Male):
    def __init__(self,Dance):
        self.dance = Dance
    
    def Work(self):
        Human.Work(self)
        print("he is a hard work")

class Boy(Ravi):
    def __init__(self, name,dance):
        Male.__init__(self,name)
        Ravi.__init__(self,dance)
boy_1 = Boy("Rahul","western dance")
boy_1.eat()
boy_1.sleep()
boy_1.Work()

print(boy_1.name)
print(boy_1.name)
print(boy_1.dance)
print(boy_1.can_Dance)

class Manohar():
    def code(self):
        print("i can write code ")
Ak = Manohar()
Ak.code()
