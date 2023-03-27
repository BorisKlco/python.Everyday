import random
import string
from tkinter import *
from tkinter import messagebox


def adding():
    """Adding acc to file"""

    if mail_input.get() == "" or psw_input.get() == "":
        return messagebox.showwarning(title="Warning", message="Mail/Psw is empty!")

    if_ok = messagebox.askokcancel(
        title="Is this correct?",
        message=f"{site_input.get()} | {mail_input.get()} | {psw_input.get()}",
    )

    if if_ok:
        with open("psw.txt", "a", encoding="utf8") as pass_file:
            pass_file.write(
                f"{site_input.get()} | {mail_input.get()} | {psw_input.get()} \n"
            )

    site_input.delete(0, END)
    psw_input.delete(0, END)


def gen_psw():
    """Generating password"""
    ran_psw = "".join(
        [
            random.choice(string.ascii_letters + string.digits + string.punctuation)
            for n in range(16)
        ]
    )
    psw_input.delete(0, END)
    psw_input.insert(0, ran_psw)


window = Tk()
window.title("Psw Manager")
window.config(padx=20, pady=20)
canvas = Canvas(window, height=200, width=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, anchor="center", image=image)
canvas.grid(column=1, row=0)

site_label = Label(text="Website:")
site_label.focus()
site_label.grid(column=0, row=1)
site_input = Entry(width=35)
site_input.grid(column=1, row=1, columnspan=2)

mail_label = Label(text="eMail/nick:")
mail_label.grid(column=0, row=2)
mail_input = Entry(width=35)
mail_input.insert(0, "default@mail")
mail_input.grid(column=1, row=2, columnspan=2)

psw_label = Label(text="Password:")
psw_label.grid(column=0, row=3)
psw_input = Entry(width=23)
psw_input.grid(column=1, row=3, columnspan=1)
pas_gen = Button(text="Generate", command=gen_psw)
pas_gen.grid(column=2, row=3)

add_buttom = Button(text="Add", width=34, command=adding)
add_buttom.grid(column=1, row=4, columnspan=2)
gen_psw()

window.mainloop()
