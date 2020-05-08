# Multi-Level Inheritance

class A:        # Parent Class
    def feature1(self):
        print('Feature1 Working...')

    def feature2(self):
        print('Feature2 Working...')


class B(A):
    def feature3(self):
        print('Feature3 Working...')

    def feature4(self):
        print('Feature4 Working...')


class C(B):
    def feature5(self):
        print('Feature5 Working...')


objA = A()
objA.feature1()
objA.feature2()

objB = B()
objB.feature1()
objB.feature2()
objB.feature3()
objB.feature4()

objC = C()
objC.feature1()
objC.feature2()
objC.feature3()
objC.feature4()
objC.feature5()
