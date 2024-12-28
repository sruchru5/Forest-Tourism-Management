from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import mysql.connector
from tkinter import ttk, messagebox
import tkinter.filedialog

def admndsh():
    import admindashboard
    

def reset():
	e1.delete(0,END)
	e2.delete(0,END)
	e3.delete(0,END)
	e4.delete(0,END)



def submit():
    tree.delete(*tree.get_children())
    if e2.get()=="":
        messagebox.showerror("Error","Enter PLACE NAME",parent=root)
    elif e3.get()=="":
        messagebox.showerror("Error","Enter ADDRESS",parent=root)
    elif e4.get()=="":
        messagebox.showerror("Error","Enter TIMINGS",parent=root)
    else:
        
        con = mysql.connector.connect(host="localhost",user="root",password="",database="foresttourism")
        cur = con.cursor()
        cur.execute("INSERT INTO tbladdplace (placeid,placename,address,timings) VALUES (%s,%s,%s,%s)",(e1.get(),e2.get(),e3.get(),e4.get())) 
        cur.execute("SELECT * FROM tbladdplace")
        tabledata = cur.fetchall()
        cpt = 0
        for row in tabledata:
            tree.insert('', 'end', text=str(cpt), values=(row[1], row[2], row[3],row[4]))
            cpt += 1 
        con.commit()
        con.close()
    e1.configure(state='normal')
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)


def edit(a):
    e1.configure(state='normal')
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)

    selectedItem = tree.selection()[0]
    e1.insert(0, tree.item(selectedItem)['values'][0])
    e1.configure(state='disabled')
    e2.insert(0, tree.item(selectedItem)['values'][1])
    e3.insert(0, tree.item(selectedItem)['values'][2])
    e4.insert(0, tree.item(selectedItem)['values'][3])
    
def update():
    tree.delete(*tree.get_children())
    con = mysql.connector.connect(host="localhost",user="root",password="",database="foresttourism")
    cur = con.cursor()
    cur.execute("UPDATE tbladdplace SET placename='%s',address='%s',timings='%s' WHERE placeid = '%s' " %(e2.get(),e3.get(),e4.get(),e1.get()))
    cur.execute("SELECT * FROM tbladdplace")
    tabledata = cur.fetchall()
    cpt = 0
    for row in tabledata:
        tree.insert('', 'end', text=str(cpt), values=(row[1], row[2], row[3], row[4]))
        cpt += 1 

    con.commit()
    con.close()
    e1.configure(state='normal')
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)


def delete():
    tree.delete(*tree.get_children())
    con = mysql.connector.connect(host="localhost",user="root",password="",database="foresttourism")
    cur = con.cursor()
    cur.execute("DELETE from tbladdplace WHERE placeid = '%s' " %(e1.get()))
    cur.execute("SELECT * FROM tbladdplace")
    tabledata = cur.fetchall()
    cpt = 0
    for row in tabledata:
        tree.insert('', 'end', text=str(cpt), values=(row[1], row[2], row[3], row[4]))
        cpt += 1 

    con.commit()
    con.close()




    
root = Tk()
root.title('ADD TOURIST FOREST PLACE')
root.geometry('1366x768')
root.state('zoomed')


var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()
var5=StringVar()


Label(root,text='ADD TOURIST FOREST PLACE',foreground="red",font=('Verdana',20,'bold')).pack(side=TOP,pady=10)



c1 = Canvas(root,bg='gray',width=500,height=580)
c1.place(x=50,y=100)




l0=Label(root,text='PLACE DETAILS',foreground="white",background='gray',font =('Verdana',13,'bold'))
l0.place(x=225,y=120)

l1=Label(root,text='PLACE ID',foreground="white",background='gray',font =('Verdana',13,'bold'))
l1.place(x=70,y=180)
e1=Entry(root,textvariable=var1,font=('Verdana',12,'bold'),foreground='RED',justify=LEFT)
e1.place(height=40,width=450,x=72,y=210)







l2=Label(root,text='PLACE NAME',foreground="white",background='gray',font =('Verdana',13,'bold'))
l2.place(x=70,y=260)
e2=Entry(root,textvariable=var2,font=('Verdana',12,'bold'),foreground='RED',justify=LEFT)
e2.place(height=40,width=450,x=72,y=290)



l3=Label(root,text='ADDRESS',foreground="white",background='gray',font =('Verdana',13,'bold'))
l3.place(x=70,y=340)
e3=Entry(root,textvariable=var3,font=('Verdana',12,'bold'),foreground='RED',justify=LEFT)
e3.place(height=40,width=450,x=72,y=370)



l4=Label(root,text='TIMINGS',foreground="white",background='gray',font =('Verdana',13,'bold'))
l4.place(x=70,y=420)
e4=Entry(root,textvariable=var4,font=('Verdana',12,'bold'),foreground='RED',justify=LEFT)
e4.place(height=40,width=450,x=72,y=450)




b1=Button(root,borderwidth=1, relief="flat",text="SUBMIT", font="verdana 15", bg="white", fg="gray",command=submit)
b1.place(height=60,width=200,x=70,y=520)

b2=Button(root,borderwidth=1, relief="flat",text="RESET", font="verdana 15", bg="white", fg="gray",command=reset)
b2.place(height=60,width=200,x=320,y=520)


b3=Button(root,borderwidth=1, relief="flat",text="UPDATE", font="verdana 15", bg="white", fg="gray",command=update)
b3.place(height=60,width=200,x=70,y=590)


b4=Button(root,borderwidth=1, relief="flat",text="DELETE", font="verdana 15", bg="white", fg="gray",command=delete)
b4.place(height=60,width=200,x=320,y=590)



c2 = Canvas(root,bg='gray',width=750,height=580)
c2.place(x=580,y=100)


tree = ttk.Treeview(root, selectmode='browse')
tree.place(height=550,width=700,x=605,y=120)

vsb = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
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




tree.delete(*tree.get_children())
con = mysql.connector.connect(host="localhost",user="root",password="",database="foresttourism")
cur = con.cursor()
cur.execute("SELECT * FROM tbladdplace")
tabledata = cur.fetchall()
cpt = 0
for row in tabledata:
    tree.insert('', 'end', text=str(cpt), values=(row[1], row[2], row[3], row[4]))
    cpt += 1 
con.commit()
con.close()
tree.bind("<<TreeviewSelect>>", edit)



mainloop()
 
