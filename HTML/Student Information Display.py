class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display_info(self):
        print("Name:", self.name)
        print("Grade:", self.grade)

s1 = Student("Aisha", "8th")
s1.display_info()