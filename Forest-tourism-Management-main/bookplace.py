from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import mysql.connector
from tkinter import ttk, messagebox
import tkinter.filedialog
from tkcalendar import Calendar, DateEntry

def home():
    import addplace
    


def reset():
	e1.delete(0,END)
	e3.delete(0,END)
	e4.delete(0,END)
	e5.delete(0,END)



def submit():
    tree.delete(*tree.get_children())
    if e1.get()=="":
        messagebox.showerror("Error","Enter BOOKING ID",parent=root)
    elif e3.get()=="":
        messagebox.showerror("Error","Enter PLACE NAME",parent=root)
    elif e4.get()=="":
        messagebox.showerror("Error","Enter DATE",parent=root)
    elif e5.get()=="":
        messagebox.showerror("Error","Enter NO OF PEOPLE",parent=root)
    else:
        
        con = mysql.connector.connect(host="localhost",user="root",password="",database="foresttourism")
        cur = con.cursor()
        print(c2.get())
        cur.execute("INSERT INTO tblbooking (bookid,placeid,placename,ddate,noppl,usrid) VALUES (%s,%s,%s,%s,%s,%s)",(e1.get(),c1.get(),e3.get(),e4.get(),e5.get(),c2.get()))
        cur.execute("SELECT * FROM tblbooking")
        tabledata = cur.fetchall()
        cpt = 0
        for row in tabledata:
            tree.insert('', 'end', text=str(cpt), values=(row[1], row[2], row[3], row[4], row[5],row[6]))
            cpt += 1 
        con.commit()
        con.close()
    e1.configure(state='normal')
    e1.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    print(c2.get())



def edit(a):
    e1.configure(state='normal')
    e1.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)


    selectedItem = tree.selection()[0]
    e1.insert(0, tree.item(selectedItem)['values'][0])
    e1.configure(state='disabled')
    e3.insert(0, tree.item(selectedItem)['values'][2])
    e4.insert(0, tree.item(selectedItem)['values'][3])
    e5.insert(0, tree.item(selectedItem)['values'][4])



def update():
    tree.delete(*tree.get_children())
    con = mysql.connector.connect(host="localhost",user="root",password="",database="foresttourism")
    cur = con.cursor()
    cur.execute("UPDATE tblbooking SET placeid='%s',placename='%s',ddate='%s',noppl='%s',usrid='%s' WHERE bookid = '%s' " %(c1.get(),e3.get(),e4.get(),e5.get(),c2.get(),e1.get()))
    cur.execute("SELECT * FROM tblbooking")
    tabledata = cur.fetchall()
    cpt = 0
    for row in tabledata:
        tree.insert('', 'end', text=str(cpt), values=(row[1], row[2], row[3], row[4], row[5],row[6]))
        cpt += 1 

    con.commit()
    con.close()
    e1.configure(state='normal')
    e1.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)



def delete():
    tree.delete(*tree.get_children())
    con = mysql.connector.connect(host="localhost",user="root",password="",database="foresttourism")
    cur = con.cursor()
    cur.execute("DELETE from tblbooking WHERE bookid = '%s' " %(e1.get()))
    cur.execute("SELECT * FROM tblbooking")
    tabledata = cur.fetchall()
    cpt = 0
    for row in tabledata:
        tree.insert('', 'end', text=str(cpt), values=(row[1], row[2], row[3], row[4], row[5],row[6]))
        cpt += 1 

    con.commit()
    con.close()
    e1.configure(state='normal')
    e1.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)


def get_index(*arg):
    e3.delete(0,END)
    e3.insert(0, results_for_combobox2[c1.current()])


    

root = Tk()
root.title('BOOK TOURIST FOREST PLACE')
root.geometry('1366x768')
root.state('zoomed')


var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()
var5=StringVar()
var6=StringVar()

Label(root,text='BOOK TOURIST FOREST PLACE',foreground="red",font=('Verdana',20,'bold')).pack(side=TOP,pady=10)



c1 = Canvas(root,bg='gray',width=500,height=580)
c1.place(x=50,y=100)




l0=Label(root,text='BOOKING DETAILS',foreground="white",background='gray',font =('Verdana',13,'bold'))
l0.place(x=225,y=120)

