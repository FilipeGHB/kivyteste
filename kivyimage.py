from kivy.app import App
from kivy.uix.image import Image

class MinhaApp(App):
    def build(self):
        return Image(source='/Users/dinho/Pictures/eu.jpeg')
    
if __name__ == "__main__":
    MinhaApp().run()
    