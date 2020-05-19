import kivy.utils
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout


class HeaderBanner(GridLayout):
    rows = 1
    def __init__(self, **kwargs):
        super().__init__()

        with self.canvas.before:
            Color(rgb=(kivy.utils.get_color_from_hex('#e5f8fc')))
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(pos=self.update_rect,size=self.update_rect)
        

       # Need left FloatLayout
        left = FloatLayout()
        left_label = Label(text=kwargs['header'], size_hint=(1, .2), pos_hint={"top": .225, "right": 1}, color = kivy.utils.get_color_from_hex('#000000'))
        left.add_widget(left_label)

        self.add_widget(left)
        # self.add_widget(right)
    
    def update_rect(self, *args):
        self.rect.pos  = self.pos
        self.rect.size = self.size