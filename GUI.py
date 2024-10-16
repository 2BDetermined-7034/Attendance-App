import kivy
kivy.require('2.3.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
#from kivy.core.window import Window
from kivy.uix.textinput import TextInput

class Gui(App):

    def build(self):
       return Label(text='First Name + Middle initials')


if __name__ == '__main__':
    Gui().run()
