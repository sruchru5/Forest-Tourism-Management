from tkinter import *
from tkinter import messagebox 
import cv2
from PIL import Image
from PIL import ImageTk
import os

def add_place():
    import addplace

def view_user():
    import viewuser

def view_bookings():
    import viewbookings

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

b1=Button(root,borderwidth=2, relief="flat",text="ADD PLACES", font="verdana 15", bg="red", fg="white",command=add_place)
b1.place(height=150,width=200,x=930,y=50)

b2=Button(root,borderwidth=2, relief="flat",text="VIEW USER", font="verdana 15", bg="red", fg="white",command=view_user)
b2.place(height=150,width=200,x=930,y=280)

b2=Button(root,borderwidth=2, relief="flat",text="VIEW BOOKINGS", font="verdana 15", bg="red", fg="white",command=view_bookings)
b2.place(height=150,width=200,x=930,y=500)

mainloop()
