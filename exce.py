'''class Circle:
    pi = 3.14# class object
    def __init__(self,r = 5):
        self.radius = r
    def Circumference(self):
       circum = 2 * self.pi * self.radius
       return circum
circle_1 = Circle()
print(circle_1.Circumference())'''


'''class Circle:
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius
        self.area = Circle.pi *radius *radius
    def Circumference_circle(self):
        return 2 *Circle.pi *self.radius
Circle_1 = Circle(4)
print(Circle_1.Circumference_circle())
print(Circle_1.area)
Circle_2 = Circle(14)
print(Circle_1.area)
print(Circle_1.Circumference_circle())'''

'''class Rectangle:
    ra = 2
    def __init__(self,length,width):
        self.lenght = length
        self.width = width
    def Height(self):
        height = self.lenght * self.width 
        return height
    
Rectangle_1 = Rectangle(5,5)
print(Rectangle_1.Height())

Rectangle_2 = Rectangle(20,20)
print(Rectangle_2.Height())
'''
'''class Parent:
    def __init__(self,heart):
        self.num_eyes = 2
        self.num_nose = 1
        self.heart = 1
    def eat(self):
        print("I can eat")
    def walk(self):
        print("I can Walk")
    def sleep(self):
        print("I can sleep at 9.30 P.M")
    

class Male(Parent):
    def __init__(self,name,Heart):
        super().__init__(Heart)
        self.name = name
    def King(self):
        print("Iam always king")
    def walk(self):
        super().walk()
        print("I can Walking daily at 3.30 P.M")
    def Display(self):
        print(f"hi my name {self.name} and I have {self.heart} heart")


Don = Male('manu',1)
Don.walk()
Don.sleep()
Don.King()
Don.walk()'''
'''print(Don.num_eyes)
print(Don.num_nose)
print(Don.heart)
Don.Display()'''

class Manu:
    def __init__(self,load):
        self.usa = 10
        self.tx = 60
        self.load = 20
    def eat(self):
        print("Iam eat the food")
    def Drink(self):
        print("Iam daily the drink")
    def Walk(self):
        print("Iam daily Walking at 9.30 P.M")

class Son(Manu):
    def __init__(self,name,load):
        super().__init__(load)
        self.name = name
    def read(self):
        print("Iam read the books")
    def Walk(self):
        super().Walk()
        print("Iam walking zero")


Manoja = Son("DON","thanu")
Manoja.eat()
Manoja.Drink()
Manoja.read()
Manoja.Walk()
print(Manoja.tx)
print(Manoja.usa)
print(Manoja.load)