class Student:
    school_name = "Digital School"
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

student_1 = Student("Alice", 15, "Python")

student_2 = Student("Bob", 16, "Java Script")

print(student_1.name, student_1.age, student_1.course)

print(student_2.name, student_2.age, student_2.course)
