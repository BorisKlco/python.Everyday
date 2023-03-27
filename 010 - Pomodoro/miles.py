from tkinter import *

window = Tk()
window.title("km/miles calculator")
window.minsize(width=400, height=200)
window.config(padx=50, pady=50)


def convert():
    user_input = km_input.get()
    try:
        miles_convert["text"] = round(float(user_input) * 0.62, 1)
    except ValueError:
        miles_convert["text"] = "Not a number"


km_text = Label(text="km", font=("Arial", 12))
km_text.grid(column=2, row=0)

km_input = Entry()
km_input.grid(column=1, row=0)

miles_text = Label(text="is equal to", font=("Arial", 12))
miles_text.grid(column=0, row=1)

miles_convert = Label(text="", font=("Arial", 12))
miles_convert.grid(column=1, row=1)

miles_km = Label(text=" miles", font=("Arial", 12))
miles_km.grid(column=2, row=1)

convert_button = Button(text="Convert", command=convert)
convert_button.grid(column=1, row=2)


window.mainloop()
