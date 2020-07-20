
# *Dropdown boxes are very similar to checkboxes
#!We need to assign a variable

from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title("Let's make dropdown boxes!!")


def show(event):
    mylabel = Label(root, text=dropdown.get())
    mylabel.pack()

my_list = ['Monday', 'Tuesday',
           'Wednesday', 'Thursday', 'Friday']
dropdown = StringVar()
dropdown.set(my_list[0])

# *The optionmenu dropbox has a specific order
#!I can directly make choosing something do something by the command.
# drop = OptionMenu(root, dropdown, 'Monday', 'Tuesday',
# 'Wednesday', 'Thursday', 'Friday', command=show)

#!I can also make a list to store all the options.

#*Can use star to unpack the list
drop = OptionMenu(root, dropdown, *my_list, command=show)

drop.pack()


myButton = Button(root, text="Show selection")

root.mainloop()
