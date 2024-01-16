class Manohar:
    def __init__(self,heart):
        self.eyes = 2
        self.nose = 1
        self.heart = heart
    def developer(self):
        print("Iam a python developer")
    def work(self):
        print("Iam a hard work")
    def display(self):
        print("Iam learning pandas")

class Chaitnaya:
    def __init__(self,name,home):
        self.name = name
        self.home = home
    def devops(self):
        print("I can work on the developer ")
    def work(self):
        print("I am smart work ")

class Tarun(Manohar,Chaitnaya):
    def __init__(self,name,heart,language,home):
        Manohar.__init__(self,heart)
        Chaitnaya.__init__(self,name,home)
        self.language = language
    def work(self):
        print("Iam learning Salesforce ")
    def test(self):
        print("Iam testing enginnering ")
    def display(self):
        print(f"Iam {self.name} learning {self.language} pandas")


Tarun_1 = Tarun("Rahual",1,"python","Vijayawada")
Tarun_1.developer()
Tarun_1.devops()
Tarun_1.work()
Chaitnaya.work(Tarun_1)
Tarun_1.display()
print(Tarun_1.eyes)
print(Tarun_1.nose)
Tarun_1.work()
Manohar.work(Tarun_1)
print(Tarun.mro())
print(Tarun_1.name)
print(Tarun_1.heart)
print(Tarun_1.language)
print(Tarun_1.home)
print(Chaitnaya.mro())
print(Manohar.mro())
Tarun_1.display()