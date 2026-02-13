# from abc import ABC, abstractmethod
# class Vehicle(ABC):

#     @abstractmethod
#     def start_engine(self):
#         pass

# class Car(Vehicle):
#     def start_engine(self):
#         print("Car engine started with key")

# class Bike(Vehicle):
#     def start_engine(self):
#         print("Bike engine started with kick")

# class Bus(Vehicle):
#     def start_engine(self):
#         print("Bus engine started with button")

# car = Car()
# bike = Bike()
# bus = Bus()

# car.start_engine()
# bike.start_engine()
# bus.start_engine()



from abc import ABC, abstractmethod
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    def sleep(self):
        print("Animal is sleeping")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

class Cow(Animal):
    def sound(self):
        print("Moo")
dog = Dog()
dog.sound()
dog.sleep()

cat = Cat()
cat.sound()

cow = Cow()
cow.sound()
