from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.title("Create a new window!!")

icon = ImageTk.PhotoImage(Image.open("conan.jpg"))
# *When creating new windows, if the first arg in iconphoto is True, the icon is used the other windows too.
root.iconphoto(False, icon)


def open_window():
    global image
    top = Toplevel()
    top.title("My second window")
    label1 = Label(top, text="Hello World!!").pack()
    #!The image doesn't load in this case.
    #!In a function with a second window, I have to declare the glbal variable.
    # *I guess all the labels and stuff which have a (top, ) part included are fine.
    image = ImageTk.PhotoImage(Image.open('conan.jpg'))
    lable2 = Label(top, image=image).pack()
    # *I am controlling when the second window opens
    #!Destroy is like grid_forget but for windows
    btn2 = Button(top, text="close window", command=top.destroy).pack()


open_button = Button(root, text="Open Second window",
                     command=open_window).pack()

# *This creates a new window which usually forgets the icon and all.
#!Interestingly, if I close the main window root, the toplevel window also closes.
# *But even if I close the top level window, the main window remains open


root.mainloop()
