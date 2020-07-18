#Two types: 
#1. Updates every time I click something but maybe not order sensitive.
#2. Does not update everytime I click but does a final calculation. Has to include brackets

#First, I am going to work on #2
#Make sure to iterate over strings because a forloop cannnot go through integers.

from tkinter import *
from tkinter import font as tkFont

calculator = Tk()
calculator.title("Calculator")

# the padx of the button is smaller because it is relative the the entry.grid(columnspan)
# Here I am going to create two entries, one for the column and
entry = Entry(calculator, width=40, borderwidth=10)

def keyboard(event):
    entry.config(state=DISABLED)
    button_0.config(state=DISABLED, bg="orange")
    button_1.config(state=DISABLED, bg="orange")
    button_2.config(state=DISABLED, bg="orange")
    button_3.config(state=DISABLED, bg="orange")
    button_4.config(state=DISABLED, bg="orange")
    button_5.config(state=DISABLED, bg="orange")
    button_6.config(state=DISABLED, bg="orange")
    button_7.config(state=DISABLED, bg="orange")
    button_8.config(state=DISABLED, bg="orange")
    button_9.config(state=DISABLED, bg="orange")
    button_plus.config(state=DISABLED, bg="orange")
    button_minus.config(state=DISABLED, bg="orange")
    button_multiply.config(state=DISABLED, bg="orange")
    button_divide.config(state=DISABLED, bg="orange")
    button_open_bracket.config(state=DISABLED, bg="orange")
    button_close_bracket.config(state=DISABLED, bg="orange")
    button_delete.config(state=DISABLED, bg="orange")
    button_equal.config(state=DISABLED, bg="orange")
    button_clear_all.config(bg="red")
    answer.config(text="Click 'Clear All'")

entry.bind("<Button-1>", keyboard)
#To only allow certain inputs, I have to allow validation for the entry

output = Label(calculator, text="Answer: ")
# now use the columnspan feature so that there can be several numbers under the entry
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
output.grid(row=1, column=1)

# I can disable and enable keys based on what was currently typed. Disabled: orange, Enabled: green, Error: red

#1. Detect open and closed brackets and match them up in order.
#2. Recognize +/-/* and /.
#3. Divide based on brackets, then int spaces between signs. then apply the sign and 
##. actually calculate it
#4. Replace the number in the original equation without brackets
#5 continue until the end of the brackets division list. 

def open_position(string):
    open_pos = []
    for char in range(0, len(string)):
        if string[char] == "(":
            open_pos.append(char)
    return open_pos

a = open_position(entry.get())

def close_position(string):
    closed_pos = []
    for haha in range(0, len(string)):
        if string[haha] == ")":
            closed_pos.append(haha)
    return closed_pos

b = close_position(entry.get())

def last():
    final = eval(entry.get())
    if final % 1 == 0:
        final = int(final)
    final = round(final, 13)
    answer.config(text=final)

