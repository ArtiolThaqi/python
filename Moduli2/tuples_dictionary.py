grades = {
    ("John", "Math"): 5,
    ("Alice", "Biology"): 4,
    ("Eve", "Music"): 3,
    ("John", "English"): 4,
}
john_math = grades["John", "Math"]
print("John's grade in math is",john_math)

grades[("Florjon","Edukate Fizike")] = 5 #add a new item in dictionary
print(grades)

keys = list(grades.keys())
print(keys)

student, subject = keys[0]
print(student,"'s grade in ",subject, "is",john_math)