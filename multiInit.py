class Manohar:
    name = "ravi"
    Live = True
    Shirt = "red colour"
class Son(Manohar):
    def read(self):
        print('The person read the books ')
class Gold(Son):
    def play(self):
        print('The person play the gitar ')

gold = Gold()
print(gold.name)
gold.read()
gold.play()

s = Son()
print(s.Live)
s.read()
