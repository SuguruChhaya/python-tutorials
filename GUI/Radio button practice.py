'''
In this version, I added a function which prints the total of everything that had been printed
'''
from tkinter import *
from PIL import Image, ImageTk
root = Tk()
icon = ImageTk.PhotoImage(Image.open('TrollFace.png'))
root.iconphoto(False, icon)

current_topping = StringVar()
#!Make sure to set value
current_topping.set("Price of topping will change")

all_toppings = {"Pepperoni": "$1", "Cheese": "$2", "Bacon": "$3"}

total = 0


def clicked(e):
    global total
    total += int(e[1:])
    my_label = Label(root, text=e).pack()


def print_total():
    total_label = Label(root, text="Current total: $" + str(total)).pack()


for key, items in all_toppings.items():
    Radiobutton(root, text=key, variable=current_topping,
                value=items).pack(anchor=W)

button_click = Button(root, text="Click to print price!",
                      command=lambda: clicked(current_topping.get()))

button_total = Button(root, text='Calculate total', command=print_total).pack()
button_click.pack()


root.mainloop()
