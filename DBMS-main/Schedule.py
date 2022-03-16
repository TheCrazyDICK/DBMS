
from tkinter import *
from PIL import Image,ImageTk



def Sched():

     root = Tk()
     root.title("Schedule")
     root.geometry("1920x1080")
     root.config(bg="#f6f6f6")
    
    
     image = Image.open('schedule.png')
     image2 = image.resize((1000,  700), Image.ANTIALIAS)
     my_img = ImageTk.PhotoImage(image2)
     my_lbl = Label(image = my_img) 
     my_lbl.pack()

     def logout():
         root.destroy()

        
     mbtn = Menubutton(root, text="",bg="#ffffff",bd=0, relief=RAISED)
     mbtn.place(x=960,y=75,height="16",width="10")
     mbtn.menu = Menu(mbtn, tearoff = 0)
     mbtn["menu"] = mbtn.menu
        
     pythonVar = IntVar()
     javaVar = IntVar()
     phpVar = IntVar()

     mbtn.menu.add_checkbutton(label="Profile", variable=pythonVar)
     mbtn.menu.add_checkbutton(label="Help", variable=javaVar)
     mbtn.menu.add_checkbutton(label="Logout",command=logout, variable=phpVar)

    

     root.state('zoomed')
     root.mainloop()

#Schedule()
