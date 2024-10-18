import kivy
kivy.require('2.3.0')

from kivy.core.window import Window

print("Hello World!")

from GUI import Gui

Gui().run()
Window.close()
