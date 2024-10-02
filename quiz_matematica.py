from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
import time
from kivy.uix.anchorlayout import AnchorLayout

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
        self.questions = [
            {
                "question": "Questão 1: Qual é a soma de 25 e 37?",
                "options": ["a) 52", "b) 62", "c) 72", "d) 80", "e) 90"],
                "answer": "b) 62"
            },
            {
                "question": "Questão 2: O que é 7²?",
                "options": ["a) 14", "b) 49", "c) 56", "d) 63", "e) 72"],
                "answer": "b) 49"
            },
            {
                "question": "Questão 3: Qual é a raiz quadrada de 144?",
                "options": ["a) 10", "b) 12", "c) 14", "d) 16", "e) 18"],
                "answer": "b) 12"
            },
            {
                "question": "Questão 4: Se um triângulo tem lados de 3, 4 e 5, que tipo de triângulo é?",
                "options": ["a) Equilátero", "b) Isósceles", "c) Retângulo", "d) Escaleno", "e) Não é um triângulo"],
                "answer": "c) Retângulo"
            },
            {
                "question": "Questão 5: Qual é a área de um círculo com raio 7?",
                "options": ["a) 14π", "b) 28π", "c) 49π", "d) 56π", "e) 78π"],
                "answer": "c) 49π"
            },
        ]

        self.current_question = 0
        self.selected_answers = []
        self.time_per_question = []
        self.score = 0
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
            btn = Button(text=option, size_hint=(None, None), width=560, height=40, pos_hint={'center_x': 0.5})
            btn.bind(on_press=self.check_answer)
            layout.add_widget(btn)
            self.option_buttons.append(btn)

        self.next_btn = Button(text='Próximo', size_hint=(None, None), width=220, height=40, pos_hint={'center_x': 0.5}, disabled=True)
        self.next_btn.bind(on_press=self.next_question)
        layout.add_widget(self.next_btn)

        self.timer_label = Label(text=f'Tempo restante: {self.time_remaining} segundos', font_size='16sp')
        layout.add_widget(self.timer_label)

        # Iniciar o temporizador de 30 segundos
        self.time_remaining = 30
        self.question_start_time = time.time() 
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

        time_spent = time.time() - self.question_start_time
        self.time_per_question.append(time_spent)

        for btn in self.option_buttons:
            if btn.text == correct_answer:
                btn.background_color = (0, 1, 0, 1)  # Verde
            elif btn.text == selected_answer:
                btn.background_color = (1, 0, 0, 1)  # Vermelho
        
        # Desabilitar os botões de resposta após a seleção
        for btn in self.option_buttons:
            btn.disabled = True

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

        if len(self.time_per_question) < self.current_question + 1:
            self.time_per_question.append(30)

        self.current_question += 1
        if self.current_question < len(self.questions):
            self.show_question()
        else:
            self.show_results()

    def show_results(self):
        self.clear_widgets()
        anchor_layout = AnchorLayout(anchor_y='center')  
        self.add_widget(anchor_layout)
        layout = BoxLayout(orientation='vertical', padding=[20, 160, 20, 60], spacing=35)  
        anchor_layout.add_widget(layout)

        layout.add_widget(Label(text=f'Pontuação final: {self.score}/{len(self.questions)}', font_size='24sp'))

        if self.selected_answers:
            layout.add_widget(Label(text='Respostas incorretas:', font_size='20sp'))
            for answer in self.selected_answers:
                layout.add_widget(Label(text=answer["question"], font_size='16sp'))
                layout.add_widget(Label(text=f'Selecionada: {answer["selected"]}', color=(1, 0, 0, 1), font_size='14sp'))
                layout.add_widget(Label(text=f'Correta: {answer["correct"]}', color=(0, 1, 0, 1), font_size='14sp'))

        for i, q in enumerate(self.questions):
            if i >= len(self.time_per_question) or self.time_per_question[i] >= 30:
                layout.add_widget(Label(text=f'Pergunta não respondida: {q["question"]}', font_size='16sp'))
                layout.add_widget(Label(text=f'Correta: {q["answer"]}', color=(0, 1, 0, 1), font_size='14sp'))

        total_time = sum(self.time_per_question)
        avg_time_per_question = total_time / len(self.questions)

        layout.add_widget(Label(text=f'Tempo total gasto: {total_time:.2f} segundos', font_size='20sp'))
        layout.add_widget(Label(text=f'Tempo médio por pergunta: {avg_time_per_question:.2f} segundos', font_size='20sp'))

        finish_btn = Button(text='Voltar ao Início', size_hint=(None, None), width=120, height=40, pos_hint={'center_x': 0.5})
        finish_btn.bind(on_press=self.go_back_to_start)
        layout.add_widget(finish_btn)

    def go_back_to_start(self, instance):
        self.manager.current = 'subject_selection'


class QuizApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MathQuizScreen(name='math_quiz'))
        return sm

if __name__ == '__main__':
    QuizApp().run()
