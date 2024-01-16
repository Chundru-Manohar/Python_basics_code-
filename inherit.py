class Mummy:

    live = True
    name = 'Manohar'
    def morning(self):
        print('The morning walkup at 6.oo AM ')
    def breakfast(self):
        print('The person is Breakfast ')
    def AfterNoon(self):
        print('the person is Eat Biryani ')
    def sleep(self):
        print('The person is sleeping at 9.00PM ')

class Amma(Mummy):
    def cook(self):
        print('The mother cook the biryani ')
class Son(Mummy):
    def reading_book(self):
        print('The son is reading books ')
class Daught(Mummy):
    def timePass(self):
        print('The time pass candidate ')

AM = Amma()
SN = Son()
FM = Daught()

print(AM.live)
AM.morning()
FM.sleep()
SN.AfterNoon()
print(SN.name)
FM.timePass()
print(FM.name)
SN.reading_book()
AM.cook()
SN.morning()
SN.AfterNoon()
SN.breakfast()
print(SN.live)
SN.reading_book()
SN.sleep()
print(SN.name)
