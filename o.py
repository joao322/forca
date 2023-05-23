from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Rectangle, Line, Ellipse
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
class l(Screen):
    def on_size(self,*args):
        with self.canvas:
            for i in range(0,2):
                Rectangle(pos=(self.width//2 , self.height/2 - 20))
class o(App):
    def build(self):
        return l()

o().run()