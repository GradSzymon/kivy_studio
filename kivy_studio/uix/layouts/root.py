from kivy_studio.uix.layouts.toolbar import ToolBarLayout
from kivy_studio.uix.layouts.workspace import WorkspaceGridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color
from kivy_studio.uix.buttons.hover_button import HoverButton

class RootLayout(FloatLayout):

    top_bar = [HoverButton(text=t) for t in ['File', 'Edit', 'View', 'Mode', 'Draw', 'Scale', 'Tools', 'Game', 'Help']]
    left_bar = [HoverButton(text=t) for t in ['Sprites', 'Hierarchy']]

    def __init__(self, **kwargs):
        super(RootLayout, self).__init__(**kwargs)
        self.add_widget(ToolBarLayout(id='top', widgets=self.top_bar, cols=len(self.top_bar), pos_hint={'x': 0, 'center_y': 0.95}, size_hint=(1, .1)))
        self.add_widget(ToolBarLayout(id='left', widgets=self.left_bar, rows=len(self.left_bar), pos_hint={'x': 0, 'center_y': 0.45}, size_hint=(.222, .9)))
        self.add_widget(WorkspaceGridLayout(size=8, pos_hint={'x': 0.222, 'center_y': 0.5}, size_hint=(.8, .8)))
