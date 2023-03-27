from tkinter import *

window = Tk()
window.title("Psw Manager")
window.config(padx=20, pady=20)
canvas = Canvas(window, height=200, width=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, anchor="center", image=image)
canvas.grid(column=1, row=0)

site_label = Label(text="Website:")
site_label.grid(column=0, row=1)
site_input = Entry(width=35)
site_input.grid(column=1, row=1, columnspan=2)

mail_label = Label(text="eMail/nick:")
mail_label.grid(column=0, row=2)
mail_input = Entry(width=35)
mail_input.grid(column=1, row=2, columnspan=2)

psw_label = Label(text="Password:")
psw_label.grid(column=0, row=3)
psw_input = Entry(width=23)
psw_input.grid(column=1, row=3, columnspan=1)
pas_gen = Button(text="Generate")
pas_gen.grid(column=2, row=3)

add_buttom = Button(text="Add", width=34)
add_buttom.grid(column=1, row=4, columnspan=2)

window.mainloop()