#!Checklist
#1. plus, minus, multiply, divide
#2. 0
#3. num
#4. equal sign
#5. (
#6. )
def button_click(number):
    #OK
    if number.isdigit():
        current = entry.get()
        entry.insert(len(current), number)
        button_plus.config(state=NORMAL,bg="green")
        button_minus.config(state=NORMAL,bg="green")
        button_multiply.config(state=NORMAL,bg="green")
        button_divide.config(state=NORMAL,bg="green")
        button_0.config(state=NORMAL,bg="green")
        button_open_bracket.config(state=DISABLED,bg="orange")
        button_1.config(state=NORMAL, bg="green")
        button_2.config(state=NORMAL, bg="green")
        button_3.config(state=NORMAL, bg="green")
        button_4.config(state=NORMAL, bg="green")
        button_5.config(state=NORMAL, bg="green")
        button_6.config(state=NORMAL, bg="green")
        button_7.config(state=NORMAL, bg="green")
        button_8.config(state=NORMAL, bg="green")
        button_9.config(state=NORMAL, bg="green")
        if len(open_position(entry.get())) == len(close_position(entry.get())):
            button_close_bracket.config(state=DISABLED,bg="orange")
            button_equal.config(state=NORMAL, bg="green")
        elif len(open_position(entry.get())) > len(close_position(entry.get())):
            button_close_bracket.config(state=NORMAL,bg="green")
            button_equal.config(state=DISABLED, bg="orange")
        else:
            button_close_bracket.config(state=DISABLED,bg="orange")
            button_equal.config(state=DISABLED, bg="orange")

    elif number == "Clear All":
        button_delete.config(state=NORMAL, bg="green")
        entry.config(state=NORMAL)
        answer.config(text="")
        entry.delete(0, END)
        button_plus.config(state=DISABLED, bg="orange")
        button_minus.config(state=DISABLED, bg="orange")
        button_multiply.config(state=DISABLED, bg="orange")
        button_divide.config(state=DISABLED, bg="orange")
        button_0.config(state=DISABLED,bg="orange")
        button_equal.config(state=DISABLED, bg="orange")
        button_open_bracket.config(state=NORMAL, bg="green")
        button_close_bracket.config(state=DISABLED, bg="orange")
        button_1.config(state=NORMAL, bg="green")
        button_2.config(state=NORMAL, bg="green")
        button_3.config(state=NORMAL, bg="green")
        button_4.config(state=NORMAL, bg="green")
        button_5.config(state=NORMAL, bg="green")
        button_6.config(state=NORMAL, bg="green")
        button_7.config(state=NORMAL, bg="green")
        button_8.config(state=NORMAL, bg="green")
        button_9.config(state=NORMAL, bg="green")
        button_clear_all.config(bg="green")
        

    elif number == "plus":
        current = entry.get()
        entry.insert(len(current), "+")
        button_plus.config(state=DISABLED, bg="orange")
        button_minus.config(state=DISABLED, bg="orange")
        button_multiply.config(state=DISABLED, bg="orange")
        button_divide.config(state=DISABLED, bg="orange")
        button_0.config(state=DISABLED,bg="orange")
        button_equal.config(state=DISABLED, bg="orange")
        button_open_bracket.config(state=NORMAL, bg="green")
        button_close_bracket.config(state=DISABLED, bg="orange")
        button_1.config(state=NORMAL, bg="green")
        button_2.config(state=NORMAL, bg="green")
        button_3.config(state=NORMAL, bg="green")
        button_4.config(state=NORMAL, bg="green")
        button_5.config(state=NORMAL, bg="green")
        button_6.config(state=NORMAL, bg="green")
        button_7.config(state=NORMAL, bg="green")
        button_8.config(state=NORMAL, bg="green")
        button_9.config(state=NORMAL, bg="green")

        
    elif number == "minus":
        current = entry.get()
        entry.insert(len(current), "-")
        button_plus.config(state=DISABLED, bg="orange")
        button_minus.config(state=DISABLED, bg="orange")
        button_multiply.config(state=DISABLED, bg="orange")
        button_divide.config(state=DISABLED, bg="orange")
        button_0.config(state=DISABLED,bg="orange")
        button_equal.config(state=DISABLED, bg="orange")
        button_open_bracket.config(state=NORMAL, bg="green")
        button_close_bracket.config(state=DISABLED, bg="orange")
        button_1.config(state=NORMAL, bg="green")
        button_2.config(state=NORMAL, bg="green")
        button_3.config(state=NORMAL, bg="green")
        button_4.config(state=NORMAL, bg="green")
        button_5.config(state=NORMAL, bg="green")
        button_6.config(state=NORMAL, bg="green")
        button_7.config(state=NORMAL, bg="green")
        button_8.config(state=NORMAL, bg="green")
        button_9.config(state=NORMAL, bg="green")
        

    elif number == "multiply":
        current = entry.get()
        entry.insert(len(current), "*")
        button_plus.config(state=DISABLED, bg="orange")
        button_minus.config(state=DISABLED, bg="orange")
        button_multiply.config(state=DISABLED, bg="orange")
        button_divide.config(state=DISABLED, bg="orange")
        button_0.config(state=DISABLED,bg="orange")
        button_equal.config(state=DISABLED, bg="orange")
        button_open_bracket.config(state=NORMAL, bg="green")
        button_close_bracket.config(state=DISABLED, bg="orange")
        button_1.config(state=NORMAL, bg="green")
        button_2.config(state=NORMAL, bg="green")
        button_3.config(state=NORMAL, bg="green")
        button_4.config(state=NORMAL, bg="green")
        button_5.config(state=NORMAL, bg="green")
        button_6.config(state=NORMAL, bg="green")
        button_7.config(state=NORMAL, bg="green")
        button_8.config(state=NORMAL, bg="green")
        button_9.config(state=NORMAL, bg="green")

    elif number == "divide":
        current = entry.get()
        entry.insert(len(current), "/")
        button_plus.config(state=DISABLED, bg="orange")
        button_minus.config(state=DISABLED, bg="orange")
        button_multiply.config(state=DISABLED, bg="orange")
        button_divide.config(state=DISABLED, bg="orange")
        button_0.config(state=DISABLED,bg="orange")
        button_equal.config(state=DISABLED, bg="orange")
        button_open_bracket.config(state=NORMAL, bg="green")
        button_close_bracket.config(state=DISABLED, bg="orange")
        button_1.config(state=NORMAL, bg="green")
        button_2.config(state=NORMAL, bg="green")
        button_3.config(state=NORMAL, bg="green")
        button_4.config(state=NORMAL, bg="green")
        button_5.config(state=NORMAL, bg="green")
        button_6.config(state=NORMAL, bg="green")
        button_7.config(state=NORMAL, bg="green")
        button_8.config(state=NORMAL, bg="green")
        button_9.config(state=NORMAL, bg="green")
        
    elif number == "(":
        current = entry.get()
        entry.insert(len(current), "(")
        button_plus.config(state=DISABLED, bg="orange")
        button_minus.config(state=DISABLED, bg="orange")
        button_multiply.config(state=DISABLED, bg="orange")
        button_divide.config(state=DISABLED, bg="orange")
        button_0.config(state=DISABLED,bg="orange")
        button_equal.config(state=DISABLED, bg="orange")
        button_open_bracket.config(state=NORMAL, bg="green")
        button_close_bracket.config(state=DISABLED, bg="orange")
        button_1.config(state=NORMAL, bg="green")
        button_2.config(state=NORMAL, bg="green")
        button_3.config(state=NORMAL, bg="green")
        button_4.config(state=NORMAL, bg="green")
        button_5.config(state=NORMAL, bg="green")
        button_6.config(state=NORMAL, bg="green")
        button_7.config(state=NORMAL, bg="green")
        button_8.config(state=NORMAL, bg="green")
        button_9.config(state=NORMAL, bg="green")
        
    elif number == ")":
        current = entry.get()
        entry.insert(len(current), ")")
        button_plus.config(state=NORMAL, bg="green")
        button_minus.config(state=NORMAL, bg="green")
        button_multiply.config(state=NORMAL, bg="green")
        button_divide.config(state=NORMAL, bg="green")
        button_0.config(state=DISABLED,bg="orange")
        button_equal.config(state=NORMAL, bg="green")
        button_open_bracket.config(state=DISABLED, bg="orange")
        button_1.config(state=DISABLED, bg="orange")
        button_2.config(state=DISABLED, bg="orange")
        button_3.config(state=DISABLED, bg="orange")
        button_4.config(state=DISABLED, bg="orange")
        button_5.config(state=DISABLED, bg="orange")
        button_6.config(state=DISABLED, bg="orange")
        button_7.config(state=DISABLED, bg="orange")
        button_8.config(state=DISABLED, bg="orange")
        button_9.config(state=DISABLED, bg="orange")
        if len(open_position(entry.get())) == len(close_position(entry.get())):
            button_close_bracket.config(state=DISABLED,bg="orange")
            button_equal.config(state=NORMAL, bg="green")
        elif len(open_position(entry.get())) > len(close_position(entry.get())):
            button_close_bracket.config(state=NORMAL,bg="green")
            button_equal.config(state=DISABLED, bg="orange")
        else:
            button_close_bracket.config(state=DISABLED,bg="orange")
            button_equal.config(state=DISABLED, bg="orange")
    
    elif number == "Delete":
        #Integers have turned into strings. Careful of type
        answer.config(text="")
        current = entry.get()
        entry.delete(0, END)
        entry.insert(0, current[:-1])
        if len(entry.get()) == 0:
            button_plus.config(state=DISABLED, bg="orange")
            button_minus.config(state=DISABLED, bg="orange")
            button_multiply.config(state=DISABLED, bg="orange")
            button_divide.config(state=DISABLED, bg="orange")
            button_0.config(state=DISABLED,bg="orange")
            button_equal.config(state=DISABLED, bg="orange")
            button_open_bracket.config(state=NORMAL, bg="green")
            button_close_bracket.config(state=DISABLED, bg="orange")
            button_1.config(state=NORMAL, bg="green")
            button_2.config(state=NORMAL, bg="green")
            button_3.config(state=NORMAL, bg="green")
            button_4.config(state=NORMAL, bg="green")
            button_5.config(state=NORMAL, bg="green")
            button_6.config(state=NORMAL, bg="green")
            button_7.config(state=NORMAL, bg="green")
            button_8.config(state=NORMAL, bg="green")
            button_9.config(state=NORMAL, bg="green")

        elif (entry.get()[-1]).isdigit():
            button_plus.config(state=NORMAL,bg="green")
            button_minus.config(state=NORMAL,bg="green")
            button_multiply.config(state=NORMAL,bg="green")
            button_divide.config(state=NORMAL,bg="green")
            button_0.config(state=NORMAL,bg="green")
            button_open_bracket.config(state=DISABLED,bg="orange")
            button_equal.config(state=NORMAL, bg="green")
            button_1.config(state=NORMAL, bg="green")
            button_2.config(state=NORMAL, bg="green")
            button_3.config(state=NORMAL, bg="green")
            button_4.config(state=NORMAL, bg="green")
            button_5.config(state=NORMAL, bg="green")
            button_6.config(state=NORMAL, bg="green")
            button_7.config(state=NORMAL, bg="green")
            button_8.config(state=NORMAL, bg="green")
            button_9.config(state=NORMAL, bg="green")
            if len(open_position(entry.get())) == len(close_position(entry.get())):
                button_close_bracket.config(state=DISABLED,bg="orange")
                button_equal.config(state=NORMAL, bg="green")
            elif len(open_position(entry.get())) > len(close_position(entry.get())):
                button_close_bracket.config(state=NORMAL,bg="green")
                button_equal.config(state=DISABLED, bg="orange")
            else:
                button_close_bracket.config(state=DISABLED,bg="orange")
                button_equal.config(state=DISABLED, bg="orange")

        elif entry.get()[-1] == "+":
            button_plus.config(state=DISABLED, bg="orange")
            button_minus.config(state=DISABLED, bg="orange")
            button_multiply.config(state=DISABLED, bg="orange")
            button_divide.config(state=DISABLED, bg="orange")
            button_0.config(state=DISABLED,bg="orange")
            button_equal.config(state=DISABLED, bg="orange")
            button_open_bracket.config(state=NORMAL, bg="green")
            button_close_bracket.config(state=DISABLED, bg="orange")
            button_1.config(state=NORMAL, bg="green")
            button_2.config(state=NORMAL, bg="green")
            button_3.config(state=NORMAL, bg="green")
            button_4.config(state=NORMAL, bg="green")
            button_5.config(state=NORMAL, bg="green")
            button_6.config(state=NORMAL, bg="green")
            button_7.config(state=NORMAL, bg="green")
            button_8.config(state=NORMAL, bg="green")
            button_9.config(state=NORMAL, bg="green")

            
        elif entry.get()[-1] == "-":
            button_plus.config(state=DISABLED, bg="orange")
            button_minus.config(state=DISABLED, bg="orange")
            button_multiply.config(state=DISABLED, bg="orange")
            button_divide.config(state=DISABLED, bg="orange")
            button_0.config(state=DISABLED,bg="orange")
            button_equal.config(state=DISABLED, bg="orange")
            button_open_bracket.config(state=NORMAL, bg="green")
            button_close_bracket.config(state=DISABLED, bg="orange")
            button_1.config(state=NORMAL, bg="green")
            button_2.config(state=NORMAL, bg="green")
            button_3.config(state=NORMAL, bg="green")
            button_4.config(state=NORMAL, bg="green")
            button_5.config(state=NORMAL, bg="green")
            button_6.config(state=NORMAL, bg="green")
            button_7.config(state=NORMAL, bg="green")
            button_8.config(state=NORMAL, bg="green")
            button_9.config(state=NORMAL, bg="green")
            

        elif entry.get()[-1] == "*":
            button_plus.config(state=DISABLED, bg="orange")
            button_minus.config(state=DISABLED, bg="orange")
            button_multiply.config(state=DISABLED, bg="orange")
            button_divide.config(state=DISABLED, bg="orange")
            button_0.config(state=DISABLED,bg="orange")
            button_equal.config(state=DISABLED, bg="orange")
            button_open_bracket.config(state=NORMAL, bg="green")
            button_close_bracket.config(state=DISABLED, bg="orange")
            button_1.config(state=NORMAL, bg="green")
            button_2.config(state=NORMAL, bg="green")
            button_3.config(state=NORMAL, bg="green")
            button_4.config(state=NORMAL, bg="green")
            button_5.config(state=NORMAL, bg="green")
            button_6.config(state=NORMAL, bg="green")
            button_7.config(state=NORMAL, bg="green")
            button_8.config(state=NORMAL, bg="green")
            button_9.config(state=NORMAL, bg="green")

        elif entry.get()[-1] == "/":
            button_plus.config(state=DISABLED, bg="orange")
            button_minus.config(state=DISABLED, bg="orange")
            button_multiply.config(state=DISABLED, bg="orange")
            button_divide.config(state=DISABLED, bg="orange")
            button_0.config(state=DISABLED,bg="orange")
            button_equal.config(state=DISABLED, bg="orange")
            button_open_bracket.config(state=NORMAL, bg="green")
            button_close_bracket.config(state=DISABLED, bg="orange")
            button_1.config(state=NORMAL, bg="green")
            button_2.config(state=NORMAL, bg="green")
            button_3.config(state=NORMAL, bg="green")
            button_4.config(state=NORMAL, bg="green")
            button_5.config(state=NORMAL, bg="green")
            button_6.config(state=NORMAL, bg="green")
            button_7.config(state=NORMAL, bg="green")
            button_8.config(state=NORMAL, bg="green")
            button_9.config(state=NORMAL, bg="green")
            
        elif entry.get()[-1] == "(":
            button_plus.config(state=DISABLED, bg="orange")
            button_minus.config(state=DISABLED, bg="orange")
            button_multiply.config(state=DISABLED, bg="orange")
            button_divide.config(state=DISABLED, bg="orange")
            button_0.config(state=DISABLED,bg="orange")
            button_equal.config(state=DISABLED, bg="orange")
            button_open_bracket.config(state=NORMAL, bg="green")
            button_close_bracket.config(state=DISABLED, bg="orange")
            button_1.config(state=NORMAL, bg="green")
            button_2.config(state=NORMAL, bg="green")
            button_3.config(state=NORMAL, bg="green")
            button_4.config(state=NORMAL, bg="green")
            button_5.config(state=NORMAL, bg="green")
            button_6.config(state=NORMAL, bg="green")
            button_7.config(state=NORMAL, bg="green")
            button_8.config(state=NORMAL, bg="green")
            button_9.config(state=NORMAL, bg="green")
            
        elif entry.get()[-1] == ")":
            button_plus.config(state=NORMAL, bg="green")
            button_minus.config(state=NORMAL, bg="green")
            button_multiply.config(state=NORMAL, bg="green")
            button_divide.config(state=NORMAL, bg="green")
            button_0.config(state=DISABLED,bg="orange")
            button_equal.config(state=NORMAL, bg="green")
            button_open_bracket.config(state=DISABLED, bg="orange")
            button_1.config(state=DISABLED, bg="orange")
            button_2.config(state=DISABLED, bg="orange")
            button_3.config(state=DISABLED, bg="orange")
            button_4.config(state=DISABLED, bg="orange")
            button_5.config(state=DISABLED, bg="orange")
            button_6.config(state=DISABLED, bg="orange")
            button_7.config(state=DISABLED, bg="orange")
            button_8.config(state=DISABLED, bg="orange")
            button_9.config(state=DISABLED, bg="orange")
            if len(open_position(entry.get())) == len(close_position(entry.get())):
                button_close_bracket.config(state=DISABLED,bg="orange")
                button_equal.config(state=NORMAL, bg="green")
            elif len(open_position(entry.get())) > len(close_position(entry.get())):
                button_close_bracket.config(state=NORMAL,bg="green")
                button_equal.config(state=DISABLED, bg="orange")
            else:
                button_close_bracket.config(state=DISABLED,bg="orange")
                button_equal.config(state=DISABLED, bg="orange")
        


