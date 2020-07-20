# ?Radio buttons are those google form buttons where you choose between some stuff
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
icon = ImageTk.PhotoImage(Image.open('conan.jpg'))
root.iconphoto(False, icon)

#!Tkinter variables are a little different, we specify the type
#!If the variable was a string, we call StringVar

choose = IntVar()
choose.set(1)


def clicked(number):
    # ? For somereason, the following code replaces the original value while the actual one creates a new label?
    # ? mylabel.config(text=number)
    mylabel = Label(root, text=number).pack()

#!The new widget, "Radio button" needs a variable to store the info that it was chosen

Radiobutton(root, text="Option1", variable=choose, value=1,
            command=lambda: clicked(choose.get())).pack()
Radiobutton(root, text="Option2", variable=choose, value=2,
            command=lambda: clicked(choose.get())).pack()

mylabel = Label(root, text=choose.get())
mylabel.pack()

myButton = Button(root, text="Click to print value",
                  command=lambda: clicked(choose.get())).pack()

mainloop()
