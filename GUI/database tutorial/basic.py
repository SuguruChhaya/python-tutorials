import sqlite3
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Let's use databases!!")

# *Database
# *Use sqlite3 since it comes built in with python


# *Firstly, I have to create a database or connect to a pre-existing one.
# *Even if addressbook.db was not created, running this code will create it in that directry.
connection = sqlite3.connect('addressbook.db')

# *Next I have to create a cursor.
# *Cursor does the sending of the data.
cursor = connection.cursor()

#!Databases have columns and rows and I have to designate these columns and rows

# *Create table
# *Also have to specify data type
# *Sqlite has 5 datatyppes: text, int, real(float), nol(exist/not), image/video etc
'''
cursor.execute("""CREATE TABLE addresses (
                first name text,
                last name text,
                address text,
                city text,
                state text,
                zipcode integer
                )""")

'''
#*Create submit function database
def submit():
    #*First, I have to reconnect to the database inside of the function.
    #*I have to commit and connect too.
    connection = sqlite3.connect('addressbook.db')
    cursor = connection.cursor()


    #*Insert into table
    #*I have to create a dictionary for this following sqlite format.
    #!The keys for the dictionary would correspond to the VALUES
    cursor.execute("INSERT INTO addresses VALUES (:first_name, :last_name, :address, :city, :state, :zipcode)", 
    {
        'first_name': first_name.get(),
        'last_name': last_name.get(),
        'address': address.get(),
        'city': city.get(),
        'state': state.get(),
        'zipcode': zipcode.get()

    })

    connection.commit()
    connection.close()



    #*Clear textbox
    first_name.delete(0, END)
    last_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

def query():
    connection = sqlite3.connect("addressbook.db")
    cursor = connection.cursor()

    #*In sqlite3, there is a unique code for each item which is created by default which is called oid. But it is ignored.
    cursor.execute("SELECT *, oid FROM addresses ")
    #*Fetchall gets all record
    records = cursor.fetchall()
    #*Have to create label to print on screen
    #*I can see how the records are printed as tuples in a list.
    #*The oid seems to be ints starting from 1
    #print(records)

    print_record = ""
    for record in records:
        #*If I just want to print out the names
        print_record += str(record[0]) + " " + str(record[1]) + "\n"
    
    query_label = Label(root, text=print_record)
    query_label.grid(row=8, column=0, columnspan=2)




    connection.commit()
    connection.close()

#*Delete a record from the database
def delete_record():
    pass




#!After the code is ran once, I have to comment out the execute line


# *Create text label
first_label = Label(root, text="First name")
first_label.grid(row=0, column=0, pady=(10, 0))

last_label = Label(root, text="Last name")
last_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)


# *Create text boxes
first_name = Entry(root, width=30)
#*I could use a tuple for the padding if I just want to pad one side(top, bottom)
first_name.grid(row=0, column=1, padx=20, pady=(10, 0))

last_name = Entry(root, width=30)
last_name.grid(row=1, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

#*Create submit button
submit_button = Button(root, text="Add record to database", padx=20, pady=10, command=submit)
#ipadx helps to space things out.
submit_button.grid(row=6, column=0, columnspan=2, ipadx=10)

#*Create Query button to show all databse entries.
query_button = Button(root, text="Show entries", padx=20, pady=10, command=query)
query_button.grid(row=7, column=0, columnspan=2, ipadx=10)

# *Commit changes
connection.commit()

# *Close connection (not really required)
connection.close()

mainloop()
