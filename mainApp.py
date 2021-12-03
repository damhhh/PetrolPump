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
    def total(self):   
        self.petrol_price=self.petrol.get()*100
        self.Kerosene_price = self.Kerosene.get()*30
        self.Diesel_price = self.Diesel.get()*190

    
        self.total_bill=float(       
                self.petrol_price +
                self.Kerosene_price +
                self.Diesel_price
        )

        
        self.total_price.set("NRs. "+str(self.total_bill))

    def welcome_bill(self):
            self.txtarea.delete('1.0',END)
            self.txtarea.insert(END,"\tSoftwarica Petrol Pump")
            self.txtarea.insert(END,f"\n Bill Number:{self.bill.get()} ")
            self.txtarea.insert(END,f"\n Name: {self.name.get()}") 
            self.txtarea.insert(END,f"\n Phone Number:{self.phone.get()} ")
            self.txtarea.insert(END,f"\n =====================================")
            self.txtarea.insert(END,"\n Fuel\t\tQTY \t\tPrice")
            self.txtarea.insert(END,f"\n =====================================")
            
    
    def bill_area(self):
            if self.name.get()== "" or self.phone.get()=="":
                    messagebox.showerror("Error", "Customer details are must")
            elif self.total_price.get() =="NRs. 0.0" :
                    messagebox.showerror("Error", "No items selected")
            else:
                self.welcome_bill()
                if self.petrol.get() !=0:
                    self.txtarea.insert(END,f"\n Petrol\t\t{self.petrol.get()}\t\t{self.petrol_price}")
                if self.Kerosene.get()!=0:
                    self.txtarea.insert(END,f"\n Keroseme\t\t{self.Kerosene.get()}\t\t{self.Kerosene_price}")
                if self.Diesel.get()!=0:
                    self.txtarea.insert(END,f"\n Diesel\t\t{self.Diesel.get()}\t\t{self.Diesel_price}")
                self.txtarea.insert(END,f"\n -------------------------------------")
                self.txtarea.insert(END,f"\n Total Bill : \t\tRs. {str(self.total_bill)} ")
                
                self.db()

    
    def clear(self):
        op = messagebox.askyesno("Clear", "Do you want to clear the data? ")
        if op > 0:
                self.petrol.set(0)
                self.Kerosene.set(0)
                self.Diesel.set(0)
                self.name.set("") 
                self.phone.set("")
                self.total_price.set(0.00)
            
    
    def exit(self):
        op = messagebox.askyesno("Exit", "Do you want to exit? ")
        if op > 0:
            self.root.destroy()
        else:
            return
    
    
    
    def db(self):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS customer_data(bill TEXT, name TEXT,phone TEXT, total TEXT)")
        c.execute('INSERT INTO customer_data (bill,name,phone,total) VALUES (?,?,?,?)', (self.bill.get(), self.name.get(),self.phone.get(), self.total_price.get()))
        conn.commit()
        conn.close()
        

        
    
root = Tk()
obj = Softwarica_Petrol_pump(root)
root.mainloop()