import random
from tkinter import *

import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"
words_list = []
random_choice = None

window = Tk()
window.title("FR/EN cards")
window.minsize(width=800, height=640)
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
check_right = PhotoImage(file="images/right.png")
check_wrong = PhotoImage(file="images/wrong.png")


def start():
    """words logic init, remove start button, add question buttons"""
    button_start.grid_forget()
    button_wrong.grid(column=0, row=1)
    button_right.grid(column=1, row=1)
    words_logic()


def words_logic():
    """Pick 10 random words from csv, create tuples list, init game logic"""
    global words_list
    data = pandas.read_csv("data/french_words.csv")
    random_data = data.sample(n=10)
    words_list = [
        (word["French"], word["English"]) for (index, word) in random_data.iterrows()
    ]
    game_logic()


def game_logic():
    """control len() of words list else call reset,
    pick random tuple from list,
    update canvas, give option to buttons
    """
    global words_list, random_choice
    if len(words_list) > 0:
        random_choice = french, english = words_list[
            random.randint(0, len(words_list) - 1)
        ]
        main_canvas.itemconfigure(question_text, text=french)
        main_canvas.itemconfigure(answer_text, text="You know this one?")
        window.after(
            3000,
            lambda: (
                main_canvas.itemconfigure(answer_text, text=english),
                main_canvas.itemconfigure(flip_card, image=card_back),
                button_right.config(command=lambda: question("right")),
                button_wrong.config(command=lambda: question("wrong")),
            ),
        )
    else:
        main_canvas.itemconfigure(question_text, text="You know all! Wanna go again?")
        main_canvas.itemconfigure(answer_text, text="")
        main_canvas.itemconfigure(flip_card, image=card_front)
        button_wrong.grid_forget()
        button_right.grid_forget()
        button_start.grid(column=0, row=1, columnspan=2)


def question(answer):
    """remove tuple from words list,
    reset canvas and button options
    call game logic"""
    if answer == "right":
        words_list.remove(random_choice)
        main_canvas.itemconfigure(flip_card, image=card_front)
        button_right.config(command="None")
        button_wrong.config(command="None")
        game_logic()
    else:
        main_canvas.itemconfigure(flip_card, image=card_front)
        button_right.config(command="None")
        button_wrong.config(command="None")
        game_logic()


main_canvas = Canvas(
    window, width=800, height=526, bg=BACKGROUND_COLOR, bd=0, highlightthickness=0
)
flip_card = main_canvas.create_image((400, 263), image=card_front)
question_text = main_canvas.create_text(
    (400, 120), text="Flash card game!", font=(FONT_NAME, 16, "bold")
)
answer_text = main_canvas.create_text(
    (400, 220), text="For start click green checkmark!", font=(FONT_NAME, 14)
)
main_canvas.grid(column=0, row=0, sticky=EW, columnspan=2)

button_start = Button(
    window,
    text="Start!",
    bd=0,
    border=0,
    borderwidth=0,
    highlightthickness=0,
    image=check_right,
    command=start,
)
button_start.grid(column=0, row=1, columnspan=2)


button_wrong = Button(
    window,
    text="Wrong",
    bd=0,
    border=0,
    borderwidth=0,
    highlightthickness=0,
    image=check_wrong,
    command=lambda: question("wrong"),
)
button_right = Button(
    window,
    text="Right",
    bd=0,
    border=0,
    borderwidth=0,
    highlightthickness=0,
    image=check_right,
)

window.mainloop()
