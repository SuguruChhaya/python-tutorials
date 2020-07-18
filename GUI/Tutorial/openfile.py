from tkinter import *
from PIL import Image, ImageTk
# *To open a local file on the computer, I have import filedialog
from tkinter import filedialog

root = Tk()
root.title("Image Viewer")

#?Issues opening a file after another but doesn't matter
def open_file():
    global mylabel
    global mylabel_image
    global myimage
    global filename
    filename = None
    filename = filedialog.askopenfilename(
        initialdir="C:/Users/sugur.LAPTOP-3N7FMET3.000/Pictures", title="Select a file:", filetypes=(("garbage png files", "*.png"), ("all the stupid files", "*.*")))
    #!This code itself doesn't open the file.
    mylabel = Label(root, text=filename).pack()
    myimage = ImageTk.PhotoImage(Image.open(filename))
    mylabel_image = Label(root, image=myimage).pack()



my_button = Button(root, text="Open file", command=open_file).pack()

mainloop()
