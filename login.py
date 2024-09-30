from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout

# Tela de Login 
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        
        # Layout principal, usando AnchorLayout para centralizar verticalmente
        anchor_layout = AnchorLayout(anchor_y='center')  
        self.add_widget(anchor_layout)

        # Layout interno com BoxLayout para organizar os elementos
        layout = BoxLayout(orientation='vertical', padding=[20, 160, 20, 60], spacing=10)  # Aumentando o padding inferior
        anchor_layout.add_widget(layout)

        # Adicionando o logotipo
        logo = Image(source=r'C:\Users\mykia\Downloads\EducaQuiz-main (1)\EducaQuiz-main\educquiz-removebg-preview.png', size_hint=(1, 0.8))
        layout.add_widget(logo)
        
        # Texto de boas-vindas
        layout.add_widget(Label(text='Bem-vindo ao Quiz! Pronto para testar seus conhecimentos?', font_size='24sp', color=(0.5, 0.5, 0.5, 1)))

        # Botão para começar o quiz 
        start_btn = Button(text='Começar o Quiz', size_hint=(None, None), width=200, height=40, pos_hint={'center_x': 0.5})
        layout.add_widget(start_btn)
        start_btn.bind(on_press=self.start_quiz)

        # Botão para acessar o simulado 
        simulado_btn = Button(text='Acessar Simulado', size_hint=(None, None), width=200, height=40, pos_hint={'center_x': 0.5})
        layout.add_widget(simulado_btn)
        simulado_btn.bind(on_press=self.access_simulado)

    def start_quiz(self, instance):
        self.manager.current = 'subject_selection'  # Redireciona para a tela de seleção de assunto

    def access_simulado(self, instance):
        self.manager.current = 'simulado'  # Redireciona para a tela do simulado
