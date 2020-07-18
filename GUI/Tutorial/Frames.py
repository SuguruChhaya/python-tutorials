from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Using Frames")
icon = ImageTk.PhotoImage(Image.open('conan.jpg'))
root.iconphoto(False, icon)

#!Careful what happens when frame padding is bigger than button padding and vice versa
frame = LabelFrame(root, text="This is my frame", padx=50, pady=50)
#!Don't need text for frame

button_1 = Button(frame, text="Don't click here")
button_2 = Button(root, text="haha")
button_1.grid(row=0, column=0)
button_2.grid(row=0, column=1)
#!When we didn't use frames, we could only do pack and pack or grid and grid
#!But when we use frames, we can pack inside a grid or grid inside a packed frame
frame.grid(padx=10, pady=10)
root.mainloop()
