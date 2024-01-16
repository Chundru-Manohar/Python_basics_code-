class Duck:
    def swim(self):
        print("I am duck. Iam can swim ")
    def speak(self):
        print("Iam can speak queak")
class Dog:
    def swim(self):
        print("Iam a dog.I can Swim ")
    def speak(self):
        print("Iam a dog i can speak Bow Bow")

def Display(ha):
    ha.swim()
    ha.speak()
    print("information Dispayed")

M = Dog()
Display(M)
d = Duck()
Display(d)

print(1+2)
print('1'+'2')
print(int.__add__(1,2))
print(str.__add__('1','2'))