#Here I will scan through the whole expression
#1 Brackets (BEDMAS)

# I am trying to make something which can correspond open brackets with closed brackets.
# I have realized that the corresponding closed bracket is the closest closed bracket counting to
# the right of the open bracket.





#Focus in and focus out
#Try
#I could make it so if I click on the entry widget the whole thing shuts down
#and I have to click the clear all button to restart


# This could work too, but it is longer
#current = e.get()
# entry.delete(0,END)
# entry.insert(0,str(current)+str(number))


# Creating the buttons
##IN THE FUTURE, I WANT TO MAKE IT SO I CAN DISABLE BUTTONS ACCORDING TO TYPING,
##EG. IF I TYPE "+", THE "=" BUTTON IS DISABLED ETC
default=tkFont.Font(size=13)
signs = tkFont.Font(size=20)
button_0 = Button(calculator, text="0", padx=40, pady=24,
                  command=lambda: button_click("0"), font=default, state=DISABLED, bg="orange")
button_1 = Button(calculator, text="1", padx=40, pady=20,
                  command=lambda: button_click("1"), font=default, state=NORMAL, bg="green")
button_2 = Button(calculator, text="2", padx=40, pady=20,
                  command=lambda: button_click("2"), font=default, state=NORMAL, bg="green")
button_3 = Button(calculator, text="3", padx=40, pady=20,
                  command=lambda: button_click("3"), font=default, state=NORMAL, bg="green")
