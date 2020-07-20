from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Lets make checkboxes!!")
icon = ImageTk.PhotoImage(Image.open("conan.jpg"))
root.iconphoto(False, icon)

# *Compared to radiobuttons, checkboxes are more like on and off, not choosing between many.
# * Similar to radiobuttons, I have to set a variable to store data from the checkbox.
#!This is because when a checkbox is clicked, the value assigned is either a 0(haven't) or a 1(have checked)


def check():
    mylabel.config(text=var2.get())


# *Checkbox data doesn't need to be stored in an intvalue, it can also be stored in a stringvar
var2 = StringVar()
# *The code below creates errors
c = Checkbutton(root, text="Check this box!!", variable=var2,
                command=check, onvalue="On", offvalue="Off")
#!This fixes the bug of the checkbox being checked by defalut
c.deselect()
c.pack()

mylabel = Label(root, text=var2.get())
mylabel.pack()


mainloop()
