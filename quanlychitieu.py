import tkinter 
from tkinter import *
from tkinter import ttk
import tkinter as tk
# import openpyxl

root = Tk()
root.title("Daily Expenses")
root.geometry("500x600+300+100") 


expense_data = []


def load_expense_data():
    for item in record_table.get_children():
        record_table.delete(item)
        
    for i in range(len(expense_data)):
        record_table.insert(parent='', index='end', text = '', iid = i, values = expense_data[i])

def put_expense_in_entry(index):
    expense_id.delete(0, END)
    expense_name.delete(0, END)
    expense_price.delete(0, END)
    expense_date.delete(0, END)
    
    exp_id = expense_data[index][0]
    exp_name = expense_data[index][1]
    exp_price = expense_data[index][2]
    exp_date = expense_data[index][3]

    
    expense_id.insert(0, exp_id)
    expense_name.insert(0, exp_name)
    expense_price.insert(0, exp_price)
    expense_date.insert(0, exp_date)
    
def clear_expense_data():
    expense_id.delete(0, END)
    expense_name.delete(0, END)
    expense_price.delete(0, END)
    expense_date.delete(0, END)
    load_expense_data()
    
def add_expense_data(exp_id, exp_name, exp_price, exp_date):
    expense_data.append([exp_id, exp_name, exp_price, exp_date]) 
    
    load_expense_data()
    clear_expense_data()
    
def update_expense_date(exp_id, exp_name, exp_price, exp_date, index):
    expense_data[index] = [exp_id, exp_name, exp_price, exp_date]
    
    load_expense_data()
    clear_expense_data()
     
def delete_expense_data(index):
    del expense_data[index]
    load_expense_data()
    clear_expense_data()

def find_expense_by_id(exp_id): 
    
    if exp_id != '':
        expense_data_index = []
        
        for data in expense_data:
            
            if str(exp_id) in str(data[0]):
                expense_data_index.append(expense_data.index(data))
        
        
        for item in record_table.get_children():
            record_table.delete(item)
        
        for i in expense_data_index:
            record_table.insert(parent='', index='end', text = '', iid = i, values = expense_data[i])
    else:
        load_expense_data()
        
        
# frame chứa widget Name, Price, Date of Expenses
head_frame = Frame(root)

heading_lbl = Label(head_frame, text = 'Daily Expense Data', font=('Bold', 13))
heading_lbl.pack(fill = X, pady=0)

# expense_id
expense_id_lbl = Label(head_frame, text = 'Expense Id: ', font = ('Bold', 10))
expense_id_lbl.place(x=0, y = 50)

expense_id = Entry(head_frame, font=('Bold', 10))
expense_id.place(x = 110,y=50,width =180)

# expense_name
expense_name_lbl = Label(head_frame, text = 'Expense Name: ', font = ('Bold', 10))
expense_name_lbl.place(x=0, y = 100)

expense_name = Entry(head_frame, font=('Bold', 10))
expense_name.place(x = 110,y=100,width =180)

# expense_price
expense_price_lbl = Label(head_frame, text = 'Expense Price: ', font = ('Bold', 10))
expense_price_lbl.place(x=0, y = 150)

expense_price = Entry(head_frame, font=('Bold', 10))
expense_price.place(x = 110,y=150,width =180)

# expense_date
expense_date_lbl = Label(head_frame, text = 'Expense Date: ', font = ('Bold', 10))
expense_date_lbl.place(x=0, y = 200)

expense_date = Entry(head_frame, font=('Bold', 10))
expense_date.place(x=110, y=200,width =180) 

# Nút thêm
add_btn = Button(head_frame, text = 'Add', font = ('Bold', 12), 
                 command = lambda: add_expense_data(expense_id.get(), 
                                                    expense_name.get(), 
                                                    expense_price.get(), 
                                                    expense_date.get()))
add_btn.place(x=20, y=250)

# Nút update
update_btn = Button(head_frame, text = 'Update', font = ('Bold', 12), 
                    command = lambda: update_expense_date(expense_id.get(), 
                                                          expense_name.get(), 
                                                          expense_price.get(), 
                                                          expense_date.get(), 
                                                         index=int(record_table.selection()[0])))
update_btn.place(x=85, y=250)

# Nút delete
delete_btn = Button(head_frame, text = 'Delete', font = ('Bold', 12),
                   command = lambda: delete_expense_data(index=int(record_table.selection()[0])))
delete_btn.place(x=163, y=250)

# Nút clear
clear_btn = Button(head_frame, text = 'Clear', font = ('Bold', 12),
                  command=lambda: clear_expense_data())
clear_btn.place(x=240, y=250)


head_frame.pack(pady = 10)
head_frame.pack_propagate(False)
head_frame.configure(width=400, height=300)



# frame search
search_bar_frame = Frame(root)
search_lbl = Label(search_bar_frame, text = 'Search Expense By Id: ', font=('Bold', 10))
search_lbl.pack(anchor=W)

search_entry = Entry(search_bar_frame, font=('Bold', 10))
search_entry.pack(anchor=W)
search_entry.bind('<KeyRelease>',lambda e: find_expense_by_id(search_entry.get()))

search_bar_frame.pack(pady=0)
search_bar_frame.pack_propagate(False)
search_bar_frame.configure(width=400, height=50)

# treeview
record_frame = Frame(root, bg = 'white')

record_table = ttk.Treeview(record_frame)
record_table.pack(fill=X, pady=5)

record_table.bind('<<TreeviewSelect>>', lambda e: put_expense_in_entry(int(record_table.selection()[0])))

record_table['column'] = ['Id','Name','Price','Date']

record_table.column('#0', anchor=W, width = 0, stretch=NO)
record_table.column('Id', anchor=W, width = 50)
record_table.column('Name', anchor=W, width = 100)
record_table.column('Price', anchor=W, width = 120)
record_table.column('Date', anchor=W, width = 160)

record_table.heading('Id', text = 'Id', anchor=W)
record_table.heading('Name', text = 'Name', anchor=W)
record_table.heading('Price', text = 'Price', anchor=W)
record_table.heading('Date', text = 'Date', anchor=W)

record_frame.pack(pady=10)
record_frame.pack_propagate(False)
record_frame.configure(width=400, height=200)

load_expense_data()

root.mainloop()     