from tkinter import *

root = Tk()

intro = Label(
    root, text='This is God speaking. I want to ask you one question. Is Suguru gay?')
intro.grid(row=0, column=0)

final = StringVar()
final.set("God's words will appear here.")


def decision(choice):
    final_print.config(text=choice)
    #final_print = Label(root, text=choice).grid(row=3, column=0)


Radiobutton(root, text="Yes, Suguru is gay.", variable=final, value="No, you filthy piece of trash! Suguru is not gay, isn't it obvious?!",
            command=lambda: decision(final.get())).grid(row=1, column=0)

Radiobutton(root, text="No, Suguru is straight.", variable=final,
            value="Yes, you are absolutely correct!! God bless you!!", command=lambda: decision(final.get())).grid(row=2, column=0)
final_print = Label(root, text=final.get())
final_print.grid(row=3, column=0)

mainloop()
