from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class minha(App):
    def build(self):
        layout = BoxLayout(orientation= 'vertical', spacing=10)

        btn1 = Button(text='Botão 1', background_color=(0.2, 0.7, 0.3, 1), font_size=30)
        layout.add_widget(btn1)

        btn2 = Button(text='Clique Aqui', halign= 'center')
        layout.add_widget(btn2)
        
        btn3 = Button(text='Clique para Continuar', background_calor=(0.9, 0.5, 0.1, 1), font_size=20)
        layout.add_widget(btn3)
