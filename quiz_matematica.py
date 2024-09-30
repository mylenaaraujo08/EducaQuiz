from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
import time
from kivy.uix.anchorlayout import AnchorLayout


# Tela de Seleção de Áreas
class AreaSelectionScreen(Screen):
    def __init__(self, **kwargs):
        super(AreaSelectionScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.add_widget(layout)

        layout.add_widget(Label(text="Selecione a Área", font_size='24sp'))

        btn_math = Button(text="Matemática", size_hint=(None, None), width=520, height=40, pos_hint={'center_x': 0.5})
        btn_math.bind(on_press=self.start_math_quiz)
        layout.add_widget(btn_math)

    def start_math_quiz(self, instance):
        self.manager.current = 'math_quiz'

# Tela do Quiz de Matemática
class MathQuizScreen(Screen):
    def __init__(self, **kwargs):
        super(MathQuizScreen, self).__init__(**kwargs)
        self.timer_event = None
        self.time_remaining = 30
        self.question_start_time = 0
        self.reset_quiz()

    def on_pre_enter(self, *args):
        self.reset_quiz()

    def reset_quiz(self):
        # Definindo as perguntas e respostas do quiz
        self.questions = [
            {
                "question": "Questão 1 (ENEM) Qual é o valor da expressão (3 + 5) × 2?",
                "options": ["a) 13", "b) 16", "c) 12", "d) 10", "e) 15"],
                "answer": "b) 16"
            },
            {
                "question": "Questão 2 (FUVEST) Qual é a solução da equação 2x + 3 = 9?",
                "options": ["a) x = 1", "b) x = 2", "c) x = 3", "d) x = 4", "e) x = 5"],
                "answer": "c) x = 3"
            },
            {
                "question": "Questão 3 (UNICAMP) Se um triângulo tem lados com comprimentos 3 cm, 4 cm e 5 cm, qual é o perímetro desse triângulo?",
                "options": ["a) 7 cm", "b) 10 cm", "c) 12 cm", "d) 15 cm", "e) 9 cm"],
                "answer": "c) 12 cm"
            },
            {
                "question": "Questão 4 (UERJ) Qual é o valor de x na equação x^2 - 4x + 4 = 0?",
                "options": ["a) x = 1", "b) x = -2", "c) x = 2", "d) x = 3", "e) x = 4"],
                "answer": "c) x = 2"
            },
            {
                "question": "Questão 5 (UNESP) Qual é a área de um círculo com raio de 3 cm? (use π ≈ 3,14)",
                "options": ["a) 9,42 cm²", "b) 18,84 cm²", "c) 28,26 cm²", "d) 37,68 cm²", "e) 42,10 cm²"],
                "answer": "c) 28,26 cm²"
            }
        ]

        self.current_question = 0
        self.score = 0
        self.selected_answers = []
        self.time_per_question = []
        self.show_question()

    def show_question(self):
        self.clear_widgets()

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.add_widget(layout)

        # Exibir a pergunta
        question = self.questions[self.current_question]["question"]
        options = self.questions[self.current_question]["options"]
        layout.add_widget(Label(text=question, font_size='18sp'))

        # Criar botões para as opções de resposta
        self.option_buttons = []
        for option in options:
            btn = Button(text=option, size_hint=(None, None), width=520, height=40, pos_hint={'center_x': 0.5})
            btn.bind(on_press=self.check_answer)
            layout.add_widget(btn)
            self.option_buttons.append(btn)

        # Botão "Próximo" inicialmente desabilitado
        self.next_btn = Button(text='Próximo', size_hint=(None, None), width=520, height=40, pos_hint={'center_x': 0.5}, disabled=True)
        self.next_btn.bind(on_press=self.next_question)
        layout.add_widget(self.next_btn)

        # Exibir o tempo restante
        self.timer_label = Label(text=f'Tempo restante: {self.time_remaining} segundos', font_size='16sp')
        layout.add_widget(self.timer_label)

        # Reiniciar o tempo e começar a contagem
        self.time_remaining = 30
        self.question_start_time = time.time()
        self.start_timer()

    def start_timer(self):
        # Iniciar o cronômetro para a pergunta atual
        if self.timer_event:
            self.timer_event.cancel()
        self.timer_event = Clock.schedule_interval(self.update_timer, 1)

    def update_timer(self, dt):
        # Atualizar o tempo restante
        if self.time_remaining > 0:
            self.time_remaining -= 1
            self.timer_label.text = f'Tempo restante: {self.time_remaining} segundos'
        else:
            self.next_question(None)

    def check_answer(self, instance):
        # Verificar se a resposta selecionada está correta
        selected_answer = instance.text
        correct_answer = self.questions[self.current_question]["answer"]

        if self.timer_event:
            self.timer_event.cancel()

        time_spent = time.time() - self.question_start_time
        self.time_per_question.append(time_spent)

        # Mudar a cor dos botões conforme a resposta
        for btn in self.option_buttons:
            btn.disabled = True  # Desabilitar todos os botões
            if btn.text == correct_answer:
                btn.background_color = (0, 1, 0, 1)  # Verde para a resposta correta
            elif btn.text == selected_answer:
                btn.background_color = (1, 0, 0, 1)  # Vermelho para a resposta incorreta

        # Atualizar pontuação e resposta selecionada
        if selected_answer == correct_answer:
            self.score += 1
        else:
            self.selected_answers.append({
                "question": self.questions[self.current_question]["question"],
                "selected": selected_answer,
                "correct": correct_answer
            })

        self.next_btn.disabled = False  # Habilitar o botão "Próximo"

    def next_question(self, instance):
        # Passar para a próxima pergunta ou mostrar os resultados
        if self.timer_event:
            self.timer_event.cancel()

        if len(self.time_per_question) < self.current_question + 1:
            self.time_per_question.append(30)

        self.current_question += 1
        if self.current_question < len(self.questions):
            self.show_question()
        else:
            self.show_results()

    def show_results(self):
        # Exibir os resultados finais do quiz
        self.clear_widgets()
        anchor_layout = AnchorLayout(anchor_y='center')  
        self.add_widget(anchor_layout)
        layout = BoxLayout(orientation='vertical', padding=[20, 160, 20, 60], spacing=10)  # Aumentando o padding inferior
        anchor_layout.add_widget(layout)

        layout.add_widget(Label(text=f'Pontuação final: {self.score}/{len(self.questions)}', font_size='24sp'))

        # Exibir as respostas incorretas
        if self.selected_answers:
            layout.add_widget(Label(text='Respostas incorretas:', font_size='20sp'))
            for answer in self.selected_answers:
                layout.add_widget(Label(text=answer["question"], font_size='16sp'))
                layout.add_widget(Label(text=f'Selecionada: {answer["selected"]}', color=(1, 0, 0, 1), font_size='14sp'))
                layout.add_widget(Label(text=f'Correta: {answer["correct"]}', color=(0, 1, 0, 1), font_size='14sp'))

        else:
            layout.add_widget(Label(text='Você acertou todas as perguntas!', font_size='20sp'))

        # Botão para voltar à seleção de áreas
        back_btn = Button(text='Voltar', size_hint=(None, None), width=520, padding=0, height=40, pos_hint={'center_x': 0.5})
        back_btn.bind(on_press=self.back_to_area_selection)
        layout.add_widget(back_btn)

    def back_to_area_selection(self, instance):
        self.manager.current = 'subject_selection'


# Gerenciador de Tela
class QuizApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(AreaSelectionScreen(name='subject_selection'))
        sm.add_widget(MathQuizScreen(name='math_quiz'))
        return sm

if __name__ == '__main__':
    QuizApp().run()
