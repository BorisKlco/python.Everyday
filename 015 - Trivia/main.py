import json
from tkinter import *

import requests

BACKGROUND_COLOR = "#B1DDC6"
CANVAS_COLOR = "#FCDDB0"
FONT_NAME = "Courier"
TRIVIA_URL = "https://opentdb.com/api.php?amount=10&type=boolean"

window = Tk()
window.title("Trivia! True or False")
window.minsize(width=600, height=600)
window.config(padx=100, pady=50, bg=BACKGROUND_COLOR)

resp = requests.get(TRIVIA_URL, timeout=5)
data = resp.json()

print(data["results"][0])


def ask_question():
    main_canvas.itemconfig(question_text, text=data["results"][0]["question"])


main_canvas = Canvas(
    window, width=400, height=400, bg=CANVAS_COLOR, bd=0, highlightthickness=0
)

question_text = main_canvas.create_text(
    (180, 150), text="", font=(FONT_NAME, 16, "bold"), width=300
)
main_canvas.grid(column=0, row=0, columnspan=2)

ask_question()

window.mainloop()
