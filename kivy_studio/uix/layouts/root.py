from kivy.uix.pagelayout import PageLayout
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color

class RootLayout(PageLayout):

    def __init__(self, **kwargs):
        super(RootLayout, self).__init__(**kwargs)
        with self.canvas:
 
            Color(.234, .456, .678, .8)  # set the colour
 
            # Setting the size and position of canvas
            self.rect = Rectangle(pos = self.center,
                                  size =(self.width / 2.,
                                        self.height / 2.))
 
            # Update the canvas as the screen size change
            self.bind(pos = self.update_rect,
                  size = self.update_rect)
            # update function which makes the canvas adjustable.
            self.add_widget(Label(text=('Hello [b][color=ff0000]Kivy[/color][color=fcba03]Studio[/color][/b]'), markup=True, font_size='12pt'))

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
