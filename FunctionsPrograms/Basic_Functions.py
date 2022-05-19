
########### without arguments ###################
def hello_function():
    print 'Hello World, This is Function.'

hello_function()

########### with 1 argument #########################
   def greet(name):
       print("Hello, " + name + ". Good morning!")

   greet('World')

#### with 2 arguments #########

def demo(name, age):
    print(name, age)

demo("Python", 30)

########################
    
   def calculation(a, b):
       return a+b


   result = calculation(40, 10)
   print(result) 
    
  ################
  
  def calculation(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction

  result = calculation(40, 10)
  print(result)
  
  ################
  
  def calculation(a, b):
    return a + b, a - b


  add, sub = calculation(40, 10)
  print(add, sub)
