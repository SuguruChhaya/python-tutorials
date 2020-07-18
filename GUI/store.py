    elif number == "Delete":
        current = entry.get()
        entry.delete(0, END)
        entry.insert(0, current[:-1])
        if len(entry.get()) > 0 and entry.get()[-1] == ")":
            button_plus.config(state=NORMAL,bg="green")
            button_minus.config(state=NORMAL,bg="green")
            button_multiply.config(state=NORMAL,bg="green")
            button_divide.config(state=NORMAL,bg="green")
            button_equal.config(state=NORMAL, bg="green")
            if len(open_position(entry.get())) > len(close_position(entry.get())):
                button_close_bracket.config(state=NORMAL,bg="green")
            else:
                button_close_bracket.config(state=DISABLED,bg="orange")
        elif len(entry.get()) > 0 or not entry.get()[-1].isdigit():
            button_plus.config(state=DISABLED, bg="orange")
            button_minus.config(state=DISABLED, bg="orange")
            button_multiply.config(state=DISABLED, bg="orange")
            button_divide.config(state=DISABLED, bg="orange")
            button_0.config(state=DISABLED,bg="orange")

            if entry.get()[-1].isdigit():
                button_equal.config(state=NORMAL, bg="green")
                button_open_bracket.config(state=DISABLED,bg="orange")
            else:
                button_equal.config(state=DISABLED, bg="orange")
        else:
            button_plus.config(state=NORMAL,bg="green")
            button_minus.config(state=NORMAL,bg="green")
            button_multiply.config(state=NORMAL,bg="green")
            button_divide.config(state=NORMAL,bg="green")
            button_equal.config(state=DISABLED, bg="orange")
            if len(open_position(entry.get())) > len(close_position(entry.get())):
                button_close_bracket.config(state=NORMAL,bg="green")
            else:
                button_close_bracket.config(state=DISABLED,bg="orange")