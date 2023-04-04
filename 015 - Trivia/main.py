import html
import random
from tkinter import *

import requests

BACKGROUND_COLOR = "#B1DDC6"
CANVAS_COLOR = "#FCDDB0"
FONT_NAME = "Courier"
TRIVIA_URL = "https://opentdb.com/api.php?amount=10&type=boolean"
resp = requests.get(TRIVIA_URL, timeout=5)
data = resp.json()
QUESTIONS = data["results"]
points = 0

window = Tk()
window.title("Trivia! True or False")
window.minsize(width=600, height=600)
window.maxsize(width=600, height=600)
window.config(padx=100, pady=50, bg=BACKGROUND_COLOR)

img_correct = PhotoImage(file="images/right.png")
img_incorrect = PhotoImage(file="images/wrong.png")


def pick_question():
    """Pick random question from list, remove question from list, return it as 2 variables"""
    global QUESTIONS

    question_number = random.randint(0, len(QUESTIONS) - 1)

    question = QUESTIONS[question_number]["question"]
    answer = QUESTIONS[question_number]["correct_answer"]
    QUESTIONS.remove(QUESTIONS[question_number])

    return question, answer


def ask_question(is_true=None):
    """Check if question can be picked --> Pick random question or call winner()
    define question and answer, commands for buttons, loop over ask_question()"""
    global QUESTIONS, points
    if is_true == "1":
        points += 1
    if len(QUESTIONS) > 0:
        question, answer = pick_question()
    else:
        return winner()

    main_canvas.itemconfig(question_text, text=html.unescape(question))
    main_canvas.itemconfig(answer_text, text=answer)  # Cheater mode

    if answer == "True":
        correct.config(command=lambda: ask_question("1"))
        incorrect.config(command=ask_question)
    else:
        correct.config(command=ask_question)
        incorrect.config(command=lambda: ask_question("1"))


def winner():
    """After winner is called, canvas labels are changed to show points, remove buttons"""
    global points
    main_canvas.itemconfig(question_text, text="Points", font=(FONT_NAME, 38, "bold"))
    main_canvas.itemconfig(answer_text, text=points, font=(FONT_NAME, 32, "bold"))
    correct.grid_forget()
    incorrect.grid_forget()


main_canvas = Canvas(
    window, width=400, height=400, bg=CANVAS_COLOR, bd=0, highlightthickness=0
)

question_text = main_canvas.create_text(
    (180, 150), text="", font=(FONT_NAME, 14), width=300
)
answer_text = main_canvas.create_text((200, 300), text="", font=(FONT_NAME, 16, "bold"))
main_canvas.grid(column=0, row=0, columnspan=2)

correct = Button(window, image=img_correct, command="None")
correct.grid(column=0, row=1)
incorrect = Button(window, image=img_incorrect, command="None")
incorrect.grid(column=1, row=1)

ask_question()  # Game start

window.mainloop()
