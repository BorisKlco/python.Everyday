import tkinter

window = tkinter.Tk()
window.title("GUI <3")
window.minsize(width=500, height=300)

label_text = tkinter.Label(text="Hello Window!", font=("Arial", 24))
label_text.pack()

window.mainloop()
