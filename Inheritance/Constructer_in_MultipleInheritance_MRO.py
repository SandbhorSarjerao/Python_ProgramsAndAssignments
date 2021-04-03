# Constructer in Multiple Inheritance

class A:		# Parent Class

  def __init__(self):
      print('Class A Constructor...')
  
	def feature1(self):
		print('Feature1-A Working...')
		
	def feature2(self):
		print('Feature2 Working...')


class B():

  def __init__(self):
      print('Class B Constructor...')
      
	def feature1(self):
		print('Feature1-B Working...')
		
	def feature3(self):
		print('Feature4 Working...')


class C(A, B):

    def __init__(self):
      super().__init__()        # MRO - Method Resolution Order
      print('Child Class C Constructor...')
      
  	def feature3(self):
		print('Feature5 Working...')
		
    def feature5(self):
      super().feature2()
      super().feature3()
		
objA = A()
objA.feature1()
objA.feature2()

objB = B()
objB.feature3()
objB.feature4()

objC = C()
objC.feature1()     # Calling this Function as per MRO
objC.feature2()
objC.feature3()
objC.feature4()
objC.feature5()

