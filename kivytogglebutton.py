from kivy.app import App
from kivy.uix.togglebutton import ToggleButton

class minhaapp(App):
    def build(self):
        return ToggleButton(text='Ligado', state='normal')
    
if __name__ == "__main__":
    minhaapp().run()
    
