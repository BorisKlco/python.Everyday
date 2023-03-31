from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"

window = Tk()
window.title("FR/EN cards")
window.minsize(width=800, height=640)
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
check_right = PhotoImage(file="images/right.png")
check_wrong = PhotoImage(file="images/wrong.png")


def start():
    button_start.grid_forget()
    button_wrong.grid(column=0, row=1)
    button_right.grid(column=1, row=1)
    game_logic()


def game_logic():
    pass


def question(answer):
    pass


main_canvas = Canvas(
    window, width=800, height=526, bg=BACKGROUND_COLOR, bd=0, highlightthickness=0
)
main_canvas.create_image((400, 263), image=card_front)
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
    command=lambda: question("right"),
)
# button_wrong.grid(column=0, row=1)
# button_right.grid(column=1, row=1)

window.mainloop()
