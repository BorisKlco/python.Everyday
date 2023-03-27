from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
RED = "#E97777"
PINK = "#FF9F9F"
ORANGE = "#FCDDB0"
YELLOW = "#FFFAD7"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 10
SEC = 60
reps = 0
timer = None
finished = []


def reset():
    """TIMER RESET"""
    global reps, finished
    window.after_cancel(timer)
    reps = 0
    finished = []
    check["text"] = finished
    name["text"] = "Timer"
    canvas.itemconfig(count_text, text="00:00")


def start_cd():
    """TIMER MECHANISM"""
    global reps

    reps += 1

    if reps % 8 == 0:
        countdown(LONG_BREAK_MIN * SEC)
        name["text"] = "BREAK!"
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN * SEC)
        name["text"] = "break"
    else:
        countdown(WORK_MIN * SEC)
        name["text"] = "WORK!"


def countdown(count):
    """COUNTDOWN MECHANISM"""
    global timer
    m, s = divmod(count, 60)
    canvas.itemconfig(count_text, text=f"{m:02d}:{s:02d}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        if name["text"] == "WORK!":
            finished.append("✔️")
            check["text"] = finished
        start_cd()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

name = Label(text="Timer", fg=RED, bg=YELLOW, font=(FONT_NAME, 35))
name.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
count_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

start = Button(text="Start", command=start_cd)
start.grid(column=0, row=2)
reset_timer = Button(text="Reset", command=reset)
reset_timer.grid(column=2, row=2)

check = Label(text="", fg=PINK, bg=YELLOW)
check.grid(column=1, row=3)

window.mainloop()
