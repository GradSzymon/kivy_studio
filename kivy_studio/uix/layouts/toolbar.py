from typing import Any, List
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color


class ToolBarLayout(GridLayout):
    def __init__(self, widgets: List[Any], id: str, rows: int = 1, cols: int = 1, **kwargs):
        super(ToolBarLayout, self).__init__(**kwargs)
        self.id = id
        self.rows = rows
        self.cols = cols
        for widget in widgets:
            self.add_widget(widget)
