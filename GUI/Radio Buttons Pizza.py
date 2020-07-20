# ?Radio buttons are those google form buttons where you choose between some stuff
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
icon = ImageTk.PhotoImage(Image.open('conan.jpg'))
root.iconphoto(False, icon)

#!Tkinter variables are a little different, we specify the type
#!If the variable was a string, we call StringVar

pizza = StringVar()
#!Somehow I have to set a non-empty value to get prevent 
#!all the checkmarks to be off
pizza.set("a")

# A list of tuples
#!In this case, we are creating a toppings list for a pizza place
modes_list = [("Pepperoni", "Pepperoni"), ("Cheese", "Cheese"),
              ("Mushroom", "Mushroom"), ("Onion", "Onion")]

for topping, mode in modes_list:
    Radiobutton(root, text=topping, variable=pizza, value=mode).pack(anchor=W)


def clicked(number):
    # ? For some reason, the following code replaces the original value while the actual one creates a new label?
    # ? mylabel.config(text=number)
    mylabel = Label(root, text=number).pack()


#!The new widget, "Radio button" needs a variable to store the info that it was chosen
# ?I commented the previous one
# ?The commented code works when there are a few options
#!The for loop works better when there are a lot of options
'''
Radiobutton(root, text="Option1", variable=choose, value=1,
            command=lambda: clicked(choose.get())).pack()
Radiobutton(root, text="Option2", variable=choose, value=2,
            command=lambda: clicked(choose.get())).pack()
'''

mylabel = Label(root, text=pizza.get())
mylabel.pack()

myButton = Button(root, text="Click to print value",
                  command=lambda: clicked(pizza.get())).pack()

mainloop()
