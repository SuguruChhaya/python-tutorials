from tkinter import *
from PIL import Image, ImageTk
#!Import messagebox
from tkinter import messagebox

root = Tk()
root.title("Message box")
icon = ImageTk.PhotoImage(Image.open("conan.jpg"))
root.iconphoto(False, icon)

#!Message box means popups


def popup():
    #!Show info isn't user interactive
    # ?Has an "I" thing because it is an info popup
    #!Different types are showwarning, showerror, askquestion, askokcancel, askyesno
    response = messagebox.askyesno("This is my popup", "r u suguru?")
    # *To do stuff based on the response, i can save the thing as a variable
    # *The response variable is either 0 for no or 1 for yes
    if response == YES:
        Label(root, text=response).pack()
        messagebox.showinfo("Welcome!!", "Welcome!!")

    elif response == NO:
        Label(root, text=response).pack()
        messagebox.showinfo("Get out of here!!", "Get out of here!!")


def popup2():
    response = messagebox.askokcancel(
        "Ok or cancel", "Do u want to install virus?")
    # *1 is ok and 0 is cancel
    if response == 1:
        messagebox.showinfo("Yay!!", "Virus installed!!")
    else:
        messagebox.showinfo("Bruh", "Bruh")


def popup3():
    response = messagebox.askquestion("Question", "Question")
    messagebox.showinfo("Yay", response)
    if response == "yes":
        
        Label(root, text="YES!!").pack()


Button(root, text="Popup", command=popup3).pack()


mainloop()
