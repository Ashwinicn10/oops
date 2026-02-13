class Student:
    college_name = "ABC College"

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    @classmethod
    def change_college(cls, new_name):
        cls.college_name = new_name

    @staticmethod
    def is_pass(marks):
        if marks >= 35:
            print("Pass")
        else:
            print("Fail")

    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"College: {Student.college_name}")

s1 = Student("Ashwini", 101)
s2 = Student("Pari", 102)

s1.display()
s2.display()

Student.change_college("MIT Engineering College")

s1.display()
s2.display()

print(Student.is_pass(80))
print(Student.is_pass(30))


