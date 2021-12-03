
import tkinter as tk
top=tk.Tk()
def changecounter():
    global counter
    lbcounter.config(text=str(counter))
    
def inc():
    global counter
    counter+=1
    changecounter()
def dec():
    global counter
    counter-=1
    changecounter()
counter=0

frmbala=tk.Frame(master=top)
frmbala.pack()
frmpayeen=tk.Frame(master=top)
frmpayeen.pack()

btmin=tk.Button(master=frmbala,text="-",font=("arial",40),width=4,fg="blue",bg="yellow",command=dec)
btmin.grid(row=0,column=0)
btplus=tk.Button(master=frmbala,text="+",font=("arial",40),width=4,fg="red",bg="yellow",command=inc)
btplus.grid(row=0,column=2)
lbcounter=tk.Label(master=frmbala,text="0",font=("arial",40))
lbcounter.grid(row=0,column=1)
btexit=tk.Button(master=frmpayeen,text="Exit",font=("arial",40),width=4,fg="green",bg="black",command=top.destroy)
btexit.pack()
top.mainloop()
