from kivy.app import app
from kivy.uix.textinput import TextInput

class minhaapp(app):
    def build(self):
        return TextInput(text='Digite Aqui')

if __name__ == "__main__":
    minhaapp().run()
    