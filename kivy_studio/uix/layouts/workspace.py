from kivy.uix.gridlayout import GridLayout
from kivy_studio.uix.buttons.hover_button import HoverButton

class WorkspaceGridLayout(GridLayout):
    
    def __init__(self, size: int = 2, **kwargs):
        super(WorkspaceGridLayout, self).__init__(**kwargs)
        self.cols = size
        self.rows = size
        self.workspace_size = size*size
        for _ in range(self.workspace_size):
            self.add_widget(HoverButton(text=('[b][color=ff0000]Kivy[/color][color=fcba03]Studio[/color][/b]'), font_size='4pt', bgcolor ='#249cff'))
