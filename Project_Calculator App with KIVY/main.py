from kivy.app import App
from kivy.core.window import Window
Window.size = (640, 700)
import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MyRoot(BoxLayout):
    def __init__(self):
        super(MyRoot, self).__init__()


    def calc_symbol(self, symbol):
        self.calc_field.text += symbol 


    def get_result(self):
        self.calc_field.text = str(eval(self.calc_field.text))

    def clear(self):
        self.calc_field.text = ""


class mycalculator(App):
    def build(self):
        return MyRoot() 



mycalculator = mycalculator()
mycalculator.run()

