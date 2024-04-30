from kivy.app import app
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import  Button
from kivy.uix.textinput import TextInput

class minhaapp(app):
    def build(self):
    layout_principal = BoxLayout(orientation='vertical')

    self.input.nome = TextInput(hint_text='Digite seu nome')
    layout_principal.add_widget(self.input)

    botao_enviar = Button(text='Enviar', on_press= self.exibir_mensagem)
    layout_principal.add_widget(self.label_mensagem)
    return layout_principal

def exibir_mensagem(self.label_mensagem)