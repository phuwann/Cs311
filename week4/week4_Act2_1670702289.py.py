from tkinter import *

def main() :

    root = Tk()
    root.geometry("1000x700+300+100")
    root.title("Common widget: Listbox Widget")
    root.configure()
    root.columnconfigure((0,1),weight=1)
    root.rowconfigure((0,2),weight=1)
    root.rowconfigure((1),weight=3)
    return(root)

def creatframe(root):

    heading = Frame(root,bg="#384B70",)
    heading.grid(row=0,columnspan=2,sticky="news")

    left = Frame(root,bg="#578FCA",)
    left.grid(row=1,column=0,sticky="news")
    left.rowconfigure((0,1,2,3,4,5),weight=1)
    left.columnconfigure((0,1),weight=1)

    right = Frame(root,bg="#A1E3F9",)
    right.grid(row=1,column=1,sticky="news")
    right.rowconfigure((0,1),weight=1)
    right.columnconfigure(0,weight=1)


    bottom = Frame(root,bg="#384B70",)
    bottom.columnconfigure((0),weight=1)
    bottom.grid(row=2,columnspan=2,sticky="news")

    return heading,left,right,bottom


def widgets(heading,left,right,bottom):

    heading = Label(heading,text='Dream Bakery Shop by Phuwan Aiamsri',fg='#131010',bg='#578FCA',font=('comic sans ms',20,'bold'))
    heading.pack(expand=True)

    order = Label(left,image=photo1 , bg='#578FCA')
    order.grid(column=0,rowspan=2)
    order = Label(left,image=photo2, bg='#578FCA')
    order.grid(column=0,rowspan=2)
    order = Label(left,image=photo3, bg='#578FCA')  
    order.grid(column=0,rowspan=2)

    menu1 = Label( left , text = 'Chocolate Cake \nPrice 160 Bath' , fg='#131010', bg='#578FCA' , font=('comic sans ms',15  , 'bold'))
    menu1.grid(column=1,row=0,sticky=S)
    spin1 = Spinbox( left , from_=0 , to=10, justify='center' , textvariable=spy1 , command=userclick)
    spin1.grid(column=1,row=1,sticky=N)

    menu2 = Label(left,text = 'Strawberry Cake \nPrice 140 Bath',fg='#131010',bg='#578FCA',font=('comic sans ms',15  ,'bold'))
    menu2.grid(column=1,row=2,sticky=S)
    spin2 = Spinbox(left,from_=0 , to=10,justify='center',textvariable=spy2 , command=userclick)
    spin2.grid(column=1,row=3,sticky=N)

    menu3 = Label( left , text = 'Pony Donut \nPrice 75 Bath', fg='#131010' , bg='#578FCA' , font=('comic sans ms',15  , 'bold'))
    menu3.grid(column=1,row=4,sticky=S)
    spin3 = Spinbox( left , from_=0 , to=10 , justify='center' , textvariable=spy3 , command=userclick )
    spin3.grid(column=1,row=5,sticky=N)



    right1 = Label(right,text='Thank You For Your Shopping \nTotal Price is',fg='#131010',bg='#A1E3F9',font=('comic sans ms',15))
    right1.grid(row=0,sticky='news')

    total = Label(right,text='Total Price = 0.00 Bath',fg='#131010',bg='#A1E3F9',font=('comic sans ms',15))
    total.grid(row=1,sticky=N)

    btn1 = Button(bottom,text="Exit Program",compound=LEFT,bg='#C6E7FF',font=('comic sans ms',12,'bold'),command=exit)
    btn1.grid(sticky=E,ipady=10 , ipadx=10,padx=5,pady=5) 

    return total


def userclick():
    net = spy1.get()*160 + spy2.get()*140 + spy3.get()*75
    total['text'] = f"Total Price = {net:.2f} Bath"
    


root = main()

photo1 = PhotoImage(file='image\cake1.png') 
photo2 = PhotoImage(file='image\cake2.png')
photo3 = PhotoImage(file='image\cake3.png')

spy1 = IntVar()
spy2 = IntVar()
spy3 = IntVar()
net = 0

creatframe(root)
heading,left,right,bottom = creatframe(root)
total = widgets(heading,left,right,bottom)
root.mainloop()