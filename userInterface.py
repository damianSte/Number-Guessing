from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import random
import math

class UserInterface(App):

    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (1, 1)

        self.title_label = Label(text="Guess the number", font_size=40, size_hint_y=None, height=110)
        self.window.add_widget(self.title_label)

        self.user = TextInput(multiline=False, size_hint_y=None, height=60, font_size=40)
        self.user.foreground_color = (0, 1, 0, 1)
        self.user.background_color = (0.2, 0.2, 0.2, 0.2)
        self.window.add_widget(self.user)

        self.submit_btn = Button(text="Submit", font_size=40, size_hint_y=None, height=100)
        self.submit_btn.bind(on_press=self.submit_callback)
        self.window.add_widget(self.submit_btn)

        self.result_label = Label(text="Good Luck", font_size=40, size_hint_y=None, height=100)
        self.window.add_widget(self.result_label)

        self.prize_label = Label(text=" ", font_size=40, size_hint_y=None, height=100)
        self.window.add_widget(self.prize_label)

        self.prize_sum = 0

        return self.window

    def submit_callback(self, instance):
        try:
            user_guess = int(self.user.text)
        except ValueError:
            self.result_label.text = "You must enter a number"
            return

        user_guess = int(self.user.text)

        random_number = math.floor(random.random() * 100+1)

        if user_guess == random_number:
            self.title_label.text = "You guessed right!"
            self.prize_sum += 100
        elif user_guess > random_number:
            self.title_label.text = "Your guess is too high!"
            self.prize_sum -= 10
        else:
            self.title_label.text = "Your guess is too low!"
            self.prize_sum -= 10

        self.prize_label.text = str(self.prize_sum)
        self.result_label.text = f"The number was {random_number}"


if __name__ == '__main__':
    UserInterface().run()
