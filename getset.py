
class Student:
    def __init__(self, name, id, password, grades = {}):
        self.name = name
        self.id = id

        self.__password = password
        self.__grades = grades

    def set_grade(self, subject, grade):
        self.__grades[subject] = grade

    def check_password(self, attempt):
        return attempt == self.__password

    def get_gpa(self):
        gpa = 0
        for grade in list(self.__grades.values()):
            gpa += grade
        gpa /= len(self.__grades)
        
        return gpa

student = Student(name = 'Michael', id = 0, password = 'jmaynard.1')
student.set_grade('SWE', 7)
student.set_grade('MAX', 6)

print(student.check_password('JMAYNARD.1'))
print(student.check_password('jmaynard.1'))

print(student.get_gpa())