
#*To delete, I can use the unique id number
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
    #!Works well if I put label before so I can grid_forget it.
    global query_label
    query_label.grid_forget()
    print_record = ""
    for record in records:
        #*If I just want to print out the names
        print_record += str(record[0]) + " " + str(record[1]) + "\t" + str(record[6]) + "\n"
    
    query_label = Label(root, text=print_record)
    query_label.grid(row=12, column=0, columnspan=2)


    connection.commit()
    connection.close()

#*Delete a record from the database
def delete_record():
    connection = sqlite3.connect('addressbook.db')
    cursor = connection.cursor()
    #*I could replace oid= to first_name etc. I have to break the quotation before deleting ID.
    cursor.execute("DELETE FROM addresses WHERE oid= " + delete_entry.get())





    connection.commit()
    connection.close()

def save_record():
    #*Save record after I edit them in the editor window.
    connection = sqlite3.connect('addressbook.db')
    cursor = connection.cursor()

    record_id = delete_entry.get()
    #*Update database 
    #!I have to use the names of column I assigned at first
    #*After the sql commands, I have to make the dictionary again
    #!As I had an error, always keep column names ONE WORD!! 
    cursor.execute("""UPDATE addresses SET
        first_name = :first_name,
        last_name = :last_name,
        address = :address,
        city = :city,
        state= :state,
        zipcode = :zipcode
    
        WHERE oid = :oid""",
        
        {'first_name': first_name_editor.get(),
        'last_name' : last_name_editor.get(),
        'address' : address_editor.get(),
        'state' : state_editor.get(),
        'city' : city_editor.get(),
        'state' : state_editor.get(),
        'zipcode': zipcode_editor.get(),
        'oid': record_id
        })
    #*Close whole window
    editor.destroy()


    connection.commit()
    connection.close()

    

#*Update a record
def update_record():

    connection = sqlite3.connect('addressbook.db')
    cursor = connection.cursor()
    record_id = delete_entry.get()

    #!Same as the query function to get the data
    cursor.execute("SELECT * FROM addresses WHERE oid=" + record_id)
    #*First have to fetch it.
    #!all_record only fetches the row specified!! Don't need to fetch everything
    all_record = cursor.fetchall()





    #*For editing, I will create a new window
    #!I need to make some of these entries and labels global to save them!!
    global editor
    editor = Tk()
    editor.title("Edit a record")
    first_label_editor = Label(editor, text="First name")
    first_label_editor.grid(row=0, column=0, pady=(10, 0))

    last_label_editor = Label(editor, text="Last name")
    last_label_editor.grid(row=1, column=0)

    address_label_editor = Label(editor, text="Address")
    address_label_editor.grid(row=2, column=0)

    city_label_editor = Label(editor, text="City")
    city_label_editor.grid(row=3, column=0)

    state_label_editor = Label(editor, text="State")
    state_label_editor.grid(row=4, column=0)

    zipcode_label_editor = Label(editor, text="Zipcode")
    zipcode_label_editor.grid(row=5, column=0)


    #*Make global
    global first_name_editor
    global last_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    first_name_editor = Entry(editor, width=30)
    #first_name_editor.insert(0, all_record[0][0])
    #*I could use a tuple for the padding if I just want to pad one side(top, bottom)




    first_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

    last_name_editor = Entry(editor, width=30)
    last_name_editor.grid(row=1, column=1, padx=20)

    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)

    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)

    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1, padx=20)

    save_button = Button(editor, text="Save record", command=save_record)
    save_button.grid(row=6, column=0, columnspan=2)

    #*Loop through results!!
    entry_list = [first_name_editor, last_name_editor, address_editor, city_editor, state_editor, zipcode_editor]
    #!When record_id = 1, I have to access the 0th item in the database. So I have to add -1 to the forloop
    counter = 0
    #*I have to be careful that all_record is a tuple in a list. But since there is only one tuple, I can
    #*just undo it by index 0
    for item in all_record[0]:
        entry_list[counter].insert(0, item)
        counter += 1

    


    connection.commit()
    connection.close()


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

query_label = Label(root, text="")
query_label.grid(row=11, column=0, columnspan=2)

#*Create a delete button
delete_label = Label(root, text="Select ID", width=10)
delete_label.grid(row=8, column=0)

delete_entry = Entry(root, width=30)
delete_entry.grid(row=8, column=1)

delete_button = Button(root, text="Delete record", command=delete_record)
delete_button.grid(row=9, column=0, columnspan=2, ipadx=10)

update_button = Button(root, text="Update record", command=update_record)
update_button.grid(row=10, column=0, columnspan=2, ipadx=10)


# *Commit changes
connection.commit()

# *Close connection (not really required)
connection.close()

mainloop()
