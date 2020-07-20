# Making Icons, images, and exit buttons
# Icons have a .ico file extension (basically a png file)
# To import actual image files (png, jpg), you need to import a module called Pillow
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Meme collection')
p1 = PhotoImage(file='TrollFace.png')
root.iconphoto(False, p1)

# Another alternate way is
# root.iconbitmap('TrollFace.ico')
# this worked on vs code but not on replit


my_img1 = ImageTk.PhotoImage(Image.open("TrollFace.png"))
my_img2 = ImageTk.PhotoImage(Image.open("shrekmeme.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("you know what time it is.jpg"))

'''
#?An alrernative more straight forward way is this. But you somehow cannot open jpg files
my_img1 = PhotoImage(file='TrollFace.png')
my_img2 = PhotoImage(file='shrekmeme.jpg')
my_img3 = PhotoImage(file='you know what time it is.jpg')
'''

my_img_list = [my_img1, my_img2, my_img3]

img_label1 = Label(image=my_img1)


def forward(image_number):
    global img_label1
    global button_forward
    global button_back
    img_label1.config(image=my_img_list[image_number + 1])
    '''
    #!A little more complicated way to do the same thing
    img_label1.grid_forget()
    img_label1 = Label(image=my_img_list[image_number + 1])
    img_label1.grid(row=0, column=0, columnspan=3)
    '''
    button_forward = Button(
        root, text=">>", command=lambda: forward(image_number+1), state=NORMAL)
    if image_number + 1 == len(my_img_list) - 1:
        button_forward.config(state=DISABLED)
    button_forward.grid(row=1, column=2)
    button_back = Button(root, text="<<", command=lambda: back(
        image_number + 1), state=NORMAL)
    button_back.grid(row=1, column=0)


def back(image_number):
    global img_label1
    global button_forward
    global button_back
    #!Careful not to redefine button_back cuz it changes!!

    img_label1.grid_forget()
    img_label1 = Label(image=my_img_list[image_number - 1])
    img_label1.grid(row=0, column=0, columnspan=3)
    button_back = Button(root, text="<<", command=lambda: back(
        image_number-1), state=NORMAL)
    if image_number <= 1:
        button_back.config(state=DISABLED)
    button_back.grid(row=1, column=0)
    button_forward = Button(root, text=">>", command=lambda: forward(
        image_number - 1), state=NORMAL)
    button_forward.grid(row=1, column=2)


button_back = Button(root, text="<<", state=DISABLED)
button_forward = Button(root, text=">>", command=lambda: forward(0))
button_quit = Button(root, text="Exit Program", command=root.quit)

img_label1.grid(row=0, column=0, columnspan=3)
button_back.grid(row=1, column=0)
button_forward.grid(row=1, column=2)
button_quit.grid(row=1, column=1)
root.mainloop()
