from tkinter import*


root=Tk()
root.title("Bill Management")
root.resizable(False,False)

def Reset():
    entry_dosa.delete(0,END)
    entry_cookies.delete(0,END)
    entry_tea.delete(0,END)
    entry_coffee.delete(0,END)
    entry_pancakes.delete(0,END)
    entry_cake.delete(0,END)
    entry_egg.delete(0,END)
    entry_juice.delete(0,END)

def Total():
    try:a1=int(Dosa.get())
    except:a1=0

    try:a2=int(Cookies.get())
    except:a2=0

    try:a3=int(Tea.get())
    except:a3=0

    try:a4=int(Coffee.get())
    except:a4=0

    try:a5=int(Pancakes.get())
    except:a5=0

    try:a6=int(Cake.get())
    except:a6=0

    try:a7=int(Egg.get())
    except:a7=0

    try:a8=int(Juice.get())
    except:a8=0

    #define cost of each item per quantity
    c1=60*a1
    c2=10*a2
    c3=15*a3
    c4=12*a4
    c5=20*a5
    c6=250*a6
    c7=8*a7
    c8=50*a8

    lbl_total=Label(f2,font=("arial",20,"bold"),text="Total",width=16,fg="Lightyellow",bg="black")
    lbl_total.place(x=0,y=100)

    entry_total=Label(f2,font=("arial",20,"bold"),textvariable=Total_bill,bd=6,width=15,fg="lightgreen")
    entry_total.place(x=20,y=200)

    totalcost=c1+c2+c3+c4+c5+c6+c7+c8
    string_bill="Rs.",str("%.2f"%totalcost)
    Total_bill.set(string_bill)

Label(text="BILL MANAGEMENT",bg="black",fg="white",font=("calbri",33),width="300",height="2").pack()

#Menu Card
f=Frame(root,bg="light green",highlightbackground="black",highlightthickness=1,width=500,height=570)
f.place(x=10,y=118)

Label(f,text="Menu",font=("Gabriola",40,"bold"),fg="black",bg="light green").place(x=80,y=0)

Label(f,font=("Lucida Calligraphy",15,"bold"),text="Dosa...............Rs.60/plate",fg="black",bg="lightgreen").place(x=10,y=100)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Cookies...............Rs.10/plate",fg="black",bg="lightgreen").place(x=10,y=130)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Tea...............Rs.15/plate",fg="black",bg="lightgreen").place(x=10,y=160)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Coffee...............Rs.12/plate",fg="black",bg="lightgreen").place(x=10,y=190)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Pancakes...............Rs.20/plate",fg="black",bg="lightgreen").place(x=10,y=210)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Cake...............Rs.250/plate",fg="black",bg="lightgreen").place(x=10,y=240)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Egg...............Rs.8/plate",fg="black",bg="lightgreen").place(x=10,y=270)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Juice...............Rs.50/plate",fg="black",bg="lightgreen").place(x=10,y=300)

#bill
f2=Frame(root,bg="Light Yellow",highlightbackground="black",highlightthickness=1,width=300,height=370)
f2.place(x=490,y=88)

Bill=Label(f2,text="Bill",font=("Calbri",20),bg="lightyellow")
Bill.place(x=120,y=10)

#Entry Work
f1=Frame(root,bd=5,height=270,width=200,relief=RAISED)
f1.pack()

Dosa=StringVar()
Cookies=StringVar()
Tea=StringVar()
Coffee=StringVar()
Pancakes=StringVar()
Cake=StringVar()
Egg=StringVar()
Juice=StringVar()
Total_bill=StringVar()

#Label
lbl_dosa=Label(f1,font=("arial",20,"bold"),text="Dosa",width=12,fg="blue")
lbl_cookies=Label(f1,font=("arial",20,"bold"),text="Cookies",width=12,fg="blue")
lbl_tea=Label(f1,font=("arial",20,"bold"),text="Tea",width=12,fg="blue")
lbl_coffee=Label(f1,font=("arial",20,"bold"),text="Coffee",width=12,fg="blue")
lbl_pancakes=Label(f1,font=("arial",20,"bold"),text="Pancakes",width=12,fg="blue")
lbl_cake=Label(f1,font=("arial",20,"bold"),text="Cake",width=12,fg="blue")
lbl_egg=Label(f1,font=("arial",20,"bold"),text="Egg",width=12,fg="blue")
lbl_juice=Label(f1,font=("arial",20,"bold"),text="Juice",width=12,fg="blue")

lbl_dosa.grid(row=1,column=0)
lbl_cookies.grid(row=2,column=0)
lbl_tea.grid(row=3,column=0)
lbl_coffee.grid(row=4,column=0)
lbl_pancakes.grid(row=5,column=0)
lbl_cake.grid(row=6,column=0)
lbl_egg.grid(row=7,column=0)
lbl_juice.grid(row=8,column=0)

entry_dosa=Entry(f1,font=("arial",20,"bold"),textvariable=Dosa,bd=6,width=8,fg="lightpink")
entry_cookies=Entry(f1,font=("arial",20,"bold"),textvariable=Cookies,bd=6,width=8,fg="lightpink")
entry_tea=Entry(f1,font=("arial",20,"bold"),textvariable=Tea,bd=6,width=8,fg="lightpink")
entry_coffee=Entry(f1,font=("arial",20,"bold"),textvariable=Coffee,bd=6,width=8,fg="lightpink")
entry_pancakes=Entry(f1,font=("arial",20,"bold"),textvariable=Pancakes,bd=6,width=8,fg="lightpink")
entry_cake=Entry(f1,font=("arial",20,"bold"),textvariable=Cake,bd=6,width=8,fg="lightpink")
entry_egg=Entry(f1,font=("arial",20,"bold"),textvariable=Egg,bd=6,width=8,fg="lightpink")
entry_juice=Entry(f1,font=("arial",20,"bold"),textvariable=Juice,bd=6,width=8,fg="lightpink")

entry_dosa.grid(row=1,column=1)
entry_cookies.grid(row=2,column=1)
entry_tea.grid(row=3,column=1)
entry_coffee.grid(row=4,column=1)
entry_pancakes.grid(row=5,column=1)
entry_cake.grid(row=6,column=1)
entry_egg.grid(row=7,column=1)
entry_juice.grid(row=8,column=1)

#buttons
btn_reset=Button(f1,bd=5,fg="black",bg="lightblue",font=("arial",16,"bold"),width=10,text="Reset",command=Reset)
btn_reset.grid(row=9,column=0)

btn_total=Button(f1,bd=5,fg="black",bg="lightblue",font=("arial",16,"bold"),width=10,text="Total",command=Total)
btn_total.grid(row=9,column=1)

root.mainloop()
