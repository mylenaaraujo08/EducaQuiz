from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
import time
from kivy.uix.anchorlayout import AnchorLayout

# Tela do Quiz de Português
class PortugueseQuizScreen(Screen):
    def __init__(self, **kwargs):
        super(PortugueseQuizScreen, self).__init__(**kwargs)
        self.timer_event = None
        self.time_remaining = 30
        self.question_start_time = 0
        self.reset_quiz()

    def on_pre_enter(self, *args):
        self.reset_quiz()

    def reset_quiz(self):
        self.questions = [
            {
                "question": "Questão 1 (ENEM) Qual das alternativas apresenta um exemplo de metáfora?",
                "options": ["a) Ele é como um leão", "b) Ela tem olhos de esmeralda", "c) João correu como o vento", "d) Maria é tão forte quanto uma rocha", "e) Ele é lento como uma tartaruga"],
                "answer": "b) Ela tem olhos de esmeralda"
            },
            {
                "question": "Questão 2 (FUVEST) Qual é a função da conjunção mas na frase: 'Tentei, mas não consegui'?",
                "options": ["a) Explicativa", "b) Conclusiva", "c) Adversativa", "d) Aditiva", "e) Causal"],
                "answer": "c) Adversativa"
            },
            {
                "question": "Questão 3 (UNICAMP) Qual é o sujeito da frase: 'Passaram-se anos desde o ocorrido'?",
                "options": ["a) Sujeito inexistente", "b) Sujeito indeterminado", "c) Sujeito composto", "d) Sujeito simples", "e) Sujeito oculto"],
                "answer": "a) Sujeito inexistente"
            },
            {
                "question": "Questão 4 (UFPE) Qual é o tempo verbal da frase: 'Se ele tivesse estudado, teria passado no exame'?",
                "options": ["a) Futuro do presente", "b) Pretérito perfeito", "c) Futuro do pretérito", "d) Pretérito mais-que-perfeito", "e) Pretérito imperfeito"],
                "answer": "c) Futuro do pretérito"
            },
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

        question = self.questions[self.current_question]["question"]
        options = self.questions[self.current_question]["options"]

        layout.add_widget(Label(text=question, font_size='18sp'))

        self.option_buttons = []
        for option in options:
            btn = Button(text=option, size_hint=(None, None), width=520, height=40, pos_hint={'center_x': 0.5})
            btn.bind(on_press=self.check_answer)
            layout.add_widget(btn)
            self.option_buttons.append(btn)

        self.next_btn = Button(text='Próximo', size_hint=(None, None), width=520, height=40, pos_hint={'center_x': 0.5}, disabled=True)
        self.next_btn.bind(on_press=self.next_question)
        layout.add_widget(self.next_btn)

        self.timer_label = Label(text=f'Tempo restante: {self.time_remaining} segundos', font_size='16sp')
        layout.add_widget(self.timer_label)

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

        # Desabilita todos os botões de opções após a seleção
        for btn in self.option_buttons:
            btn.disabled = True

        if self.timer_event:
            self.timer_event.cancel()

        time_spent = time.time() - self.question_start_time
        self.time_per_question.append(time_spent)

        # Marca a resposta correta com a cor verde e a selecionada incorreta com a cor vermelha
        for btn in self.option_buttons:
            if btn.text == correct_answer:
                btn.background_color = (0, 1, 0, 1)
            elif btn.text == selected_answer:
                btn.background_color = (1, 0, 0, 1)

        # Verifica se a resposta selecionada é correta e atualiza a pontuação
        if selected_answer == correct_answer:
            self.score += 1
        else:
            self.selected_answers.append({
                "question": self.questions[self.current_question]["question"],
                "selected": selected_answer,
                "correct": correct_answer
            })

        # Habilita o botão "Próximo" para avançar à próxima pergunta
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
        layout = BoxLayout(orientation='vertical', padding=[20, 160, 20, 60], spacing=10)  # Aumentando o padding inferior
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

        finish_btn = Button(text='Voltar ao Início', size_hint=(None, None), width=120, height=40)
        finish_btn.bind(on_press=self.go_back_to_start)
        layout.add_widget(finish_btn)

    def go_back_to_start(self, instance):
        self.manager.current = 'subject_selection'