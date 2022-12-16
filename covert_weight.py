from tkinter import *

win = Tk()
win.title("Weight Conversion")
win.geometry("500x80")
win.attributes("-topmost", True) 
win["bg"] = "#20B2AA"
def convert_kg():
    gram = 1000*float(e2_value.get())
    pounds = 2.20462*float(e2_value.get()) 
    ounce = 35.274*float(e2_value.get())
    
    gr.delete("1.0", END)
    gr.insert(END,gram)
     
    po.delete("1.0", END)
    po.insert(END,pounds)
     
    ou.delete("1.0", END)
    ou.insert(END,ounce)

e1 = Label(win, text = "Enter the weight in Kg", bg = "#00FA9A", fg = "red")
e2_value = StringVar()
e2 = Entry(win, textvariable = e2_value)
e3 = Label(win, text = 'Gram', bg = "#00FA9A", fg = "red")
e4 = Label(win, text = 'Pounds', bg = "#00FA9A", fg = "red")
e5 = Label(win, text = 'Ounce', bg = "#00FA9A", fg = "red")

gr = Text(win, height =1 , width = 20)
po = Text(win, height =1 , width = 20)
ou = Text(win, height =1 , width = 20)

#Tạo button widget
b1 = Button(win, text = "Convert", bg = "yellow", fg = "red",  command = convert_kg)



e1.grid(row = 0, column = 0)
e2.grid(row = 0, column = 1)
e3.grid(row = 1, column = 0)
e4.grid(row = 1, column = 1)
e5.grid(row = 1, column = 2)

gr.grid(row = 2, column = 0)
po.grid(row = 2, column = 1)
ou.grid(row = 2, column = 2)

b1.grid(row = 0, column = 2)

win.mainloop()