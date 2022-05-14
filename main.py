
import kivy
from kivy.app import App
from kivy_studio.uix.layouts.root import RootLayout

import logging

logger = logging.getLogger(__name__)
kivy_version = '2.1.0'

class KivyStudioApp(App):
    def build(self):
        return RootLayout()

def run_studio() -> None:
    kivy.require(kivy_version)
    kivy_studio = KivyStudioApp()
    kivy_studio.run()

if __name__ == '__main__':
    try:
        run_studio()
    except Exception as e:
        logger.exception(f'Exception {e} occurred')
