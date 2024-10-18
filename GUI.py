import kivy
kivy.require('2.3.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp

class Gui(GridLayout):

    def __init__(self, **kwargs):
        super(Gui, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Fisrt Name + Last Initial (EX: Bart S.)'))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text='ID)'))
        self.ID = TextInput(multiline=False)
        self.add_widget(self.ID)

        self.Login = Button(text='Login', size_hint_y=None, height=44)
        self.add_widget(self.Login)
        self.Logout = Button(text='Logout', size_hint_y=None, height=44)
        self.add_widget(self.Logout)

class MyApp(App):

    def build(self):
        self.title = 'List of the endangered species'
        return Gui()
