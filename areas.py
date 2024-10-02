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


# Tela de Ciências Humanas
class CienciasHumanasScreen(Screen):
    def __init__(self, **kwargs):
        super(CienciasHumanasScreen, self).__init__(**kwargs)
        
        anchor_layout = AnchorLayout(anchor_y='center')  
        self.add_widget(anchor_layout)
        
        layout = BoxLayout(orientation='vertical', padding=[20, 160, 20, 60], spacing=10)  # Aumentando o padding inferior
        anchor_layout.add_widget(layout)
        
        layout.add_widget(Label(text='Ciências Humanas', font_size='24sp'))
        
        btn_historia = Button(text='História', size_hint=(None, None), width=520, height=40, pos_hint={'center_x': 0.5})
        btn_geografia = Button(text='Geografia', size_hint=(None, None), width=520, height=40, pos_hint={'center_x': 0.5})
        btn_filosofia = Button(text='Filosofia', size_hint=(None, None), width=520 ,height=40, pos_hint={'center_x': 0.5})
        btn_sociologia = Button(text='Sociologia', size_hint=(None, None), width=520 ,height=40, pos_hint={'center_x': 0.5})
        back_btn = Button(text='Voltar', size_hint=(None, None), height=40, width=220, pos_hint={'center_x': 0.5})
        
        layout.add_widget(btn_historia)
        layout.add_widget(btn_geografia)
        layout.add_widget(btn_filosofia)
        layout.add_widget(btn_sociologia)
        layout.add_widget(back_btn)
        
        btn_historia.bind(on_press=self.go_to_historia)
        btn_geografia.bind(on_press=self.go_to_geografia)
        btn_filosofia.bind(on_press=self.go_to_filosofia)
        btn_sociologia.bind(on_press=self.go_to_sociologia)
        back_btn.bind(on_press=self.go_to_subject_selection)

    def go_to_historia(self, instance):
        self.manager.current = 'history_quiz'

    def go_to_geografia(self, instance):
        self.manager.current = 'geography_quiz'

    def go_to_filosofia(self, instance):
        self.manager.current = 'philosophy_quiz'

    def go_to_sociologia(self, instance):
        self.manager.current = 'sociology_quiz'

    def go_to_subject_selection(self, instance):
        self.manager.current = 'subject_selection'

# Tela de Ciências da Natureza
class NatureSciencesScreen(Screen):
    def __init__(self, **kwargs):
        super(NatureSciencesScreen, self).__init__(**kwargs)
        anchor_layout = AnchorLayout(anchor_y='center')  
        self.add_widget(anchor_layout)
        layout = BoxLayout(orientation='vertical', padding=[20, 160, 20, 60], spacing=10)  # Aumentando o padding inferior
        anchor_layout.add_widget(layout)
        
        layout.add_widget(Label(text='Ciências da Natureza', font_size='24sp'))
        
        btn_biologia = Button(text='Biologia', size_hint=(None, None), height=40, width=520, pos_hint={'center_x': 0.5})
        btn_quimica = Button(text='Química', size_hint=(None, None), height=40, width=520, pos_hint={'center_x': 0.5})
        btn_fisica = Button(text='Física', size_hint=(None, None), height=40, width=520, pos_hint={'center_x': 0.5})
        back_btn = Button(text='Voltar', size_hint=(None, None), height=40, width=220, pos_hint={'center_x': 0.5})
        
        layout.add_widget(btn_biologia)
        layout.add_widget(btn_quimica)
        layout.add_widget(btn_fisica)
        layout.add_widget(back_btn)
        
        btn_biologia.bind(on_press=self.go_to_biology)
        btn_quimica.bind(on_press=self.go_to_quimica)
        btn_fisica.bind(on_press=self.go_to_fisica)
        back_btn.bind(on_press=self.go_to_subject_selection)

    def go_to_biology(self, instance):
        self.manager.current = 'biology_quiz'

    def go_to_quimica(self, instance):
        pass  

    def go_to_fisica(self, instance):
        pass 

    def go_to_subject_selection(self, instance):
        self.manager.current = 'subject_selection'

# Tela de Linguagens e Códigos
class LinguagensCodigosScreen(Screen):
    def __init__(self, **kwargs):
        super(LinguagensCodigosScreen, self).__init__(**kwargs)
        anchor_layout = AnchorLayout(anchor_y='center')  
        self.add_widget(anchor_layout)
        layout = BoxLayout(orientation='vertical', padding=[20, 160, 20, 60], spacing=10)
        anchor_layout.add_widget(layout)
        
        layout.add_widget(Label(text='Linguagens e Códigos', font_size='24sp'))
        
        btn_portugues = Button(text='Português', size_hint=(None, None), height=40, width=520, pos_hint={'center_x': 0.5})
        btn_literatura = Button(text='Literatura', size_hint=(None, None), height=40, width=520, pos_hint={'center_x': 0.5})
        btn_lingua_estrangeira = Button(text='Língua Estrangeira', size_hint=(None, None), height=40, width=520, pos_hint={'center_x': 0.5})
        btn_artes = Button(text='Artes', size_hint=(None, None), height=40, width=520, pos_hint={'center_x': 0.5})
        btn_educacao_fisica = Button(text='Educação Física', size_hint=(None, None), height=40, width=520, pos_hint={'center_x': 0.5})
        btn_tecnologias = Button(text='Tecnologias da Informação e Comunicação', size_hint=(None, None), height=40, width=520, pos_hint={'center_x': 0.5})
        back_btn = Button(text='Voltar',size_hint=(None, None), height=40, width=220, pos_hint={'center_x': 0.5})
        
        layout.add_widget(btn_portugues)
        layout.add_widget(btn_literatura)
        layout.add_widget(btn_lingua_estrangeira)
        layout.add_widget(btn_artes)
        layout.add_widget(btn_educacao_fisica)
        layout.add_widget(btn_tecnologias)
        layout.add_widget(back_btn)
        
        btn_portugues.bind(on_press=self.go_to_portugues)
        btn_literatura.bind(on_press=self.go_to_literatura)
        btn_lingua_estrangeira.bind(on_press=self.go_to_lingua_estrangeira)
        btn_artes.bind(on_press=self.go_to_artes)
        btn_educacao_fisica.bind(on_press=self.go_to_educacao_fisica)
        btn_tecnologias.bind(on_press=self.go_to_tecnologias)
        back_btn.bind(on_press=self.go_to_subject_selection)

    def go_to_portugues(self, instance):
       self.manager.current = 'portuguese_quiz'


    def go_to_literatura(self, instance):
        pass  

    def go_to_lingua_estrangeira(self, instance):
        pass  

    def go_to_artes(self, instance):
        pass  

    def go_to_educacao_fisica(self, instance):
        pass  

    def go_to_tecnologias(self, instance):
        pass  

    def go_to_subject_selection(self, instance):
        self.manager.current = 'subject_selection'
