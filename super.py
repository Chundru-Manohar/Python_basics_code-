'''class Add():
     def __init__(self,a,b):
        self.a = a
        self.b = b
class Subs(Add):
    def __init__(self,a,b):
     super().__init__(a,b)
    def area(self):
        return self.a*self.b
    
class Mult(Add):
    def __init__(self,a,b,c):
       super().__init__(a,b)
       self.c = c
    def volume(self):
        return self.a*self.b*self.c
    
s = Subs(2,2)
m = Mult(3,3,3)
print(s.area())
print(m.volume())
'''

class Go():
    def __init__(self,length,width):
        self.length = length
        self.width = width
class Square(Go):
    def __init__(self,length,width):
     super().__init__(length,width)
    def area(self):
        return self.length*self.width
        
class Cube(Go):
    def __init__(self,length,width,height):
        super().__init__(length,width)
        self.height = height
    def volume(self):
        return self.length*self.width*self.height
    
s = Square(6,6)
c = Cube(5,5,5)

print(c.volume())
print(s.area())
        
