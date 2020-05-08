
class Student:
    university = 'Pune University'      # Class/Static Variable
    college = 'Modern College'

    def __init__(self, mrks1, mrks2, mrks3):
        self.mrks1 = mrks1      # Instance Variable
        self.mrks2 = mrks2
        self.mrks3 = mrks3

    def set_mrks1(self, value):         # Setter/Mutator Methods
        self.mrks1 = value

    def set_mrks2(self, value):
        self.mrks2 = value

    def set_mrks3(self, value):
        self.mrks3 = value

    def get_mrks1(self):                # Getter/Accessor Methods
        return self.mrks1

    def get_mrks2(self):
        return self.mrks2

    def get_mrks3(self):
        return self.mrks3

    def average_marks(self):        # Instance Method - used self keyword
        return (self.mrks1 + self.mrks2 + self.mrks3) / 3

    @classmethod
    def getCollegeName(cls):        # Class Method
        return cls.college

    @staticmethod
    def getUniversityName():
        return Student.university


stud_obj1 = Student(66, 72, 75)
stud_obj2 = Student(69, 57, 81)

print('Average of 1st Stud Object: ', stud_obj1.average_marks())
print('Average of 2nd Stud Object: ', stud_obj2.average_marks())

print('CollegeName: ', Student.getCollegeName())        # Calling Class Method
print('UniversityName: ', Student.getUniversityName())  # Calling Static Method
