class Student:

    def __init__(self, mrks1, mrks2):
        self.mrks1 = mrks1
        self.mrks2 = mrks2

    def __add__(self, other):
        mrks1 = self.mrks1 + other.mrks1
        mrks2 = self.mrks2 + other.mrks2
        obj_stud3 = Student(mrks1, mrks2)
        return obj_stud3

    def __gt__(self, other):
        m1 = self.mrks1 + self.mrks2
        m2 = other.mrks1 + other.mrks2
        if m1 > m2:
            return True
        else:
            return False

    def __str__(self):
        # return self.mrks1, self.mrks2
        return '{} {}'.format(self.mrks1, self.mrks2)

obj_stud1 = Student(72, 75)  # Create Objec of Student Class
obj_stud2 = Student(63, 70)  # Create Objec of Student Class

obj_stud3 = obj_stud1 + obj_stud2
print('mrks1: ', obj_stud3.mrks1)
print('mrks2: ', obj_stud3.mrks2)

if obj_stud1 > obj_stud2:
    print("obj_stud1 Wins...")
else:
    print("obj_stud2 Wins...")

# print(obj_stud2.__str__())
print(obj_stud1)
print(obj_stud2)