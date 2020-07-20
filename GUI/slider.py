
# *I am learning how to make sliders to create different options.
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Let's make sliders!!")
icon = ImageTk.PhotoImage(Image.open("conan.jpg"))
root.iconphoto(False, icon)
# *To specify window size, call root.geometry
root.geometry("200x200")

# *Use scale widget
# *Use a from_ method to specify where the widget is from.
# *Default is vertical
vertical = Scale(root, from_=0, to=200)
vertical.pack()

horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()


def slider_value():
    horizontal_label.config(text="vertical length: " + str(vertical.get()))
    vertical_label.config(text="horizontal length: " + str(horizontal.get()))
    #!Can do interseting things with this value such as changing window sizes
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))


# *To get the actual label, use the .get() which was used for entries too.
get_button = Button(root, command=slider_value).pack()

horizontal_label = Label(root, text="")
horizontal_label.pack()
vertical_label = Label(root, text="")
vertical_label.pack()


# * I can make things more dynamic by resizing immediately after the slider value is changed.
root2 = Tk()

# *Need to pass. But makes things really touchy so rather use a button.


def slider_2(var):
    horizontal_label2.config(text="vertical length: " + str(vertical2.get()))
    vertical_label2.config(text="horizontal length: " + str(horizontal2.get()))
    #!Can do interseting things with this value such as changing window sizes
    root2.geometry(str(horizontal2.get()) + "x" + str(vertical2.get()))


#!make sure to make the command a lambda and pass the value
vertical2 = Scale(root2, from_=0, to=200, command=slider_2)
vertical2.pack()

horizontal2 = Scale(root2, from_=0, to=200,
                    orient=HORIZONTAL, command=slider_2)
horizontal2.pack()

horizontal_label2 = Label(root2, text="")
horizontal_label2.pack()
vertical_label2 = Label(root2, text="")
vertical_label2.pack()

root2.mainloop()
