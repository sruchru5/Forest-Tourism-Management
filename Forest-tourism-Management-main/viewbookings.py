from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import mysql.connector
from tkinter import ttk, messagebox
import tkinter.filedialog



def home():
    import main
    


def reset():
	e1.delete(0,END)
	e2.delete(0,END)
	e3.delete(0,END)
	e4.delete(0,END)
	e5.delete(0,END)


def view():
    tree.delete(*tree.get_children())
    con = mysql.connector.connect(host="localhost",user="root",password="",database="foresttourism")
    cur = con.cursor()
    cur.execute("SELECT * FROM tblbooking")
    tabledata = cur.fetchall()
    cpt = 0
    for row in tabledata:
        tree.insert('', 'end', text=str(cpt), values=(row[1], row[2], row[3], row[4], row[5],row[6]))
        cpt += 1 
    con.commit()
    con.close()
master = Tk()
master.title('BOOKING DETAILS')
master.geometry('1366x768')
master.state('zoomed')




Label(master,text='BOOKING DETAILS',foreground="red",font=('Verdana',20,'bold')).pack(side=TOP,pady=10)




c2 = Canvas(master,bg='gray',width=1150,height=580)
c2.place(x=100,y=100)


tree = ttk.Treeview(master, selectmode='browse')
tree.place(height=550,width=1110,x=120,y=120)

vsb = ttk.Scrollbar(master, orient="vertical", command=tree.yview)
vsb.place(x=1500, y=181, height=548)

tree.configure(yscrollcommand=vsb.set)

tree["columns"] = ("1", "2","3","4","5","6")
tree['show'] = 'headings'
tree.column("1", width=100, anchor='c')
tree.column("2", width=100, anchor='c')
tree.column("3", width=100, anchor='c')
tree.column("4", width=100, anchor='c')
tree.column("5", width=100, anchor='c')
tree.column("6", width=100, anchor='c')




tree.heading("1", text="BOOKING ID")
tree.heading("2", text="PLACE ID")
tree.heading("3", text="PLACE NAME")
tree.heading("4", text="DATE")
tree.heading("5", text="NO OF PEOPLE")
tree.heading("6", text="USER ID")


view()
mainloop()
 
