class Student:
    university = "SkillWill"

    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

    @property
    def is_passing(self):
        return self.grade > 60

    def increase_grade(self, increase_by):
        self.grade += increase_by
stu = Student("Nick", 70, 10)
print(stu.is_passing)
stu.increase_grade(10)
print(stu.grade)