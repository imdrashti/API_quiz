from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125,
                                width=280,
                                text="Hey how are you",
                                font=("Arial", 20, "italic"),
                                fill=THEME_COLOR
                )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.check_button = PhotoImage(file="true.png")
        self.ture_button = Button(image=self.check_button, highlightthickness=0)
        self.ture_button.grid(row=2, column=0)

        self.cross_button = PhotoImage(file="false.png")
        self.false_button = Button(image=self.cross_button, highlightthickness=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_ques()

        self.window.mainloop()

    def get_next_ques(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfigure(self.question_text, text=q_text)

