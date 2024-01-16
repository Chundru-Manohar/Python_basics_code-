class Animal:
    def eat(self):
        print('The animal is eating food ')
class Rabbit(Animal):
    def food(self):
        print('The Rabbit eating carrot ')
    def eat(self):
        print('The animal is person food ')

rabbit = Rabbit()
rabbit.eat()
