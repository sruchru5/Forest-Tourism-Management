from tkinter import *
from tkinter import messagebox 
import cv2
from PIL import Image
from PIL import ImageTk
import mysql.connector
import os
import sys

pyexec = sys.executable

def reset():
	adminid_entry.delete(0,END)
	pwd_entry.delete(0,END)


def login():
        if e1.get()=="" or e2.get()=="":
                messagebox.showerror("Error","Enter Admin ID And Password",parent=master)       
        else:
                con = mysql.connector.connect(host="localhost",user="root",password="",database="foresttourism")
                cur = con.cursor()
                cur.execute("select * from tbladminlogin where username=%s and pwd = %s",(e1.get(),e2.get()))
                row = cur.fetchone()
                if row==None:
                        messagebox.showerror("Error" , "Invalid Admin ID And Password", parent = root)

                else:
                        messagebox.showinfo("Success" , "Login Successfully" , parent = root)
                        root.quit()
                        root.destroy()
                        exec(open("./admindashboard.py").read())
                con.close()



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

c6 = Canvas(root,bg='white',width=450,height=350,highlightthickness=1, highlightbackground="black") 
c6.place(x=790,y=180)

labelb = Label(root,text ="ADMIN LOGIN",foreground="red",background='white',font =('Verdana',20))
labelb.place(x=930,y=200)

l1=Label(root,text='Name',foreground="red",background='white',font =('Verdana',13))
l1.place(x=835,y=250)
e1=Entry(root,textvariable=var1,borderwidth=2, relief="groove",font=('Verdana',12),foreground='RED',justify=LEFT)
e1.place(height=50,width=350,x=840,y=280)

l2=Label(root,text='Password',foreground="red",background='white',font =('Verdana',13))
l2.place(x=835,y=350)
e2=Entry(root,show='*',textvariable=var2,borderwidth=2, relief="groove",font=('Verdana',12),foreground='RED',justify=LEFT)
e2.place(height=50,width=350,x=840,y=380)


b1=Button(root,borderwidth=2, relief="flat",text="LOGIN", font="verdana 15", bg="red", fg="white",command=login)
b1.place(height=60,width=150,x=840,y=450)

b2=Button(root,borderwidth=2, relief="flat",text="RESET", font="verdana 15", bg="red", fg="white",command=reset)
b2.place(height=60,width=150,x=1040,y=450)

mainloop()