button_4 = Button(calculator, text="4", padx=40, pady=20,
                  command=lambda: button_click("4"), font=default, state=NORMAL, bg="green")
button_5 = Button(calculator, text="5", padx=40, pady=20,
                  command=lambda: button_click("5"), font=default, state=NORMAL, bg="green")
button_6 = Button(calculator, text="6", padx=40, pady=20,
                  command=lambda: button_click("6"), font=default, state=NORMAL, bg="green")
button_7 = Button(calculator, text="7", padx=40, pady=20,
                  command=lambda: button_click("7"), font=default, state=NORMAL, bg="green")
button_8 = Button(calculator, text="8", padx=40, pady=20,
                  command=lambda: button_click("8"), font=default, state=NORMAL, bg="green")
button_9 = Button(calculator, text="9", padx=40, pady=20,
                  command=lambda: button_click("9"), font=default, state=NORMAL, bg="green")
button_plus = Button(calculator, text="+", padx=32, pady=13, state=DISABLED, bg="orange",
                     command=lambda: button_click("plus"), font=signs)
button_minus = Button(calculator, text="-", padx=34, state=DISABLED, bg="orange",
                      pady=13, command=lambda: button_click("minus"), font=signs)
button_multiply = Button(calculator, text="×", padx=31, state=DISABLED, bg="orange",
                         pady=13, command=lambda: button_click("multiply"), font=signs)
