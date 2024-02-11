from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget



class UserInterface(App):

    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)

        title_label = Label(text="Guess the number", font_size=40, color='green', size_hint_y=None, height=110)
        self.window.add_widget(title_label)

        self.user = TextInput(multiline=False, size_hint_y=None, height=50,)
        self.window.add_widget(self.user)

        return self.window

    def on_text_input_size(self, instance, value):
        # Update center_x when the size of the TextInput changes
        self.user.center_x = self.window.width / 2

if __name__ == '__main__':
    UserInterface().run()

