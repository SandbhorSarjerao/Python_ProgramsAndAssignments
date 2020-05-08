# Constructer in Inheritance

class A:        # Parent Class

    def __init__(self):
        print('In a Constructor of A => Parnent Class...')
    
    def feature1(self):
        print('Feature1 Working...')

    def feature2(self):
        print('Feature2 Working...')


class B(A):

    def __init__(self):
        super().__init__()          # calling Constructor of A => Parent Class
        print('In a Constructor of B => Child Class...')
        
    def feature3(self):
        print('Feature3 Working...')

    def feature4(self):
        print('Feature4 Working...')


objA = A()
objA.feature1()
objA.feature2()

objB = B()
objB.feature1()
objB.feature2()
objB.feature3()
objB.feature4()

