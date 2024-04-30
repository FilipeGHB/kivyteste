from kivy.app import App
from kivy.uix import slider

class MinhaApp(App):
    def build(self):
        return slider(min=0, max=100, value=50)
    
if __name__ == "__main__":
    MinhaApp().run()
    