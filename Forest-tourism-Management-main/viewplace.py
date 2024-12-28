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
    cur.execute("SELECT * FROM tbladdplace")
    tabledata = cur.fetchall()
    cpt = 0
    for row in tabledata:
        tree.insert('', 'end', text=str(cpt), values=(row[0], row[1], row[2], row[3], row[4]))
        cpt += 1 
    con.commit()
    con.close()



def edit(a):
    e1.configure(state='normal')
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)

    selectedItem = tree.selection()[0]
    e1.insert(0, tree.item(selectedItem)['values'][0])
    e1.configure(state='disabled')
    e2.insert(0, tree.item(selectedItem)['values'][1])
    e3.insert(0, tree.item(selectedItem)['values'][2])
    e4.insert(0, tree.item(selectedItem)['values'][3])
    e5.insert(0, tree.item(selectedItem)['values'][4])

def update():
    tree.delete(*tree.get_children())
    con = mysql.connector.connect(host="localhost",user="root",password="",database="pastoral")
    cur = con.cursor()
    cur.execute("UPDATE user_details SET user_name='%s',address='%s',email_id='%s',contact_number='%s' WHERE user_id = '%s' " %(e2.get(),e3.get(),e4.get(),e5.get(),int(e1.get())))
    cur.execute("SELECT * FROM user_details")
    tabledata = cur.fetchall()
    cpt = 0
    for row in tabledata:
        tree.insert('', 'end', text=str(cpt), values=(row[0], row[1], row[2], row[3], row[4]))
        cpt += 1 
    con.commit()
    con.close()
    

master = Tk()
master.title('VIEW PLACES')
master.geometry('1366x768')
master.state('zoomed')




Label(master,text='VIEW PLACES',foreground="red",font=('Verdana',20,'bold')).pack(side=TOP,pady=10)




c2 = Canvas(master,bg='gray',width=1150,height=580)
c2.place(x=100,y=100)


tree = ttk.Treeview(master, selectmode='browse')
tree.place(height=550,width=1110,x=120,y=120)

vsb = ttk.Scrollbar(master, orient="vertical", command=tree.yview)
vsb.place(x=1500, y=181, height=548)

tree.configure(yscrollcommand=vsb.set)

tree["columns"] = ("1", "2","3","4")
tree['show'] = 'headings'
tree.column("1", width=100, anchor='c')
tree.column("2", width=100, anchor='c')
tree.column("3", width=100, anchor='c')
tree.column("4", width=100, anchor='c')

tree.heading("1", text="PLACE ID")
tree.heading("2", text="PLACE NAME")
tree.heading("3", text="ADDRESS")
tree.heading("4", text="TIMINGS")

view()
mainloop()
 
