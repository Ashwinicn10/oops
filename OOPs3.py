class book():
    def __init__(self, title, author):
        self.title=title
        self.author=author

    def display_book_details(self):
        print(f"Title: {self.title}, Author: {self.author}")

class issuedbook(book):
    def __init__(self, title, author, issued_to, issued_date):
        super().__init__(title, author)
        self.issued_to=issued_to
        self.issued_date=issued_date

    def display_issued_book_details(self):
        self.display_book_details()
        print("the title of the book is", self.title)
        print("the author of the book is", self.author)
        print(f"Issued to: {self.issued_to}, Issued date: {self.issued_date}")

obj = issuedbook("Python", "George Orwell", "John Doe", "2023-01-01")
obj.display_issued_book_details()


#Single level inheritance

# class Animal:
#     def speak(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")

# d = Dog()
# d.speak()
# d.bark()


#multilevel inheritance

# class Vehicle:
#     def start(self):
#         print("Vehicle started")

# class Car(Vehicle):
#     def drive(self):
#         print("Car is driving")

# class ElectricCar(Car):
#     def charge(self):
#         print("Electric car is charging")

# e = ElectricCar()
# e.start()
# e.drive()
# e.charge()




#single inheritance

# class father:
#     def __init__(self, surname,name):
#         self.surname=surname
#         self.father_name=name
#     def display_surname(self):
#         print("surname is", self.surname)
#     def display_father_name(self):
#         print("The father name is", self.father_name)

# class son(father):
#     def __init__(self,name,surname,father_name):
#         super().__init__(surname,father_name)
#         self.name=name
#     def display_name(self):
#         print("Son's name is", self.name)

# child_obj=son("john","doe","james")
# child_obj.display_father_name()
# child_obj.display_surname()
# child_obj.display_name()