l1=Label(root,text='BOOKING ID',foreground="white",background='gray',font =('Verdana',13,'bold'))
l1.place(x=70,y=180)
e1=Entry(root,textvariable=var1,font=('Verdana',12,'bold'),foreground='RED',justify=LEFT)
e1.place(height=40,width=200,x=72,y=210)


l3=Label(root,text='PLACE NAME',foreground="white",background='gray',font =('Verdana',13,'bold'))
l3.place(x=70,y=340)
e3=Entry(root,textvariable=var3,font=('Verdana',12,'bold'),foreground='RED',justify=LEFT)
e3.place(height=40,width=450,x=72,y=370)



l4=Label(root,text='DATE',foreground="white",background='gray',font =('Verdana',13,'bold'))
l4.place(x=70,y=420)
e4=DateEntry(root,textvariable=var4,font=('Verdana',12,'bold'),foreground='RED',justify=LEFT)
e4.place(height=40,width=450,x=72,y=450)



l5=Label(root,text='NO OF PEOPLE',foreground="white",background='gray',font =('Verdana',13,'bold'))
l5.place(x=70,y=500)
e5=Entry(root,textvariable=var5,font=('Verdana',12,'bold'),foreground='RED',justify=LEFT)
e5.place(height=40,width=450,x=72,y=530)




b1=Button(root,borderwidth=1, relief="flat",text="SUBMIT", font="verdana 15", bg="white", fg="gray",command=submit)
b1.place(height=30,width=200,x=73,y=590)

b2=Button(root,borderwidth=1, relief="flat",text="RESET", font="verdana 15", bg="white", fg="gray",command=reset)
b2.place(height=30,width=200,x=320,y=590)

b3=Button(root,borderwidth=1, relief="flat",text="UPDATE", font="verdana 15", bg="white", fg="gray",command=update)
b3.place(height=30,width=200,x=73,y=630)

b4=Button(root,borderwidth=1, relief="flat",text="DELETE", font="verdana 15", bg="white", fg="gray",command=delete)
b4.place(height=30,width=200,x=320,y=630)


c2 = Canvas(root,bg='gray',width=750,height=580)
c2.place(x=580,y=100)


tree = ttk.Treeview(root, selectmode='browse')
tree.place(height=550,width=700,x=605,y=120)

vsb = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
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
tree.heading("6", text="USER NAME")

tree.delete(*tree.get_children())
con = mysql.connector.connect(host="localhost",user="root",password="",database="foresttourism")
cur = con.cursor()
cur.execute("SELECT * FROM tblbooking")
tabledata = cur.fetchall()
cpt = 0
for row in tabledata:
    tree.insert('', 'end', text=str(cpt), values=(row[1], row[2], row[3], row[4],row[5],row[6]))
    cpt += 1 
con.commit()
con.close()
tree.bind("<<TreeviewSelect>>", edit)


con = mysql.connector.connect(host="localhost",user="root",password="",database="foresttourism")
cur = con.cursor()
cur.execute("SELECT * FROM tbladdplace")
tabledat = cur.fetchall()
results_for_combobox1 = [result[1] for result in tabledat]
results_for_combobox2 = [result[2] for result in tabledat]

cur.execute("SELECT * FROM tbluser")
tabledati = cur.fetchall()
results_for_combobox3 = [result[1] for result in tabledati]
    
con.commit()
con.close()


l2=Label(root,text='PLACE ID',foreground="white",background='gray',font =('Verdana',13,'bold'))
l2.place(x=70,y=260)
c1 = ttk.Combobox(root,textvariable=var2,font=('Verdana',12,'bold'),foreground='RED',justify=LEFT)
c1.place(height=40,width=450,x=72,y=290)
c1['values'] = results_for_combobox1
c1.current(0)

l3=Label(root,text='USER NAME',foreground="white",background='gray',font =('Verdana',13,'bold'))
l3.place(x=318,y=180)
c2 = ttk.Combobox(root,textvariable=var6,font=('Verdana',12,'bold'),foreground='RED',justify=LEFT)
c2.place(height=40,width=200,x=320,y=210)
c2['values'] = results_for_combobox3
c2.current(0)



var2.trace('w', get_index)

mainloop()
 
