from kivy.uix.button import Button
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = 400,500

class Tic_Tac_ToeApp(MDApp):
  def build(self):
    return Builder.load_file('tic_tac_toe.kv')
  
class MainWidget(MDBoxLayout):
    pass
