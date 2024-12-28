from tkinter import *
from tkinter import messagebox 
import cv2
import mysql.connector
from PIL import Image
from PIL import ImageTk
import os
import sys
pyexec = sys.executable


def submit():
    if e1.get()=="":
        messagebox.showerror("Error","Enter PLACE ID",parent=root)
    elif e2.get()=="":
        messagebox.showerror("Error","Enter PLACE NAME",parent=root)
    elif e3.get()=="":
        messagebox.showerror("Error","Enter ADDRESS",parent=root)
    elif e3.get()=="":
        messagebox.showerror("Error","Enter TIMINGS",parent=root)
    else:
        
        con = mysql.connector.connect(host="localhost",user="root",password="",database="foresttourism")
        cur = con.cursor()
        cur.execute("INSERT INTO tbluser (uname,ucontact,uemail,upwd) VALUES (%s,%s,%s,%s)",(e1.get(),int(e2.get()),e3.get(),e4.get())) 
        cur.execute("SELECT * FROM tbluser")
        tabledata = cur.fetchall()

        con.commit()
        con.close()
        messagebox.showinfo("Success" , "Registered Successfully" , parent = root)


def reset():
	e1.delete(0,END)
	e2.delete(0,END)
	e3.delete(0,END)
	e4.delete(0,END)



root = Tk() 
root.title('FOREST TOURISM MANAGEMENT SYSTEM')
root.geometry('1366x768')
root.configure(background='lightgray')


var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()


c2 = Canvas(root,bg='white',width=673,height=690)
c2.place(x=2,y=2)

lmain = Label(root)
lmain.place(x=2,y=2)

img = cv2.imread('usrlg.jpg')

image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
resized_image1 = cv2.resize(image_rgb,(673,690))
imgg = Image.fromarray(resized_image1)
imgtk = ImageTk.PhotoImage(image=imgg)
lmain.imgtk = imgtk
lmain.configure(image=imgtk)

labela = Label(root,text ="ONLINE FOREST TOUR MANAGMENT SYSTEM",foreground="white",background='black',font =('Verdana',20))
labela.place(x=20,y=300)


c5 = Canvas(root,bg='white',width=673,height=690)
c5.place(x=679,y=2)

c6 = Canvas(root,bg='white',width=450,height=600,highlightthickness=1, highlightbackground="black") 
c6.place(x=790,y=50)

labelb = Label(root,text ="USER REGISTRATION",foreground="red",background='white',font =('Verdana',18))
labelb.place(x=895,y=90)

l1=Label(root,text='Name',foreground="red",background='white',font =('Verdana',13))
l1.place(x=835,y=150)
e1=Entry(root,textvariable=var1,borderwidth=2, relief="groove",font=('Verdana',12),foreground='RED',justify=LEFT)
e1.place(height=40,width=350,x=840,y=180)

l2=Label(root,text='Contact Number',foreground="red",background='white',font =('Verdana',13))
l2.place(x=835,y=230)
e2=Entry(root,textvariable=var2,borderwidth=2, relief="groove",font=('Verdana',12),foreground='RED',justify=LEFT)
e2.place(height=40,width=350,x=840,y=260)

l3=Label(root,text='Email Id',foreground="red",background='white',font =('Verdana',13))
l3.place(x=835,y=310)
e3=Entry(root,textvariable=var3,borderwidth=2, relief="groove",font=('Verdana',12),foreground='RED',justify=LEFT)
e3.place(height=40,width=350,x=840,y=340)

l4=Label(root,text='Password',foreground="red",background='white',font =('Verdana',13))
l4.place(x=835,y=390)
e4=Entry(root,textvariable=var4,borderwidth=2, relief="groove",font=('Verdana',12),foreground='RED',justify=LEFT)
e4.place(height=40,width=350,x=840,y=420)

l5=Label(root,text='Confirm Password',foreground="red",background='white',font =('Verdana',13))
l5.place(x=835,y=470)
e5=Entry(root,textvariable=var4,borderwidth=2, relief="groove",font=('Verdana',12),foreground='RED',justify=LEFT)
e5.place(height=40,width=350,x=840,y=500)


b1=Button(root,borderwidth=2, relief="flat",text="SUBMIT", font="verdana 15", bg="red", fg="white",command=submit)
b1.place(height=50,width=150,x=840,y=565)

b2=Button(root,borderwidth=2, relief="flat",text="RESET", font="verdana 15", bg="red", fg="white",command=reset)
b2.place(height=50,width=150,x=1040,y=565)

mainloop()
