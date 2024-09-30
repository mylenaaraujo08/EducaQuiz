from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import Clock
import time
from kivy.uix.anchorlayout import AnchorLayout

class SimulatedQuizScreen(Screen):
    def __init__(self, **kwargs):
        super(SimulatedQuizScreen, self).__init__(**kwargs)
        self.timer_event = None
        self.time_remaining = 60  # 1 minuto por questão
        self.reset_quiz()

    def reset_quiz(self):
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
            },
            {
                "question": "Questão 6 (ENEM) Qual das alternativas apresenta um exemplo de metáfora?",
                "options": ["a) Ele é como um leão", "b) Ela tem olhos de esmeralda", "c) João correu como o vento", "d) Maria é tão forte quanto uma rocha", "e) Ele é lento como uma tartaruga"],
                "answer": "b) Ela tem olhos de esmeralda"
            },
            {
                "question": "Questão 7 (FUVEST) Qual é a função da conjunção mas na frase: 'Tentei, mas não consegui'?",
                "options": ["a) Explicativa", "b) Conclusiva", "c) Adversativa", "d) Aditiva", "e) Causal"],
                "answer": "c) Adversativa"
            },
            {
                "question": "Questão 8 (UNICAMP) Qual é o sujeito da frase: 'Passaram-se anos desde o ocorrido'?",
                "options": ["a) Sujeito inexistente", "b) Sujeito indeterminado", "c) Sujeito composto", "d) Sujeito simples", "e) Sujeito oculto"],
                "answer": "a) Sujeito inexistente"
            },
            {
                "question": "Questão 9 (UFPE) Qual é o tempo verbal da frase: 'Se ele tivesse estudado, teria passado no exame'?",
                "options": ["a) Futuro do presente", "b) Pretérito perfeito", "c) Futuro do pretérito", "d) Pretérito mais-que-perfeito", "e) Futuro do subjuntivo"],
                "answer": "c) Futuro do pretérito"
            },
            {
                "question": "Questão 10 (UERJ) Qual é o valor de x na equação x² - 9 = 0?",
                "options": ["a) x = 1", "b) x = 3", "c) x = -3", "d) x = 0", "e) x = 9"],
                "answer": "b) x = 3"
            }
        ]
        self.current_question = 0
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
            btn = Button(text=option, size_hint=(0.9, None), height=40, pos_hint={'center_x': 0.5})  # Mais centralizado
            btn.bind(on_press=self.check_answer)
            layout.add_widget(btn)
            self.option_buttons.append(btn)

        self.next_btn = Button(text='Próximo', size_hint=(0.9, None), height=40, disabled=True, pos_hint={'center_x': 0.5})  # Botão próximo centralizado
        self.next_btn.bind(on_press=self.next_question)
        layout.add_widget(self.next_btn)

        self.time_remaining = 60  # Reiniciar temporizador para 60 segundos por questão
        self.timer_label = Label(text=f'Tempo restante: {self.time_remaining} segundos', font_size='16sp')
        layout.add_widget(self.timer_label)

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

        for btn in self.option_buttons:
            btn.disabled = True  # Desabilitar todos os botões
            if btn.text == correct_answer:
                btn.background_color = (0, 1, 0, 1)  # Verde
            elif btn.text == selected_answer:
                btn.background_color = (1, 0, 0, 1)  # Vermelho

        if selected_answer == correct_answer:
            self.score += 1

        self.next_btn.disabled = False
        if self.timer_event:
            self.timer_event.cancel() 

    def next_question(self, instance):
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.show_question()
        else:
            self.end_quiz()

    def end_quiz(self):
        if self.timer_event:
            self.timer_event.cancel()

        self.clear_widgets()
        
        anchor_layout = AnchorLayout(anchor_y='center')  
        self.add_widget(anchor_layout)
        layout = BoxLayout(orientation='vertical', padding=[20, 160, 20, 60], spacing=10)  # Aumentando o padding inferior
        anchor_layout.add_widget(layout)
    

        layout.add_widget(Label(text=f'Pontuação final: {self.score}/{len(self.questions)}', font_size='24sp'))

        if self.score >= 9:
            reward_message = "Parabéns! Você acertou mais de 90% das questões. Você ganhou uma bolsa gratuita no ProENEM!   : - )"
        elif self.score >= 7:
            reward_message = "Ótimo trabalho! Você acertou mais de 70% das questões. Você ganhou uma bolsa de 50% no ProENEM!  : - )"
        else:
            reward_message = "Infelizmente, você não atingiu pontos suficientes para obter a premiação!   : - ( "

        layout.add_widget(Label(text=reward_message, font_size='20sp'))

        # Botão de voltar com tamanho e posicionamento ajustado
        finish_btn = Button(text='Voltar ao Início', size_hint=(None, None), width=150, height=60, pos_hint={'center_x': 0.5})
        finish_btn.bind(on_press=self.go_back_to_start)
        layout.add_widget(finish_btn)

    def go_back_to_start(self, instance):
        self.manager.current = 'login'