button_divide = Button(calculator, text="÷", padx=32, state=DISABLED, bg="orange",
                       pady=13, command=lambda: button_click("divide"), font=signs)
button_delete = Button(calculator, text="Delete",padx=21, pady=20, command=lambda: button_click("Delete"), font=default, state=NORMAL, bg="green")
button_clear_all = Button(calculator, text="Clear All", padx=14,
                          pady=20, command=lambda: button_click("Clear All"), font=default, state=NORMAL, bg="green")
                    
button_open_bracket = Button(calculator, text="(", padx=35, pady=13, command=lambda: button_click("("), font=signs,\
state=NORMAL, bg="green")
button_close_bracket = Button(calculator, text=")", padx=35,pady=13, command=lambda: button_click(")"), font=signs,\
state=DISABLED, bg="orange")

button_decimal = Button(calculator, text=".", command= lambda: button_click("."), font = signs, state=DISABLED, bg="orange", padx=35, pady=13)

button_equal = Button(calculator, text="=", padx=40,
                      pady=100, font=default, state=DISABLED, bg="orange", command=last)

# Putting the buttons on the screen

button_0.grid(row=5, column=2)
button_plus.grid(row=5, column=0)
button_minus.grid(row=5, column=1)
button_multiply.grid(row=6, column=0)
button_divide.grid(row=6, column=1)
button_open_bracket.grid(row=7,column=0)
button_close_bracket.grid(row=7,column=1)
button_delete.grid(row=8, column=1)
button_clear_all.grid(row=8, column=0)
button_equal.grid(row=6, column=2, rowspan=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

answer = Label(calculator, width=11, borderwidth=10, bg= "red", text="")
answer.grid(row=1, column=2, sticky=W)

calculator.resizable(True,True)
calculator.mainloop()

