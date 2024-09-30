from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.anchorlayout import AnchorLayout


# Tela de Seleção de Assuntos
class SubjectSelectionScreen(Screen):
    def __init__(self, **kwargs):
        super(SubjectSelectionScreen, self).__init__(**kwargs)
        anchor_layout = AnchorLayout(anchor_y='center')  
        self.add_widget(anchor_layout)
        
        layout = BoxLayout(orientation='vertical', padding=[20, 160, 20, 60], spacing=10)
        anchor_layout.add_widget(layout)

        
        layout.add_widget(Label(text='Áreas de Conhecimento', font_size='24sp'))
        
        btn_ciencias_humanas = Button(text='Ciências Humanas', size_hint=(None, None), width=520, height=40, pos_hint={'center_x': 0.5})
        btn_ciencias_natureza = Button(text='Ciências da Natureza', size_hint=(None, None), width=520, height=40, pos_hint={'center_x': 0.5})
        btn_linguagens = Button(text='Linguagens e Códigos',size_hint=(None, None), width=520, height=40, pos_hint={'center_x': 0.5})
        btn_matematica = Button(text='Matemática', size_hint=(None, None), width=520, height=40, pos_hint={'center_x': 0.5})
        back_btn = Button(text='Voltar', size_hint=(None, None), width=220, height=40, pos_hint={'center_x': 0.5})
        
        layout.add_widget(btn_ciencias_humanas)
        layout.add_widget(btn_ciencias_natureza)
        layout.add_widget(btn_linguagens)
        layout.add_widget(btn_matematica)
        layout.add_widget(back_btn)
        
        btn_ciencias_natureza.bind(on_press=self.go_to_nature_sciences)
        btn_ciencias_humanas.bind(on_press=self.go_to_ciencias_humanas)
        btn_linguagens.bind(on_press=self.go_to_linguagens)
        btn_matematica.bind(on_press=self.go_to_matematica)
        back_btn.bind(on_press=self.go_to_login)

    def go_to_nature_sciences(self, instance):
        self.manager.current = 'nature_sciences'

    def go_to_ciencias_humanas(self, instance):
        self.manager.current = 'ciencias_humanas'

    def go_to_linguagens(self, instance):
        self.manager.current = 'linguagens_codigos'

    def go_to_matematica(self, instance):
        self.manager.current = 'matematica'

    def go_to_login(self, instance):
        self.manager.current = 'login'
