# Two types:
# 1. Updates every time I click something but maybe not order sensitive.
# 2. Does not update everytime I click but does a final calculation. Has to include brackets

# First, I am going to work on #2

from tkinter import *

calculator = Tk()
calculator.title("Calculator")

# the padx of the button is smaller because it is relative the the entry.grid(columnspan)
# Here I am going to create two entries, one for the column and
entry = Entry(calculator, width=40, borderwidth=10)
output = Label(calculator, text="Answer: ")
# now use the columnspan feature so that there can be several numbers under the entry
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
output.grid(row=1, column=1)

# Look into whether I can manage this function as a class


def button_click(number):
    if type(number) == type(1):
        current = entry.get()
        entry.insert(len(current), number)
    elif number == "Delete":
        current = entry.get()
        entry.delete(0, END)
        entry.insert(0, current[:-1])
    elif number == "Clear All":
        entry.delete(0, END)
    elif number == "plus":
        current = entry.get()
        entry.insert(len(current), "+")
    elif number == "minus":
        current = entry.get()
        entry.insert(len(current), "-")
    elif number == "multiply":
        current = entry.get()
        entry.insert(len(current), "×")
    elif number == "divide":
        current = entry.get()
        entry.insert(len(current), "÷")

# This could work too, but it is longer
#current = e.get()
# entry.delete(0,END)
# entry.insert(0,str(current)+str(number))


# Creating the buttons
button_0 = Button(calculator, text="0", padx=40, pady=20,
                  command=lambda: button_click(0))
button_1 = Button(calculator, text="1", padx=40, pady=20,
                  command=lambda: button_click(1))
button_2 = Button(calculator, text="2", padx=40, pady=20,
                  command=lambda: button_click(2))
button_3 = Button(calculator, text="3", padx=40, pady=20,
                  command=lambda: button_click(3))
button_4 = Button(calculator, text="4", padx=40, pady=20,
                  command=lambda: button_click(4))
button_5 = Button(calculator, text="5", padx=40, pady=20,
                  command=lambda: button_click(5))
button_6 = Button(calculator, text="6", padx=40, pady=20,
                  command=lambda: button_click(6))
button_7 = Button(calculator, text="7", padx=40, pady=20,
                  command=lambda: button_click(7))
button_8 = Button(calculator, text="8", padx=40, pady=20,
                  command=lambda: button_click(8))
button_9 = Button(calculator, text="9", padx=40, pady=20,
                  command=lambda: button_click(9))
button_plus = Button(calculator, text="+", padx=40, pady=20,
                     command=lambda: button_click("plus"))
button_minus = Button(calculator, text="-", padx=40,
                      pady=20, command=lambda: button_click("minus"))
button_multiply = Button(calculator, text="×", padx=40,
                         pady=20, command=lambda: button_click("multiply"))
button_divide = Button(calculator, text="÷", padx=40,
                       pady=20, command=lambda: button_click("divide"))
button_equal = Button(calculator, text="=", padx=40,
                      pady=50, command=lambda: button_click("equal"))
button_delete = Button(calculator, text="Delete",
                       padx=27, pady=20, comm="Delete")
button_clear_all = Button(calculator, text="Clear All", padx=23,
                          pady=20, command=lambda: button_click("Clear All"))


# Putting the buttons on the screen

button_0.grid(row=5, column=2)
button_plus.grid(row=5, column=0)
button_minus.grid(row=5, column=1)
button_multiply.grid(row=6, column=0)
button_divide.grid(row=6, column=1)
button_delete.grid(row=7, column=1)
button_clear_all.grid(row=7, column=0)
button_equal.grid(row=6, column=2, rowspan=2)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

answer = Label(calculator, width=10, borderwidth=10,
               state=DISABLED, text="bad")
answer.grid(row=1, column=2)

entry.mainloop()

