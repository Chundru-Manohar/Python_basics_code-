class Car:
    colour = None

class Motor:
    colour = None

def change(car,colour):
    car.colour = colour


car_1 = Car()
car_2 = Car()
car_3 = Car()
Bike_1 = Motor()

change(car_1,'blue')
change(car_2,'yellow')
change(car_3,'red')
change(Bike_1,'black')

print(Bike_1.colour)

print(car_1.colour)

print(car_2.colour)

print(car_3.colour)