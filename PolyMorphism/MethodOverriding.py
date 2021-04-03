

class A:

    def showInfo(self):
        print('In Class-A-showInfo() method....')

class B(A):
    def showInfo(self):
        print('In Class-B-showInfo() method....')
        # super().showInfo()      # Calling Parent Class Method

objA = A()
objA.showInfo()

objB = B()
objB.showInfo()