from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

# Library to create Mobile Application



# Define Class
class CalciApp(App):
    # Define Constructor
    def build(self):
        # Create Variables
        self.icon = "calculator.png"
        self.operators = ["%", "/", "*", "+", "-"]
        self.last_was_operator = None               # Operator
        self.last_button = None

        main_layout = BoxLayout(orientation = "vertical")

        # Results Screen
        self.solution = TextInput(background_color = "black", foreground_color = "white", multiline = False, halign = "right", font_size = 50)      # readonly=True

        # In main layout pass Results Screen
        main_layout.add_widget(self.solution)

        # Define Buttons Array
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "+"],
            [".", "0", "C", "-"]
        ]

        # In main layout Add Buttons
        for row in buttons:
            h_layout = BoxLayout()

            # Create Labels for Numbers & operators
            for label in row:
                button = Button(
                    text = label, font_size = 30, background_color = "grey",

                    # Button Position
                    pos_hint = {"center_x": 0.5, "center_y": 0.5}
                )

                # Insert Button in h_layout
                h_layout.add_widget(button)

                # To make buttons functional we will create a function named "on_button_press"
                button.bind(on_press = self.on_button_press)


            # Insert h_layout in main_layout
            main_layout.add_widget(h_layout)

        equal_button = Button(
            text="=", font_size=50, background_color="gray",

            # "=" Button Position
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )

        # To make "=" button functional we will create a funtion named "on_solution"
        equal_button.bind(on_press=self.on_solution)

        # Insert "=" button in main_layout
        main_layout.add_widget(equal_button)

        return main_layout


    # Define "on_button_press" funtion
    def on_button_press(self, instance):
        # Create Variable to store pressed value
        current = self.solution.text                    # screen text format
        button_text = instance.text

        # Clear "C" button function
        if button_text == "C":
            self.solution.text = ""

        # Only 1 operator to work at a time, means if 1 operator already pressed then should not allow to press other operator
        else:
            if current and (
                self.last_was_operator and button_text in self.operators):
                return None      # 2nd operator cant add to 1st operator

            # if screen is empty and wants to type operator then should not allow to press operator first, at 1st only digit should be pressed
            # 1st letter should be number not operator
            elif current == "" and button_text in self.operators:
                return None
            else:
                # show number and operator pressed in screen
                new_text = current + button_text
                self.solution.text = new_text

        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators



    # Define "on_solution" funtion
    def on_solution(self, instance):
        text = self.solution.text

        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution




# To Run Applcation
if __name__ == "__main__":
    app = CalciApp()
    app.run()




