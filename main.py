from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import Clock
import time


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

# Tela do Quiz de Biologia
class BiologyQuizScreen(Screen):
    def __init__(self, **kwargs):
        super(BiologyQuizScreen, self).__init__(**kwargs)
        self.timer_event = None
        self.time_remaining = 30
        self.time_per_question = []  # Para armazenar o tempo gasto em cada pergunta
        self.question_start_time = 0  # Momento de início de cada pergunta
        self.reset_quiz()

    def on_pre_enter(self, *args):
        self.reset_quiz()

    def reset_quiz(self):
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
        self.selected_answers = []
        self.score = 0
        self.time_per_question = []  # Reiniciar o tempo gasto por pergunta
        self.show_question()

    def show_question(self):
        self.clear_widgets()
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.add_widget(layout)

        question = self.questions[self.current_question]["question"]
        options = self.questions[self.current_question]["options"]

        layout.add_widget(Label(text=question, font_size='18sp'))

        self.option_buttons = []
        for option in options:
            btn = Button(text=option, size_hint_y=None, height=40)
            btn.bind(on_press=self.check_answer)
            layout.add_widget(btn)
            self.option_buttons.append(btn)

        self.next_btn = Button(text='Próximo', size_hint_y=None, height=40, disabled=True)
        self.next_btn.bind(on_press=self.next_question)
        layout.add_widget(self.next_btn)

        self.timer_label = Label(text=f'Tempo restante: {self.time_remaining} segundos', font_size='16sp')
        layout.add_widget(self.timer_label)

        # Iniciar o temporizador de 30 segundos e registrar o início da pergunta
        self.time_remaining = 30
        self.question_start_time = time.time()  # Guardar o tempo de início
        self.start_timer()

    def start_timer(self):
        if self.timer_event:
            self.timer_event.cancel()

        self.timer_event = Clock.schedule_interval(self.update_timer, 1)

    def update_timer(self, dt):
        if self.time_remaining > 0:
            self.time_remaining -= 1
            self.timer_label.text = f'Tempo restante: {self.time_remaining} segundos'
        else:
            self.next_question(None)

    def check_answer(self, instance):
        selected_answer = instance.text
        correct_answer = self.questions[self.current_question]["answer"]

        # Cancelar o temporizador quando o usuário responder
        if self.timer_event:
            self.timer_event.cancel()

        # Calcular o tempo gasto nesta pergunta e armazenar
        time_spent = time.time() - self.question_start_time
        self.time_per_question.append(time_spent)

        for btn in self.option_buttons:
            if btn.text == correct_answer:
                btn.background_color = (0, 1, 0, 1)  # Verde
            elif btn.text == selected_answer:
                btn.background_color = (1, 0, 0, 1)  # Vermelho

        if selected_answer == correct_answer:
            self.score += 1
        else:
            self.selected_answers.append({
                "question": self.questions[self.current_question]["question"],
                "selected": selected_answer,
                "correct": correct_answer
            })

        self.next_btn.disabled = False

    def next_question(self, instance):
        if self.timer_event:
            self.timer_event.cancel()

        # Caso o usuário não tenha respondido, calcular o tempo máximo (30s)
        if len(self.time_per_question) < self.current_question + 1:
            self.time_per_question.append(30)

        self.current_question += 1
        if self.current_question < len(self.questions):
            self.show_question()
        else:
            self.show_results()

    def show_results(self):
        self.clear_widgets()
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.add_widget(layout)

        layout.add_widget(Label(text=f'Pontuação final: {self.score}/{len(self.questions)}', font_size='24sp'))

        if self.selected_answers:
            layout.add_widget(Label(text='Respostas incorretas:', font_size='20sp'))
            for answer in self.selected_answers:
                layout.add_widget(Label(text=answer["question"], font_size='16sp'))
                layout.add_widget(Label(text=f'Selecionada: {answer["selected"]}', color=(1, 0, 0, 1), font_size='14sp'))
                layout.add_widget(Label(text=f'Correta: {answer["correct"]}', color=(0, 1, 0, 1), font_size='14sp'))

        # Estatísticas de tempo
        total_time = sum(self.time_per_question)
        avg_time_per_question = total_time / len(self.questions)

        layout.add_widget(Label(text=f'Tempo total gasto: {total_time:.2f} segundos', font_size='20sp'))
        layout.add_widget(Label(text=f'Tempo médio por pergunta: {avg_time_per_question:.2f} segundos', font_size='20sp'))

        finish_btn = Button(text='Voltar ao Início', size_hint_y=None, height=40)
        finish_btn.bind(on_press=self.go_back_to_start)
        layout.add_widget(finish_btn)

    def go_back_to_start(self, instance):
        self.manager.current = 'subject_selection'

       # Tela do Quiz de História
