from kivymd.uix.behaviors import HoverBehavior
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex

class HoverButton(Button, HoverBehavior):
    '''Custom item implementing hover behavior.'''

    def __init__(self, bgcolor: str = '#d9d9d4', font_size: str = '18pt',  **kwargs):
       super(HoverButton, self).__init__(**kwargs)
       self.keep_color = bgcolor
       self.background_color = get_color_from_hex(bgcolor)
       self.markup=True
       self.font_size=font_size

    def on_enter(self, *args):
        '''The method will be called when the mouse cursor
        is within the borders of the current widget.'''

        self.background_color = get_color_from_hex('#40403f')

    def on_leave(self, *args):
        '''The method will be called when the mouse cursor goes beyond
        the borders of the current widget.'''

        self.background_color = get_color_from_hex(self.keep_color)