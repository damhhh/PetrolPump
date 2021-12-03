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

        # Frame2 items
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Petrol",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5, y=90,width=325,height=530)
	
	
        #  Variable types
        self.petrol=IntVar()


        f2_lbl1=Label(F2,text="Petrol",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0, column=0,padx=10,pady=7,sticky="w")
        f2_txt1=Entry(F2,width=8,textvariable=self.petrol,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=7)

       
        # For 

        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Kerosene",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=335, y=90,width=375,height=530)

        self.Kerosene=IntVar()


        f3_lbl1=Label(F3,text="Kerosene",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0, column=0,padx=10,pady=7,sticky="w")
        f3_txt1=Entry(F3,width=8,textvariable=self.Kerosene ,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=7)
	
# Frame 4 Items

        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Diesel",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=710, y=90,width=325,height=530)

        # Local food items Variable types
        self.Diesel=IntVar()


        f4_lbl1=Label(F4,text="Diesel",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=0, column=0,padx=10,pady=7,sticky="w")
        f4_txt1=Entry(F4,width=8, textvariable=self.Diesel, font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=7)




# Frame 5 Bill Area

        F5=Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1040, y=90, width=350, height=530)
        bill_title = Label(F5, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)

        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)


# Frame6 Bill Menu

        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=("times new roman", 15, "bold"), fg="gold",bg=bg_color)
        F6.place(x=0, y=620, relwidth=1, height=95)

        self.total_price=StringVar()

        total_price_lbl=Label(F6,text="Total price: ",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0, column=0, padx=5,pady=1,sticky="w")
        total_price_txt=Entry(F6, width=18, textvariable=self.total_price, font="arial 15 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=9,pady=1)

        Label(F6, text="        ",bg=bg_color).grid(row=0, column=2, padx=50, pady=0)  # adding empty space


        Total_btn= Button(F6,text="Total",command=self.total, bg="white",fg="black",width=8,bd=7,font=("arial 14 bold")).grid(row=0, column=3, padx=10, pady=0)
        
        Generate_Bill_btn= Button(F6, text="Generate Bill",command=self.bill_area, bg="white",width=10, fg="black",bd=7, font=("arial 14 bold")).grid(row=0, column=4, padx=10, pady=0)

        Clear_btn = Button(F6, text="Clear",command=self.clear, bg="white", fg="black",width=8,bd=7,  font=("arial 14 bold")).grid(row=0, column=5, padx=10, pady=0)

        Exit_btn=Button(F6, text="Exit",command = self.exit, bg="white", fg="black",width=8,bd=7, font=("arial 14 bold")).grid(row=0, column=6, padx=10, pady=0)
        self.welcome_bill()


        
    
root = Tk()
obj = Softwarica_Petrol_pump(root)
root.mainloop()