import kivy
kivy.require('2.3.0')

from kivy.core.window import Window

from GUI import MyApp
from Attendance_logic import Student, main

MyApp().run()
Window.close()
