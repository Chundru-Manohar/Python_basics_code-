#method Chaning calling multiple methos at a time

class Car:

    def trunon(self):
        print('You start the enginee ')
        return self
    def start(self):
        print('you drive the car ')
        return self
    def brake(self):
        print('you step on the brake ')
        return self
    def off(self):
        print('you can stop the car ')
        return self

car = Car()
#car.trunon().start().brake().off()

car.trunon()\
.start()\
.brake()\
.off()