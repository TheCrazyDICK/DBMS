
import tkinter
from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk



def pwd():

     root = Tk()
     root.title("Forgot Password")
     root.geometry("1920x1080")
     root.config(bg="#f6f6f6")
    
    
     image = Image.open('finalfpwd1.jpg')
     image = image.resize((1000,  700), Image.ANTIALIAS)
     my_img = ImageTk.PhotoImage(image)
     my_lbl = Label(image = my_img) 
     my_lbl.pack()

     b1 = Button( root,text="Back",bg="#f6f6f6",fg="Black",relief="flat",font=('Arial', 20))
     b1.place(x=1440,y=40,height=50,width=80)

     l1 = Label( root,text="Forgot Password",bg="#f6f6f6",fg="Black", font=('Arial', 30))
     l1.place(x=500,y=20,height=110,width=500)

     l2 = Label( root,text="Enter your Admission Number ",bg="#f6f6f6",fg="Black", font=('Arial', 18))
     l2.place(x=325,y=240,height="50",width="450")

     e1 = Entry( root,text="",bg='#EFEFEF',relief="flat")
     e1.place(x=325,y=320,height="50",width="300")

     b2 = Button( root,text="CONTINUE",bg="#7028c6",fg="#FFFFFF",relief="flat",font=('Arial', 11))
     b2.place(x=650,y=415,height="40",width="160")


     root.state('zoomed')
     root.mainloop()




