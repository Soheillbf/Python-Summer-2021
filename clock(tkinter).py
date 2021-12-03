from tkinter import *
import tkinter as tk
import time

top=tk.Tk()
top.config(bg='yellow')
top.geometry("300x150")
lb=Label(master=top,text="",width="30",height="2",font=("arial",26),fg="red",bg="orange")
lb.pack()
lb2=Label(master=top,text="",font=("arial",14),fg="blue",bg="yellow")
lb2.pack()

    
def Time():
    hour=time.strftime("%H")
    minute=time.strftime("%M")
    second=time.strftime("%S")
    day=time.strftime("%d")
    month=time.strftime("%B")

    lb.config(text= hour +":"+ minute +":"+ second)
    lb.after(1000,Time)
    lb2.config(text=month +"/"+ day)
if __name__=="__main__":
    Time()


