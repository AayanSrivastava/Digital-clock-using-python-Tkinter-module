from tkinter import *
from tkinter.ttk import *
from time import strftime

def time():
    string=strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000,time)

#UI for outlook
root=Tk()
root.title("Clock")


label=Label(root,font=("ds-digit",40), background="grey") #downlaod the font
label.pack(anchor='center')
time()

mainloop()