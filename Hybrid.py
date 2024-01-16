class A:
    def work(self):
        print("I can you are work ")
class B(A):
    def morning(self):
        print("i going to out side")

class C:
    def Afternoon(self):
        print("Iam eat the biryani food ")

class D(B,C):
    def Evening(self):
        print("Iam going to the movie ")

a = D()
a.Evening()
a.morning()
a.Afternoon()
a.work()