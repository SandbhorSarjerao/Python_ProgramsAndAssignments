class Student:

    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name = name
        self.lap = self.Laptop()  # Created Object of Inner Class

    def showInfo(self):
        print(self.rollno, self.name)
        self.lap.showInfo()


    class Laptop:

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 16

        def showInfo(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student(101, 'Sarjerao')
s2 = Student(102, 'Shivajirao')

lap1 = s1.lap
lap2 = s2.lap

lap3 = Student.Laptop()
lap4 = Student.Laptop()

s1.showInfo()
s2.showInfo()