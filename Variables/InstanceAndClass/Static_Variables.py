class Car:

    wheels = 4      # Class/Static Variable

    def __init__(self):
        self.milege = 18        # Instance Variable
        self.company = 'BMW'    # Instance Variable


c1 = Car()
c2 = Car()

print('Instance Variable Values for C1 Object: ', c1.milege, c1.company)
print('Instance Variable Values for C2 Object: ', c2.milege, c2.company)

c1.milege = 15
print('Updated Instance Variable Values for C1 Object: ', c1.milege, c1.company)

Car.wheels = 6      # Updated Class/Static Variable Value

print('Instance & Class/Static Variable Values for C1 Object: ', c1.milege, c1.company, c1.wheels)
print('Instance & Class/Static Variable Values for C2 Object: ', c2.milege, c2.company, c2.wheels)