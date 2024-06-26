from kivy.app import app
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import  Button
from kivy.uix.textinput import TextInput

class minhaapp(app):
    def build(self):
        layout_principal = BoxLayout(orientation='vertical')

        self.input.nome = TextInput(hint_text='Digite seu nome')
        layout_principal.add_widget(self.input_nome)

        botao_enviar = Button(text='Enviar', on_press=self.exibir_mensagem)
        layout_principal.add_widget(botao_enviar)

        self.label_mensagem = Label()
        layout_principal.add_widget(self.label_mensagem)
        
        return layout_principal

def exibir_mensagem(self, instance):
    nome_usuario = self.input_nome.text
    mensagem = f'Olá {nome_usuario}, você está avaçando no kivy! Parabéns SESIANO!!!'
    self.label_mensagem.text = mensagem
    
if __name__ == "__main__":
    minhaapp().run()