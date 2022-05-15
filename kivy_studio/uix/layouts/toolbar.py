from typing import Tuple
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color
from kivy_studio.uix.buttons.hover_button import HoverButton


class ToolBarLayout(GridLayout):
    def __init__(self, id: str, rows: int = 3, cols: int = 3, **kwargs):
        super(ToolBarLayout, self).__init__(**kwargs)
        self.id = id
        self.rows = rows
        self.cols = cols
        self.add_widget(HoverButton(text='File'))
        self.add_widget(HoverButton(text='Edit'))
        self.add_widget(HoverButton(text='View'))
        self.add_widget(HoverButton(text='Mode'))
        self.add_widget(HoverButton(text='Draw'))
        self.add_widget(HoverButton(text='Scale'))
        self.add_widget(HoverButton(text='Tools'))
        self.add_widget(HoverButton(text='Game'))
        self.add_widget(HoverButton(text='Help'))
