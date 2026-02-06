#hybrid inherotance
class Person:
    def __init__(self, name):
        self.name = name

    def display_person(self):
        print(f"Name: {self.name}")


class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    def display_student(self):
        print(f"Student ID: {self.student_id}")


class SportsPlayer(Person):
    def __init__(self, name, sport_name):
        super().__init__(name)
        self.sport_name = sport_name

    def display_sports_player(self):
        print(f"Sport: {self.sport_name}")


class CollegeStudent(Student, SportsPlayer):
    def __init__(self, name, student_id, sport_name, college_name):
        Student.__init__(self, name, student_id)
        SportsPlayer.__init__(self, name, sport_name)
        self.college_name = college_name

    def display_college_student(self):
        self.display_person()
        self.display_student()
        self.display_sports_player()
        print(f"College: {self.college_name}")



college_student = CollegeStudent("Ashwini","ST123","Cricket","MITT Engineering College")
college_student.display_college_student()
