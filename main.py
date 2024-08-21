from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.core.window import Window

Window.size = (360, 640) 

# Tela de Login
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.add_widget(layout)

        # Adicionando o logotipo
        logo = Image(source='C:/Users/mykia/OneDrive/Documentos/Nova pasta (4)/educquiz.png', size_hint=(1, 0.8))
        layout.add_widget(logo)
        
        layout.add_widget(Label(text='Bem-vindo ao Quiz! Pronto para testar seus conhecimentos?', font_size='24sp', color=(0.5, 0.5, 0.5, 1)))
        
        start_btn = Button(text='Começar o Quiz', size_hint_y=None, height=40)
        layout.add_widget(start_btn)

        start_btn.bind(on_press=self.start_quiz)

    def start_quiz(self, instance):
        self.manager.current = 'subject_selection'

# Tela de Cadastro
class SignupScreen(Screen):
    def __init__(self, **kwargs):
        super(SignupScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.add_widget(layout)
        
        layout.add_widget(Label(text='Crie sua conta para começar', font_size='24sp', color=(0.5, 0.5, 0.5, 1)))
        
        self.username = TextInput(hint_text='Usuário', size_hint_y=None, height=40)
        self.password = TextInput(hint_text='Senha', size_hint_y=None, height=40, password=True)
        layout.add_widget(self.username)
        layout.add_widget(self.password)
        
        signup_btn = Button(text='Cadastrar', size_hint_y=None, height=40)
        login_btn = Button(text='Voltar para Login', size_hint_y=None, height=40)
        layout.add_widget(signup_btn)
        layout.add_widget(login_btn)

        signup_btn.bind(on_press=self.signup)
        login_btn.bind(on_press=self.go_to_login)

    def signup(self, instance):
        self.manager.current = 'subject_selection'

    def go_to_login(self, instance):
        self.manager.current = 'login'

# Tela de Seleção de Assuntos
class SubjectSelectionScreen(Screen):
    def __init__(self, **kwargs):
        super(SubjectSelectionScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.add_widget(layout)
        
        layout.add_widget(Label(text='Áreas de Conhecimento', font_size='24sp'))
        
        btn_ciencias_humanas = Button(text='Ciências Humanas', size_hint_y=None, height=40)
        btn_ciencias_natureza = Button(text='Ciências da Natureza', size_hint_y=None, height=40)
        btn_linguagens = Button(text='Linguagens e Códigos', size_hint_y=None, height=40)
        btn_matematica = Button(text='Matemática', size_hint_y=None, height=40)
        back_btn = Button(text='Voltar', size_hint_y=None, height=40)
        
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
        pass  # Implementar se necessário

    def go_to_login(self, instance):
        self.manager.current = 'login'

# Tela de Ciências Humanas
class CienciasHumanasScreen(Screen):
    def __init__(self, **kwargs):
        super(CienciasHumanasScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.add_widget(layout)
        
        layout.add_widget(Label(text='Ciências Humanas', font_size='24sp'))
        
        btn_historia = Button(text='História', size_hint_y=None, height=40)
        btn_geografia = Button(text='Geografia', size_hint_y=None, height=40)
        btn_filosofia = Button(text='Filosofia', size_hint_y=None, height=40)
        btn_sociologia = Button(text='Sociologia', size_hint_y=None, height=40)
        back_btn = Button(text='Voltar', size_hint_y=None, height=40)
        
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
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.add_widget(layout)
        
        layout.add_widget(Label(text='Ciências da Natureza', font_size='24sp'))
        
        btn_biologia = Button(text='Biologia', size_hint_y=None, height=40)
        btn_quimica = Button(text='Química', size_hint_y=None, height=40)
        btn_fisica = Button(text='Física', size_hint_y=None, height=40)
        back_btn = Button(text='Voltar', size_hint_y=None, height=40)
        
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
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.add_widget(layout)
        
        layout.add_widget(Label(text='Linguagens e Códigos', font_size='24sp'))
        
        btn_portugues = Button(text='Português', size_hint_y=None, height=40)
        btn_literatura = Button(text='Literatura', size_hint_y=None, height=40)
        btn_lingua_estrangeira = Button(text='Língua Estrangeira', size_hint_y=None, height=40)
        btn_artes = Button(text='Artes', size_hint_y=None, height=40)
        btn_educacao_fisica = Button(text='Educação Física', size_hint_y=None, height=40)
        btn_tecnologias = Button(text='Tecnologias da Informação e Comunicação', size_hint_y=None, height=40)
        back_btn = Button(text='Voltar', size_hint_y=None, height=40)
        
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
        pass  

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

# Tela de Quiz de Biologia
class BiologyQuizScreen(Screen):
    def __init__(self, **kwargs):
        super(BiologyQuizScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.add_widget(self.layout)
        self.questions = [
            {
    "question": "Questão 1 (UFPE) Ao dizer onde uma espécie pode ser encontrada e o que faz no lugar onde vive, estamos informando respectivamente",
    "options": ["a) Nicho ecológico e habitat.", "b) Habitat e nicho ecológico.", "c) Habitat e biótopo.", "d) Nicho ecológico e ecossistema.", "e) Habitat e ecossistema."],
    "answer": "b) Habitat e nicho ecológico."
},
{
    "question": "Questão 2 (PUC) Em uma floresta ocorrem três espécies de árvores, igualmente bem sucedidas e numerosas. Essas árvores constituem:",
    "options": ["a) Três populações.", "b) Um ecossistema.", "c) Duas comunidades.", "d) Três comunidades.", "e) Uma população."],
    "answer": "a) Três populações."
},
{
    "question": "Questão 3 (CESGRANRIO) Um ecossistema tanto terrestre como aquático se define:",
    "options": ["a) exclusivamente por todas as associações de seres vivos;", "b) pelos fatores ambientais, especialmente climáticos;", "c) pela interação de todos os seres vivos;", "d) pela interação dos fatores físicos e químicos;", "e) pela interação dos fatores abióticos e bióticos."],
    "answer": "e) pela interação dos fatores abióticos e bióticos."
},
{
    "question": "Questão 4 (FATEC) Observe a cadeia alimentar abaixo: Capim → preá → lobo guará → onça Podemos dizer que:",
    "options": ["a) o preá é o consumidor primário e, portanto, representa o primeiro nível trófico.", "b) o lobo guará e a onça ocupam o terceiro e o quarto níveis tróficos, respectivamente.", "c) o lobo guará é consumidor terciário e representa o segundo nível trófico", "d) o capim é o produtor e representa o segundo nível trófico.", "e) a onça é consumidor terciário e representa o terceiro nível trófico."],
    "answer": "a) o preá é o consumidor primário e, portanto, representa o primeiro nível trófico."
},
{
    "question": "Questão 5 (UNESP) O fato de, em algumas flores, o gineceu e o androceu amadurecerem ao mesmo tempo:",
    "options": ["a) Garante floração mais prolongada da espécie;", "b) Propicia maior produtividade de frutos;", "c) Favorece a autofecundação;", "d) Reduz as chances de autofecundação;", "e) Impede a autofecundação."],
    "answer": "c) Favorece a autofecundação."
}

        ]
        self.current_question = 0
        self.score = 0

    def on_enter(self, *args):
        self.reset_quiz()

    def reset_quiz(self):
        self.current_question = 0
        self.score = 0
        self.show_question()

    def show_question(self):
        self.layout.clear_widgets()

        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            question_text = question_data["question"]
            options = question_data["options"]

            self.layout.add_widget(Label(text=question_text, font_size='18sp'))

            for option in options:
                btn = Button(text=option, size_hint_y=None, height=40)
                btn.bind(on_press=self.check_answer)
                self.layout.add_widget(btn)
        else:
            self.show_score()

    def check_answer(self, instance):
        selected_option = instance.text
        correct_answer = self.questions[self.current_question]["answer"]

        if selected_option == correct_answer:
            instance.background_color = (0, 1, 0, 1) 
            self.score += 1
        else:
            instance.background_color = (1, 0, 0, 1) 

        # Desativar todos os botões de resposta após selecionar uma opção
        for child in self.layout.children:
            if isinstance(child, Button):
                child.disabled = True

        # Avançar para a próxima questão
        self.current_question += 1
        self.layout.add_widget(Button(text='Próxima', size_hint_y=None, height=40, on_press=lambda x: self.show_question()))

    def show_score(self):
        self.layout.clear_widgets()
        self.layout.add_widget(Label(text=f'Pontuação final: {self.score}', font_size='24sp'))
        back_btn = Button(text='Voltar à Seleção de Assunto', size_hint_y=None, height=40)
        self.layout.add_widget(back_btn)
        back_btn.bind(on_press=self.go_to_subject_selection)

    def go_to_subject_selection(self, instance):
        self.manager.current = 'subject_selection'

# Gerenciador de Telas
class QuizApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(SignupScreen(name='signup'))
        sm.add_widget(SubjectSelectionScreen(name='subject_selection'))
        sm.add_widget(CienciasHumanasScreen(name='ciencias_humanas'))
        sm.add_widget(NatureSciencesScreen(name='nature_sciences'))
        sm.add_widget(LinguagensCodigosScreen(name='linguagens_codigos'))
        sm.add_widget(BiologyQuizScreen(name='biology_quiz'))
        return sm

if __name__ == '__main__':
    QuizApp().run()
