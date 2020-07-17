from tkinter import *
import sqlite3

root = Tk()
root.title('MGA')
root.geometry('300x500')
root.iconbitmap('D:\Python\Level 2\Codemy\Python And TKinter\PYTkinter\Images/moon.ico')

conn = sqlite3.connect('address_book.db')
c = conn.cursor()

'''
c.execute("""CREATE TABLE addresses(
                    first_name text,
                    last_name text,
                    address text,
                    city text,
                    state text,
                    age integer)""")
'''

def delete():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("DELETE FROM addresses WHERE oid = " + id.get()) # No problem to put id.get() with no str here
    id.delete(0, END)
    conn.commit()
    conn.close()


def submit():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    if f_name.get() == '':
        pass
    else:
        c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :age)",
              {
                'f_name':f_name.get(),
                'l_name':l_name.get(),
                'address':address.get(),
                'city' : city.get(),
                'state': state.get(),
                'age' : age.get()
              }
              )

    conn.commit()
    conn.close()

    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    age.delete(0, END)

def show():
    global my_label
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute('SELECT *, oid FROM addresses')
    #c.fetchone()
    #c.fetchmany(50)
    records = c.fetchall()
    all_records = ''
    for record in records:
        all_records += str(record) + "\n"
        #all_records += str(record[6]) + " - " + str(record[0]) + " " + str(record[1]) + "\n"
    my_label = Label(root, text = all_records)
    my_label.grid(row = 11, column = 0, columnspan = 2)

    conn.commit()
    conn.close()

def clear():
    global my_label
    my_label.grid_forget()

f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=5)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20, pady=5)
address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20, pady=5)
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20, pady=5)
state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20, pady=5)
age = Entry(root, width=30)
age.grid(row=5, column=1, padx=20, pady=5)
id = Entry(root, width=30)
id.grid(row=9, column=1, padx=10, pady=5)

f_name_label = Label(root, text="First name").grid(row=0, column=0, padx=10, pady=5)
l_name_label = Label(root, text="Last name").grid(row=1, column=0, padx=10, pady=5)
address_label = Label(root, text="Address").grid(row=2, column=0, padx=10, pady=5)
city_label = Label(root, text="City").grid(row=3, column=0, padx=10, pady=5)
state_label = Label(root, text="State").grid(row=4, column=0, padx=10, pady=5)
age_label = Label(root, text="Age").grid(row=5, column=0, padx=10, pady=5)
id_label = Label(root, text="ID Record").grid(row=9, column=0, padx=10, pady=5)

submit_btn = Button(root, text="Add Record", fg = 'green', command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=5, ipadx=100)
query_butn = Button(root, text = "Show Records", fg = 'blue',command = show)
query_butn.grid(row=7, column=0, columnspan=2, padx=10, pady=5, ipadx=95)
clear_butn = Button(root, text = "Clear", fg = 'red',command = clear)
clear_butn.grid(row = 8, column = 0, columnspan = 2,padx=10, pady=5, ipadx=119)
delete_butn = Button(root, text = "Delete Record", fg = 'brown',command = delete)
delete_butn.grid(row = 10, column = 0, columnspan = 2,padx=10, pady=5, ipadx=95)

conn.commit()
conn.close()

root.mainloop()
