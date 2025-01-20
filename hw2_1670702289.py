from tkinter import *

def mainwindow() :
    
    master = Tk()
    master.wm_geometry("700x700+300+100")
    master.wm_title("Week2 : Activity by Phuwan")
    master.configure(bg="#384B70")
    master.option_add('*font','Poppins 16')

    master.rowconfigure((0,6),weight=2) 
    master.rowconfigure((1,2,3,4,5),weight=1) 

    master.columnconfigure((0,1),weight=1)
    return(master)

def widget(master) : 

    heading = Label(master,text="Registration Form",font=('Poppins',22,'bold'),bg="#384B70",fg='#ffffff')
    heading.grid(row=0,columnspan=2)

    userlabel = Label(master,text="Name : ",bg="#384B70" , fg="#ffffff")
    userlabel.grid(row=1,column=0,sticky=E)

    pwdlabel = Label(master,text="Student ID : ",bg="#384B70", fg="#ffffff")
    pwdlabel.grid(row=2,column=0,sticky=E)

    dplabel = Label(master,text="Department : ",bg="#384B70", fg="#ffffff")
    dplabel.grid(row=3,column=0,sticky=E)

    sqlabel = Label(master,text="Security Question : ",bg="#384B70", fg="#ffffff")
    sqlabel.grid(row=4,column=0,sticky=E)

    userbox = Entry(master,width=20 , bg="#507687",fg="#ffffff")
    userbox.grid(row=1,column=1,sticky=W)

    pwdbox = Entry(master,width=20, bg="#507687",fg="#ffffff")
    pwdbox.grid(row=2,column=1,sticky=W,)

    dpbox = Entry(master,width=20 , bg="#507687",fg="#ffffff")
    dpbox.grid(row=3,column=1,sticky=W)

    sqbox = Entry(master,width=20 , bg="#507687",fg="#ffffff")
    sqbox.grid(row=4,column=1,sticky=W)

    btn1 = Button(master,text="CANCEL",width=10 ,bg="#FCFAEE")
    btn1.grid(row=5,column=0,sticky=NE,ipady=8,padx=5)    

    btn2 = Button(master,text="REGISTER",width=10 ,bg="#FCFAEE")
    btn2.grid(row=5,column=1,sticky=NW,ipady=8,padx=5)

    end = Label(master,text="Created by Phuwan Aiamsri, Id : 1670702289",font=('Poppins',18,'bold'),bg="#384B70",fg='#507687')
    end.grid(row=6,columnspan=2,sticky=N)

master = mainwindow()
widget(master)
master.mainloop()