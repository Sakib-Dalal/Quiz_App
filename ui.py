import tkinter

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tkinter.Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=('Arial', 20, 'italic'))
        self.score_label.config(padx=20, pady=20)
        self.score_label.grid(row=0, column=1)

        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Some Question Text", fill=THEME_COLOR,
                                                     font=("Ariel", 20, "italic"), width=280)

        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=50)

        self.true_button_image = tkinter.PhotoImage(file="./images/true.png")
        self.true_button = tkinter.Button(image=self.true_button_image, highlightbackground=THEME_COLOR,
                                          command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        self.false_button_image = tkinter.PhotoImage(file="./images/false.png")
        self.false_button = tkinter.Button(image=self.false_button_image, highlightbackground=THEME_COLOR,
                                           command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.true_button.destroy()
            self.false_button.destroy()
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(
            1000, self.get_next_question)
