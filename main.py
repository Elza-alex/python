from tkinter import *
main=Tk()
main.title("Calculator")

operator=""
input_value=StringVar()
display_text=Entry(main,font=("arial",20,"bold"),textvariable=input_value,bd=30,insertwidth=4,bg="powder blue",justify=RIGHT)
display_text.grid(columnspan=4)

#row1
btn_7=Button(main,padx=16,fg="black",font=("arial",20,"bold"),text="7")
btn_7.grid(row=1,column=0)
btn_7=Button(main,padx=16,fg="black",font=("arial",20,"bold"),text="8")
btn_7.grid(row=1,column=1)
btn_7=Button(main,padx=16,fg="black",font=("arial",20,"bold"),text="9")
btn_7.grid(row=1,column=2)
btn_7=Button(main,padx=16,fg="black",font=("arial",20,"bold"),text="+")
btn_7.grid(row=1,column=3)

#row2
btn_7=Button(main,padx=16,fg="black",font=("arial",20,"bold"),text="4")
btn_7.grid(row=2,column=0)
btn_7=Button(main,padx=16,fg="black",font=("arial",20,"bold"),text="5")
btn_7.grid(row=2,column=1)
btn_7=Button(main,padx=16,fg="black",font=("arial",20,"bold"),text="6")
btn_7.grid(row=2,column=2)
btn_7=Button(main,padx=16,fg="black",font=("arial",20,"bold"),text="-")
btn_7.grid(row=2,column=3)

#row3
btn_7=Button(main,padx=16,fg="black",font=("arial",20,"bold"),text="1")
btn_7.grid(row=3,column=0)
btn_7=Button(main,padx=16,fg="black",font=("arial",20,"bold"),text="2")
btn_7.grid(row=3,column=1)
btn_7=Button(main,padx=16,fg="black",font=("arial",20,"bold"),text="3")
btn_7.grid(row=3,column=2)
btn_7=Button(main,padx=16,fg="black",font=("arial",20,"bold"),text="*")
btn_7.grid(row=3,column=3)

#row4
btn_7=Button(main,padx=16,fg="black",font=("arial",20,"bold"),text="0")
btn_7.grid(row=4,column=0)
btn_7=Button(main,padx=16,fg="black",font=("arial",20,"bold"),text="c")
btn_7.grid(row=4,column=1)
btn_7=Button(main,padx=16,fg="black",font=("arial",20,"bold"),text="=")
btn_7.grid(row=4,column=2)
btn_7=Button(main,padx=16,fg="black",font=("arial",20,"bold"),text="/")
btn_7.grid(row=4,column=3)













main.mainloop()