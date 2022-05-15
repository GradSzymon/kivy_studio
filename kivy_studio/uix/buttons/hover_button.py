from kivymd.uix.behaviors import HoverBehavior
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex

class HoverButton(Button, HoverBehavior):
    '''Custom item implementing hover behavior.'''

    def __init__(self, **kwargs):
       super(HoverButton, self).__init__(**kwargs)
       self.background_color = get_color_from_hex('#d9d9d4')
       self.markup=True
       self.font_size='18pt'

    def on_enter(self, *args):
        '''The method will be called when the mouse cursor
        is within the borders of the current widget.'''

        self.background_color = get_color_from_hex('#40403f')

    def on_leave(self, *args):
        '''The method will be called when the mouse cursor goes beyond
        the borders of the current widget.'''

        self.background_color = get_color_from_hex('#d9d9d4')