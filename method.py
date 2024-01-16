class Nana:
    def add(self,x,y):
        print(x + y)
    def add(self,x,y,z=0):
        print(x+y+z)
    def add(self,*args):
        total = 0
        for i in args:
            total = total +i
        return total
    

s = Nana()
s.add(1,2)
s.add(2,3,5)
s.add(2,3,5,6,7,8,9,10,26)
print(s.add(2,3,5,6,7,8,9,10,26))