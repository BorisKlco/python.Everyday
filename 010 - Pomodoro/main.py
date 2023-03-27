import random
import tkinter

window = tkinter.Tk()
window.title("GUI <3")
window.minsize(width=500, height=300)

label_text = tkinter.Label(text="Hello Window!", font=("Arial", 24))
label_text.grid(column=0, row=0)


def click_me():
    label_text["text"] = user_input.get()


def click_random():
    label_text["text"] = random.randint(1, 100)


click_button = tkinter.Button(text="Click me!", command=click_me)
click_button.grid(column=1, row=1)

random_button = tkinter.Button(text="Random int", command=click_random)
random_button.grid(column=2, row=0)

user_input = tkinter.Entry()
user_input.grid(column=3, row=2)

window.mainloop()