class HistoryQuizScreen(Screen):
    def __init__(self, **kwargs):
        super(HistoryQuizScreen, self).__init__(**kwargs)
        self.reset_quiz()

    def on_pre_enter(self, *args):
        self.reset_quiz()

    def reset_quiz(self):
        self.questions = [
            {
                "question": "Questão 1: Quem foi o primeiro presidente do Brasil?",
                "options": ["a) Getúlio Vargas", "b) Juscelino Kubitschek", "c) Marechal Deodoro da Fonseca", "d) João Goulart"],
                "answer": "c) Marechal Deodoro da Fonseca"
            },
            {
                "question": "Questão 2: Qual foi o ano da Proclamação da República no Brasil?",
                "options": ["a) 1888", "b) 1889", "c) 1891", "d) 1905"],
                "answer": "b) 1889"
            },
            {
                "question": "Questão 3: Em que ano começou a Primeira Guerra Mundial?",
                "options": ["a) 1912", "b) 1914", "c) 1918", "d) 1923"],
                "answer": "b) 1914"
            },
            {
                "question": "Questão 4: Qual tratado pôs fim à Primeira Guerra Mundial?",
                "options": ["a) Tratado de Versalhes", "b) Tratado de Tordesilhas", "c) Tratado de Paris", "d) Tratado de Roma"],
                "answer": "a) Tratado de Versalhes"
            },
            {
                "question": "Questão 5: Quem foi o líder do movimento nazista na Alemanha?",
                "options": ["a) Adolf Hitler", "b) Benito Mussolini", "c) Josef Stalin", "d) Winston Churchill"],
                "answer": "a) Adolf Hitler"
            }
        ]

        self.current_question = 0
        self.selected_answers = []
        self.score = 0
        self.answer_checked = False

        self.show_question()

    def show_question(self):
        self.clear_widgets()
        
        if self.current_question < len(self.questions):
            layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
            self.add_widget(layout)

            question = self.questions[self.current_question]["question"]
            options = self.questions[self.current_question]["options"]

            layout.add_widget(Label(text=question, font_size='18sp'))

            self.option_buttons = []
            for option in options:
                btn = Button(text=option, size_hint_y=None, height=40)
                btn.bind(on_press=self.check_answer)
                layout.add_widget(btn)
                self.option_buttons.append(btn)

            self.next_btn = Button(text='Próximo', size_hint_y=None, height=40, disabled=True)
            self.next_btn.bind(on_press=self.next_question)
            layout.add_widget(self.next_btn)
        else:
            self.show_results()

    def check_answer(self, instance):
        selected_answer = instance.text
        correct_answer = self.questions[self.current_question]["answer"]

        for btn in self.option_buttons:
            if btn.text == correct_answer:
                btn.background_color = (0, 1, 0, 1)  # verde
            elif btn.text == selected_answer:
                btn.background_color = (1, 0, 0, 1)  # vermelho

        if selected_answer == correct_answer:
            self.score += 1
        else:
            self.selected_answers.append({
                "question": self.questions[self.current_question]["question"],
                "selected": selected_answer,
                "correct": correct_answer
            })

        self.next_btn.disabled = False

    def next_question(self, instance):
        self.current_question += 1
        self.show_question()

    def show_results(self):
        self.clear_widgets()
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.add_widget(layout)

        layout.add_widget(Label(text=f'Pontuação final: {self.score}/{len(self.questions)}', font_size='24sp'))

        if self.selected_answers:
            layout.add_widget(Label(text='Respostas incorretas:', font_size='20sp'))
            for answer in self.selected_answers:
                layout.add_widget(Label(text=answer["question"], font_size='16sp'))
                layout.add_widget(Label(text=f'Selecionada: {answer["selected"]}', color=(1, 0, 0, 1), font_size='14sp'))
                layout.add_widget(Label(text=f'Correta: {answer["correct"]}', color=(0, 1, 0, 1), font_size='14sp'))

        finish_btn = Button(text='Voltar ao Início', size_hint_y=None, height=40)
        finish_btn.bind(on_press=self.go_back_to_start)
        layout.add_widget(finish_btn)

    def go_back_to_start(self, instance):
        self.manager.current = 'subject_selection'

# Atualizando o ScreenManager para incluir a tela de história
class QuizApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(SubjectSelectionScreen(name='subject_selection'))
        sm.add_widget(CienciasHumanasScreen(name='ciencias_humanas'))
        sm.add_widget(NatureSciencesScreen(name='nature_sciences'))
        sm.add_widget(BiologyQuizScreen(name='biology_quiz'))
        sm.add_widget(HistoryQuizScreen(name='history_quiz'))  # Adicionando o quiz de história
        return sm


if __name__ == '__main__':
    QuizApp().run()
