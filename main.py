from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

class BosProqram(App):
def build(self):
Window.clearcolor = (0, 0, 0, 1)
return Label(
text="PROQRAM HAZIRDIR",
color=(1, 0.8, 0.2, 1),
font_size="24sp"
)

BosProqram().run()