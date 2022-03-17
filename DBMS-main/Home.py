
import tkinter
from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from Schedule import *
from time import strftime


def home():

     root = Tk()
     root.title("HOME")
     root.geometry("1920x1080")
     root.config(bg="#f6f6f6")
    
    
     image = Image.open('home_bg.png')
     image = image.resize((1000,  700), Image.ANTIALIAS)
     my_img = ImageTk.PhotoImage(image)
     my_lbl = Label(image = my_img) 
     my_lbl.pack()

     def logout():
         root.destroy()
     def Sched2():
          root.destroy()
          Sched()

        
     mbtn = Menubutton(root, text="",bg="#ffffff",bd=0, relief=RAISED)
     mbtn.place(x=968,y=59,height="9",width="11")
     mbtn.menu = Menu(mbtn, tearoff = 0)
     mbtn["menu"] = mbtn.menu
        
     pythonVar = IntVar()
     javaVar = IntVar()
     phpVar = IntVar()

     mbtn.menu.add_checkbutton(label="Profile", variable=pythonVar)
     mbtn.menu.add_checkbutton(label="Help", variable=javaVar)
     mbtn.menu.add_checkbutton(label="Logout",command=logout, variable=phpVar)

     b1 = Button(root, text="Home",relief="flat")
     b1.config(bg="#5d53f1",fg="#ffffff",font=('Lucida Console',22))
     b1.place(x=32,y=119)

     b2 = Button(root, text="Students",relief="flat")
     b2.config(bg="#5d53f1",fg="#ffffff",font=('Lucida Console',18))
     b2.place(x=13,y=200)

     b3 = Button(root, text="Teachers",relief="flat")
     b3.config(bg="#5d53f1",fg="#ffffff",font=('Lucida Console',18))
     b3.place(x=14,y=280)

     b4 = Button(root, text=" Fees \nStructure",relief="flat")
     b4.config(bg="#5d53f1",fg="#ffffff",font=('Lucida Console',15))
     b4.place(x=12,y=352)

     b5 = Button(root, text="Iventory",relief="flat")
     b5.config(bg="#5d53f1",fg="#ffffff",font=('Lucida Console',18))
     b5.place(x=14,y=434)

     b6 = Button(root, text="Attendance",relief="flat")
     b6.config(bg="#5d53f1",fg="#ffffff",font=('Lucida Console',15))
     b6.place(x=12,y=516)

     b7 = Button(root, text="Schedule",command=Sched2
                 ,relief="flat")
     b7.config(bg="#5d53f1",fg="#ffffff",font=('Lucida Console',18))
     b7.place(x=14,y=596)
 
     def time():
             string = strftime('%H:%M:%S %p')
             lbl.config(text = string)
             lbl.after(1000, time)

  
     lbl = Label(root, font = ('Lucida Console', 18), background = '#f3f8ff',
                             foreground = 'black')


     lbl.place(x=825,y=500)

     time()

     root.state('zoomed')
     root.mainloop()