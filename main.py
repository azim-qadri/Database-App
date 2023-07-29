from tkinter import *
import sqlite3


def add():
    # connect
    conn = sqlite3.connect('data.db')
    # cursor
    c = conn.cursor()
    # query
    c.execute("""CREATE TABLE IF NOT EXISTS addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
        )""")
    c.execute("INSERT INTO addresses VALUES(:first, :last, :address, :city, :state, :zipcode)",
              {
                  'first': f_name_ent.get(),
                  'last': l_name_ent.get(),
                  'address': address_ent.get(),
                  'city': city_ent.get(),
                  'state': state_ent.get(),
                  'zipcode': zip_ent.get()
              })

    # commit
    conn.commit()
    # close
    conn.close()


def show():
    # connect
    conn = sqlite3.connect('data.db')
    # cursor
    c = conn.cursor()
    # query
    c.execute("SELECT *,oid FROM addresses")
    records = c.fetchall()
    all_records = ''
    for record in records:
        all_records += str(record).removeprefix('(').removesuffix(')') + "\n"
    Label(root, text=all_records).grid(row=11, column=0, columnspan=2, padx=10, pady=10)

    # commit
    conn.commit()
    # close
    conn.close()


def delete():
    # connect
    conn = sqlite3.connect('data.db')
    # cursor
    c = conn.cursor()
    # query
    c.execute("DELETE FROM addresses WHERE oid="+sel_ent.get())
    sel_ent.delete(0, END)
    # commit
    conn.commit()
    # close
    conn.close()


def edit():
    global editor
    global f_name_ent_edit
    global l_name_ent_edit
    global address_ent_edit
    global city_ent_edit
    global state_ent_edit
    global zip_ent_edit
    editor = Tk()
    editor.title('Update A Record')

    # create labels
    f_name_lbl = Label(editor, text='First Name')
    f_name_lbl.grid(row=0, column=0, padx=10)
    l_name_lbl = Label(editor, text='Last Name')
    l_name_lbl.grid(row=1, column=0)
    address_lbl = Label(editor, text='Address')
    address_lbl.grid(row=2, column=0)
    city_lbl = Label(editor, text='City')
    city_lbl.grid(row=3, column=0)
    state_lbl = Label(editor, text='State')
    state_lbl.grid(row=4, column=0)
    zip_lbl = Label(editor, text='Zip code')
    zip_lbl.grid(row=5, column=0)

    # create entry
    f_name_ent_edit = Entry(editor, width=35)
    f_name_ent_edit.grid(row=0, column=1)
    l_name_ent_edit = Entry(editor, width=35)
    l_name_ent_edit.grid(row=1, column=1)
    address_ent_edit = Entry(editor, width=35)
    address_ent_edit.grid(row=2, column=1)
    city_ent_edit = Entry(editor, width=35)
    city_ent_edit.grid(row=3, column=1)
    state_ent_edit = Entry(editor, width=35)
    state_ent_edit.grid(row=4, column=1)
    zip_ent_edit = Entry(editor, width=35)
    zip_ent_edit.grid(row=5, column=1)

    record = sel_ent.get()
    # connect
    conn = sqlite3.connect('data.db')
    # cursor
    c = conn.cursor()
    # query
    c.execute("SELECT * FROM addresses WHERE oid="+record)
    records = c.fetchall()
    for rec in records:
        f_name_ent_edit.insert(0, rec[0])
        l_name_ent_edit.insert(0, rec[1])
        address_ent_edit.insert(0, rec[2])
        city_ent_edit.insert(0, rec[3])
        state_ent_edit.insert(0, rec[4])
        zip_ent_edit.insert(0, rec[5])

    # commit
    conn.commit()
    # close
    conn.close()
    # btn
    save_btn = Button(editor, text='Save', command=save)
    save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=137)


def save():
    # connect
    conn = sqlite3.connect('data.db')
    # cursor
    c = conn.cursor()
    record_id = sel_ent.get()
    # query
    c.execute("""UPDATE addresses SET 
    first_name = :f_name,
    last_name = :l_name,
    address = :address,
    city = :city,
    state = :state,
    zip = :zip
    
    WHERE oid = oid""",
              {
                  'f_name': f_name_ent_edit.get(),
                  'l_name': l_name_ent_edit.get(),
                  'address': address_ent_edit.get(),
                  'city': city_ent_edit.get(),
                  'state': state_ent_edit.get(),
                  'zip': zip_ent_edit.get(),
                  'oid': record_id

              })
    # commit
    conn.commit()
    # close
    conn.close()
    editor.destroy()


root = Tk()
root.title('Database')

# create labels
f_name_lbl = Label(root, text='First Name')
f_name_lbl.grid(row=0, column=0, padx=10)
l_name_lbl = Label(root, text='Last Name')
l_name_lbl.grid(row=1, column=0)
address_lbl = Label(root, text='Address')
address_lbl.grid(row=2, column=0)
city_lbl = Label(root, text='City')
city_lbl.grid(row=3, column=0)
state_lbl = Label(root, text='State')
state_lbl.grid(row=4, column=0)
zip_lbl = Label(root, text='Zip code')
zip_lbl.grid(row=5, column=0)
sel_lbl = Label(root, text='Select Id')
sel_lbl.grid(row=8, column=0)

# create entry
f_name_ent = Entry(root, width=35)
f_name_ent.grid(row=0, column=1)
l_name_ent = Entry(root, width=35)
l_name_ent.grid(row=1, column=1)
address_ent = Entry(root, width=35)
address_ent.grid(row=2, column=1)
city_ent = Entry(root, width=35)
city_ent.grid(row=3, column=1)
state_ent = Entry(root, width=35)
state_ent.grid(row=4, column=1)
zip_ent = Entry(root, width=35)
zip_ent.grid(row=5, column=1)
sel_ent = Entry(root, width=35)
sel_ent.grid(row=8, column=1)

# create buttons
add_record = Button(root, text='Add Record', command=add)
add_record.grid(row=6, column=0, columnspan=2, ipadx=137, padx=10, pady=10)
show_records = Button(root, text='Show Records', command=show)
show_records.grid(row=7, column=0, columnspan=2, ipadx=132, padx=10, pady=10)
del_record = Button(root, text='Delete Record', command=delete)
del_record.grid(row=9, column=0, columnspan=2, ipadx=132, padx=10, pady=10)
upd_record = Button(root, text='Update Record', command=edit)
upd_record.grid(row=10, column=0, columnspan=2, ipadx=132, padx=10, pady=10)

root.mainloop()
