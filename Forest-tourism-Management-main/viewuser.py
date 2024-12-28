from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import mysql.connector
from tkinter import ttk, messagebox
import tkinter.filedialog


def view():
    tree.delete(*tree.get_children())
    con = mysql.connector.connect(host="localhost",user="root",password="",database="foresttourism")
    cur = con.cursor()
    cur.execute("SELECT * FROM tbluser")
    tabledata = cur.fetchall()
    cpt = 0
    for row in tabledata:
        tree.insert('', 'end', text=str(cpt), values=(row[0], row[1], row[2], row[3], row[4]))
        cpt += 1 
    con.commit()
    con.close()


master = Tk()
master.title('VIEW USER')
master.geometry('1366x768')
master.state('zoomed')




Label(master,text='VIEW USER',foreground="red",font=('Verdana',20,'bold')).pack(side=TOP,pady=10)




c2 = Canvas(master,bg='gray',width=1150,height=580)
c2.place(x=100,y=100)


tree = ttk.Treeview(master, selectmode='browse')
tree.place(height=550,width=1110,x=120,y=120)

vsb = ttk.Scrollbar(master, orient="vertical", command=tree.yview)
vsb.place(x=1500, y=181, height=548)

tree.configure(yscrollcommand=vsb.set)

tree["columns"] = ("1", "2","3")
tree['show'] = 'headings'
tree.column("1", width=100, anchor='c')
tree.column("2", width=100, anchor='c')
tree.column("3", width=100, anchor='c')


tree.heading("1", text="NAME")
tree.heading("2", text="CONTACT NUMBER")
tree.heading("3", text="EMAIL ID")
view()
mainloop()
 
