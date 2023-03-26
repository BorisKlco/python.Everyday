import time
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
RED = "#E97777"
PINK = "#FF9F9F"
ORANGE = "#FCDDB0"
YELLOW = "#FFFAD7"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    test = time.gmtime(time.time())
    print(test.tm_sec)


# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown():
    print("1")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

name = Label(text="Timer", fg=RED, bg=YELLOW, font=(FONT_NAME, 35))
name.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start = Button(text="Start", command=countdown)
start.grid(column=0, row=2)
reset_timer = Button(text="Reset", command=reset)
reset_timer.grid(column=2, row=2)

check = Label(text="✔️", fg=PINK, bg=YELLOW)
check.grid(column=1, row=3)


window.mainloop()
