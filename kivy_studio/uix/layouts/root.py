from kivy_studio.uix.layouts.toolbar import ToolBarLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color

class RootLayout(FloatLayout):

    def __init__(self, **kwargs):
        super(RootLayout, self).__init__(**kwargs)
        self.add_widget(Label(text=('[color=000000]Hello [b][color=ff0000]Kivy[/color][color=fcba03]Studio[/color][/b]'), markup=True, font_size='12pt'))
        self.add_widget(ToolBarLayout(id='top', rows=1, cols=9, pos_hint={'x': 0, 'center_y': 0.95}, size_hint=(1, .1)))
        self.add_widget(ToolBarLayout(id='left', rows=9, cols=1, pos_hint={'x': 0, 'center_y': 0.45}, size_hint=(.222, .9)))
