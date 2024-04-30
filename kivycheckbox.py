from kivy.app import App
from kivy.uix.checkbox import checkbox

class MinhaApp(App):
    def build(self):
        return checkbox(active=False)
    
if __name__ == "__main__":
    MinhaApp().run()