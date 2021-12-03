from tkinter import *
import sqlite3
import math,random,os
from tkinter import messagebox
class Softwarica_Petrol_pump:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1400x720+0+0")
        self.root.title("Softawrica Petrol Pump")
        bg_color = "#143875"

        # Frame1 Customer Detail Frame 
        F1 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0, y=0, relwidth=1)

        # Frame1 Customer Details Variable types
        self.name=StringVar()
        self.phone=StringVar()
        self.bill=StringVar()
        x=random.randint(0000,9000)
        self.bill.set(str(x))
        self.search_bill=StringVar()
        
        name_lbl=Label(F1, text="Name: ", bg=bg_color, fg="white", font=("times new roman",18,"bold")).grid(row=0, column=0, padx=20, pady=5)
        name_txt=Entry(F1,width=20, bd=7, relief=SUNKEN,textvariable=self.name ,font="arial 15").grid(row=0,column=1,pady=5,padx=10)

        phone_lbl = Label(F1, text="Phone No.", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        phone_txt = Entry(F1, width=18,bd=7,relief=SUNKEN,textvariable=self.phone ,font="arial 15").grid(row=0, column=3, pady=5, padx=10)

        bill_lbl = Label(F1, text="Bill No.", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        billtxt = Entry(F1, width=10,bd=7,relief=SUNKEN,textvariable=self.bill, font="arial 15").grid(row=0, column=5, pady=5, padx=10)
        
        search_btn=Button(F1,text="Search",width=10,bd=7,relief=GROOVE, font="arial 12 bold").grid(row=0, column=6,padx=10,pady=0)

        # Frame2  Snack items
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Petrol",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5, y=90,width=325,height=530)

        
    
root = Tk()
obj = Softwarica_Petrol_pump(root)
root.mainloop()