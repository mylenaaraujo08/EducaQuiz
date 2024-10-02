from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.clock import Clock
from areas import *
from quiz_biologia import *
from quiz_historia import *
from quiz_portugues import *
from quiz_matematica import *
from simulado import *
from login import *
from subareas import *
import time

Window.size = (1220, 940)

# Carrega o arquivo .kv
Builder.load_file('Background.kv')

# Gerenciamento de telas
class QuizApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(SubjectSelectionScreen(name='subject_selection'))
        sm.add_widget(CienciasHumanasScreen(name='ciencias_humanas'))
        sm.add_widget(LinguagensCodigosScreen(name= 'linguagens_codigos'))
        sm.add_widget(MathQuizScreen(name= 'matematica')) 
        sm.add_widget(NatureSciencesScreen(name='nature_sciences'))
        sm.add_widget(BiologyQuizScreen(name='biology_quiz'))
        sm.add_widget(HistoryQuizScreen(name='history_quiz')) 
        sm.add_widget(PortugueseQuizScreen(name='portuguese_quiz')) 
        sm.add_widget(SimulatedQuizScreen(name='simulado')) 
        return sm

if __name__ == '__main__':
    QuizApp().run()
