# I am going to review the steps I took to make the image viewer
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Meme Collection')
icon = PhotoImage(file='TrollFace.png')
root.iconphoto(False, icon)
#!root.geometry can change the size of tkinter webpage
root.geometry = '160x190'
my_img1 = ImageTk.PhotoImage(Image.open('you know what time it is.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('TrollFace.png'))
my_img3 = ImageTk.PhotoImage(Image.open('shrekmeme.jpg'))

my_img_list = [my_img1, my_img2, my_img3]

# status
status = Label(root, text="Image 1 of " + str(len(my_img_list)),
               bd=1, relief=SUNKEN, anchor=E)

image_label = Label(image=my_img1)


def forward(image_number):
    #!The config makes the "global" statements unnecessary
    image_label.config(image=my_img_list[image_number + 1])
    button_next.config(command=lambda: forward(image_number + 1))
    if image_number + 1 == len(my_img_list) - 1:
        button_next.config(state=DISABLED)
    button_back.config(state=NORMAL, command=lambda: back(image_number + 1))
    status.config(text="Image " + str(image_number + 2) +
                  " of " + str(len(my_img_list)))


def back(image_number):
    image_label.config(image=my_img_list[image_number - 1])
    button_back.config(command=lambda: back(image_number - 1))
    if image_number == 1:
        button_back.config(state=DISABLED)
    button_next.config(state=NORMAL, command=lambda: forward(image_number - 1))
    status.config(text="Image " + str(image_number) +
                  " of " + str(len(my_img_list)))


button_next = Button(root, text=">>", command=lambda: forward(0))
button_back = Button(root, text="<<", state=DISABLED)
button_exit = Button(root, text="Click to exit", command=root.quit)

image_label.grid(row=0, column=0, columnspan=3)
button_next.grid(row=1, column=2)
button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()
