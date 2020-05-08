# Duck Typing ==> DuckTyping.py

class PyCharm:
  
  def execute(self):
      print('Compiling...')
      print('Running...')
      

class Eclipse:
  def execute(self):
      print('Spell-Check...')
      print('Code Standard Checking...')
      print('Compiling...')
      print('Running...')    

class Laptop:
    
    def code(self, ide):
        ide.execute()

# ide = PyCharm()
ide = Eclipse()
        
lap1 = Laptop()
lap1.code(ide)

