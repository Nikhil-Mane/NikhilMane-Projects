from tkinter import *
from tkinter import messagebox
import os
import requests
class billing_system:
                
        def __init__(self,root):

                self.root=root
                self.root.geometry("1525x790+0+0")
                self.root.title("billing management system")
                bg_color="#074463"
                self.root.configure(bg=bg_color)
                ########################## variable for entry ##############################
                ################## for  customer details variables ############
                self.c_name=StringVar()
                self.c_phone=StringVar()
                self.c_bill=StringVar()
                ################## for  cosmetics variables ############
                self.soap=IntVar()
                self.fracecreame=IntVar()
                self.fw=IntVar()
                self.hs=IntVar()
                self.HG=IntVar()
                self.BL=IntVar()
                ################## for  Glossary variables ############
                self.rice=IntVar()
                self.oil=IntVar()
                self.daal=IntVar()
                self.wheat=IntVar()
                self.sugar=IntVar()
                self.tea=IntVar()
                ################## for  cold Drinks variables ############
                self.Tu=IntVar()
                self.s=IntVar()
                self.P=IntVar()
                self.RB=IntVar()
                self.Coca=IntVar()
                self.soda=IntVar()
                ################## for  price variables ############
                self.tcp=StringVar()
                self.tgp=StringVar()
                self.tcdp=StringVar()

                ################## for  tax variables ############
                self.tcpt=StringVar()
                self.tgpt=StringVar()
                self.tcdpt=StringVar()
                self.title=Label(self.root,text="Billing software",font=("times new roman",24,"bold"),bg=bg_color,fg="white",bd=12,relief=GROOVE).pack(fill=X)
        ###################################### customer details#######################
                f1=LabelFrame(self.root,text="Customer Details",font=("times new roman",22,"bold"),bg=bg_color,fg="red",bd=12,relief=GROOVE)
                f1.place(x=0,y=60,relwidth=1,height=130)
                self.cname=Label(f1,text="Customer Name",font=("times new roman",20,"bold"),bg=bg_color,fg="yellow").grid(row=0,column=0,padx=10,pady=10)
                self.cname_txt=Entry(f1,width=15,textvariable=self.c_name,bd=5,relief=SUNKEN,font=("times new roman",20,"bold")).grid(row=0,column=1,padx=10,pady=10)
                
                self.cphone=Label(f1,text="Phone No.",font=("times new roman",20,"bold"),bg=bg_color,fg="yellow").grid(row=0,column=2,padx=10,pady=10)
                self.cphone_txt=Entry(f1,width=15,textvariable=self.c_phone,bd=5,relief=SUNKEN,font=("times new roman",20,"bold")).grid(row=0,column=3,padx=10,pady=10)
                
                self.cbill=Label(f1,text="Billing No.",font=("times new roman",20,"bold"),bg=bg_color,fg="yellow").grid(row=0,column=4,padx=10,pady=10)
                self.cbill_txt=Entry(f1,width=15,textvariable=self.c_bill,bd=5,relief=SUNKEN,font=("times new roman",20,"bold")).grid(row=0,column=5,padx=10,pady=10)

                self.bill_button=Button(f1,text="Search",command=self.search_bills,width=10,font=("times new roman",20,"bold"),bg="white",fg="black",bd=10).grid(row=0,column=6,padx=40,pady=10)

        ###################################### cosmatics#######################
                f2=LabelFrame(self.root,text="Cosmatics",font=("times new roman",22,"bold"),bg=bg_color,fg="red",bd=12,relief=GROOVE)
                f2.place(x=0,y=195,width=400,height=430)
                self.bath_soap=Label(f2,text="Bath Soap",font=("times new roman",20,"bold"),bg=bg_color,fg="yellow").grid(row=0,column=0,padx=10,pady=10)
                self.bath_soap_txt=Entry(f2,width=10,textvariable=self.soap,bd=5,relief=SUNKEN,font=("times new roman",20,"bold")).grid(row=0,column=1,padx=10,pady=10)
                
                self.face_cream=Label(f2,text="Face Creame",font=("times new roman",20,"bold"),bg=bg_color,fg="yellow").grid(row=1,column=0,padx=10,pady=10)
                self.face_cream_txt=Entry(f2,width=10,bd=5,textvariable=self.fracecreame,relief=SUNKEN,font=("times new roman",20,"bold")).grid(row=1,column=1,padx=10,pady=10)

                self.face_wash=Label(f2,text="Face Wash",font=("times new roman",20,"bold"),bg=bg_color,fg="yellow").grid(row=2,column=0,padx=10,pady=10)
                self.face_wash_txt=Entry(f2,width=10,bd=5,textvariable=self.fw,relief=SUNKEN,font=("times new roman",20,"bold")).grid(row=2,column=1,padx=10,pady=10)
                
                self.hair_spray=Label(f2,text="Hair Spray",font=("times new roman",20,"bold"),bg=bg_color,fg="yellow").grid(row=3,column=0,padx=10,pady=10)
                self.hair_s_txt=Entry(f2,width=10,bd=5,textvariable=self.hs,relief=SUNKEN,font=("times new roman",20,"bold")).grid(row=3,column=1,padx=10,pady=10)

                self.hair_Gell=Label(f2,text="Hair Gell",font=("times new roman",20,"bold"),bg=bg_color,fg="yellow").grid(row=4,column=0,padx=10,pady=10)
                self.heir_gell_txt=Entry(f2,width=10,bd=5,textvariable=self.HG,relief=SUNKEN,font=("times new roman",20,"bold")).grid(row=4,column=1,padx=10,pady=10)

                self.body_loshan=Label(f2,text="Body Loshan",font=("times new roman",20,"bold"),bg=bg_color,fg="yellow").grid(row=5,column=0,padx=10,pady=10)
                self.body_loshan_txt=Entry(f2,width=10,bd=5,textvariable=self.BL,relief=SUNKEN,font=("times new roman",20,"bold")).grid(row=5,column=1,padx=10,pady=10)

                ###################################### GLOSSARY  #######################
                f3=LabelFrame(self.root,text="Glossary",font=("times new roman",22,"bold"),bg=bg_color,fg="red",bd=12,relief=GROOVE)
                f3.place(x=405,y=195,width=360,height=430)
                self.Rice=Label(f3,text="Rice",font=("times new roman",20,"bold"),bg=bg_color,fg="yellow").grid(row=0,column=0,padx=10,pady=10)
                self.rice_txt=Entry(f3,width=10,bd=5,textvariable=self.rice,relief=SUNKEN,font=("times new roman",20,"bold")).grid(row=0,column=1,padx=10,pady=10)
                
                self.food_oil=Label(f3,text="Food Oil",font=("times new roman",20,"bold"),bg=bg_color,fg="yellow").grid(row=1,column=0,padx=10,pady=10)
                self.food_oil_txt=Entry(f3,width=10,bd=5,textvariable=self.oil,relief=SUNKEN,font=("times new roman",20,"bold")).grid(row=1,column=1,padx=10,pady=10)

                self.Daal=Label(f3,text="Daal",font=("times new roman",20,"bold"),bg=bg_color,fg="yellow").grid(row=2,column=0,padx=10,pady=10)
                self.Daal_txt=Entry(f3,width=10,bd=5,textvariable=self.daal,relief=SUNKEN,font=("times new roman",20,"bold")).grid(row=2,column=1,padx=10,pady=10)
                
                self.Wheat=Label(f3,text="Wheat",font=("times new roman",20,"bold"),bg=bg_color,fg="yellow").grid(row=3,column=0,padx=10,pady=10)
                self.Wheat_txt=Entry(f3,width=10,bd=5,textvariable=self.wheat,relief=SUNKEN,font=("times new roman",20,"bold")).grid(row=3,column=1,padx=10,pady=10)

                self.Sugar=Label(f3,text="Sugar",font=("times new roman",20,"bold"),bg=bg_color,fg="yellow").grid(row=4,column=0,padx=10,pady=10)
                self.Sugar_txt=Entry(f3,width=10,bd=5,textvariable=self.sugar,relief=SUNKEN,font=("times new roman",20,"bold")).grid(row=4,column=1,padx=10,pady=10)

                self.Tea=Label(f3,text="Tea",font=("times new roman",20,"bold"),bg=bg_color,fg="yellow").grid(row=5,column=0,padx=10,pady=10)
                self.Tea_txt=Entry(f3,width=10,bd=5,textvariable=self.tea,relief=SUNKEN,font=("times new roman",20,"bold")).grid(row=5,column=1,padx=10,pady=10)

                ###################################### cold drinks  #######################
                f4=LabelFrame(self.root,text="Cold Drinks",font=("times new roman",22,"bold"),bg=bg_color,fg="red",bd=12,relief=GROOVE)
                f4.place(x=770,y=195,width=350,height=430)
                G1=Label(f4,text="Thums Up",font=("times new roman",20,"bold"),bg=bg_color,fg="yellow").grid(row=0,column=0,padx=10,pady=10)
                G11=Entry(f4,width=10,bd=5,textvariable=self.Tu,relief=SUNKEN,font=("times new roman",20,"bold")).grid(row=0,column=1,padx=10,pady=10)
                
                G2=Label(f4,text="Sprite",font=("times new roman",20,"bold"),bg=bg_color,fg="yellow").grid(row=1,column=0,padx=10,pady=10)
                G22=Entry(f4,width=10,bd=5,textvariable=self.s,relief=SUNKEN,font=("times new roman",20,"bold")).grid(row=1,column=1,padx=10,pady=10)

                G3=Label(f4,text="Pepsi",font=("times new roman",20,"bold"),bg=bg_color,fg="yellow").grid(row=2,column=0,padx=10,pady=10)
                G33=Entry(f4,width=10,bd=5,textvariable=self.P,relief=SUNKEN,font=("times new roman",20,"bold")).grid(row=2,column=1,padx=10,pady=10)
                
                G4=Label(f4,text="Red Bull",font=("times new roman",20,"bold"),bg=bg_color,fg="yellow").grid(row=3,column=0,padx=10,pady=10)
                G44=Entry(f4,width=10,bd=5,textvariable=self.RB,relief=SUNKEN,font=("times new roman",20,"bold")).grid(row=3,column=1,padx=10,pady=10)

                G5=Label(f4,text="Coca",font=("times new roman",20,"bold"),bg=bg_color,fg="yellow").grid(row=4,column=0,padx=10,pady=10)
                G55=Entry(f4,width=10,bd=5,textvariable=self.Coca,relief=SUNKEN,font=("times new roman",20,"bold")).grid(row=4,column=1,padx=10,pady=10)

                G6=Label(f4,text="Soda",font=("times new roman",20,"bold"),bg=bg_color,fg="yellow").grid(row=5,column=0,padx=10,pady=10)
                G66=Entry(f4,width=10,bd=5,textvariable=self.soda,relief=SUNKEN,font=("times new roman",20,"bold")).grid(row=5,column=1,padx=10,pady=10)

                ###################################### print bill  #######################
                f5=Frame(self.root,bd=12,relief=GROOVE)
                f5.place(x=1140,y=200,width=390,height=430)
                self.bill_label=Label(f5,text="Bill Receipt",font=("times new roman",20,"bold"),bg="grey",fg="black").pack(side="top",fill="x")
                self.bill_scroll=Scrollbar(f5,orient=VERTICAL)
                self.bill_txt=Text(f5,font=("times new roman",14),yscrollcommand=self.bill_scroll.set)
                self.bill_scroll.pack(side=RIGHT,fill=Y)
                self.bill_scroll.config(command=self.bill_txt.yview)
                self.bill_txt.pack(fill="both",expand=1)

                ###################################### for taxes  and pricess  and buttons #######################
                f6=Frame(self.root,bd=10,relief=GROOVE,bg=bg_color)
                f6.place(x=0,y=630,relwidth=1,height=165)
                T1=Label(f6,text="Total Cosmatics Price",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=0,column=0,padx=10,pady=10)
                T11=Entry(f6,width=10,bd=5,textvariable=self.tcp,relief=SUNKEN,font=("times new roman",15,"bold")).grid(row=0,column=1,padx=10,pady=7)

                T2=Label(f6,text="Total Glossary Price",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=1,column=0,padx=10,pady=10)
                T22=Entry(f6,width=10,bd=5,textvariable=self.tgp,relief=SUNKEN,font=("times new roman",15,"bold")).grid(row=1,column=1,padx=10,pady=7)

                T3=Label(f6,text="Total Cold Drinks Price",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=2,column=0,padx=10,pady=10)
                T33=Entry(f6,width=10,bd=5,textvariable=self.tcdp,relief=SUNKEN,font=("times new roman",15,"bold")).grid(row=2,column=1,padx=10,pady=7)

                T4=Label(f6,text="Cosmatics Tax",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=0,column=2,padx=10,pady=10)
                T44=Entry(f6,width=10,bd=5,textvariable=self.tcpt,relief=SUNKEN,font=("times new roman",15,"bold")).grid(row=0,column=3,padx=10,pady=7)

                T5=Label(f6,text="Glossary Tax",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=1,column=2,padx=10,pady=10)
                T55=Entry(f6,width=10,bd=5,textvariable=self.tgpt,relief=SUNKEN,font=("times new roman",15,"bold")).grid(row=1,column=3,padx=10,pady=7)

                T6=Label(f6,text="Cold Drinks Tax",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=2,column=2,padx=10,pady=10)
                T6=Entry(f6,width=10,bd=5,textvariable=self.tcdpt,relief=SUNKEN,font=("times new roman",15,"bold")).grid(row=2,column=3,padx=10,pady=7)

                f7=Frame(f6,bd=10,relief=GROOVE,bg=bg_color)
                f7.place(x=660,y=10,width=850,height=130)

                total_button=Button(f7,text="Total",width=10,command=self.total_price,font=("times new roman",20,"bold"),bg="white",fg="black",bd=10).grid(row=0,column=0,padx=10,pady=25)
                Generate_button=Button(f7,text="Send Bill",width=10,command=self.send_bill,font=("times new roman",20,"bold"),bg="white",fg="black",bd=10).grid(row=0,column=1,padx=15,pady=25)
                clear_button=Button(f7,text="Clear",width=10,font=("times new roman",20,"bold"),bg="white",fg="black",bd=10,command=self.clear_data).grid(row=0,column=2,padx=10,pady=25)
                Exit_button=Button(f7,text="Exit",width=10,command=self.exit_app,font=("times new roman",20,"bold"),bg="white",fg="black",bd=10).grid(row=0,column=3,padx=10,pady=25)
        def total_price(self):
                self.soap_price=self.soap.get() * 40
                self.FC_price=self.fracecreame.get() * 140
                self.FW_price=self.fw.get() * 100
                self.HS_price=self.hs.get() * 190
                self.HG_price=self.HG.get() * 120
                self.BL_price=self.BL.get() * 150

                self.rice_price=self.rice.get() * 40
                self.oil_price=self.oil.get() * 100
                self.daal_price=self.daal.get() * 70
                self.wheat_price=self.wheat.get() * 30
                self.sugar_price=self.sugar.get() * 40
                self.tea_price=self.tea.get() * 150

                self.TU_price=self.Tu.get() * 60
                self.S_price=self.s.get() * 50
                self.P_price=self.P.get() * 70
                self.RB_price=self.RB.get() * 190
                self.COCA_price=self.Coca.get() * 120
                self.Soda_price=self.soda.get() * 60
                # calculation of price
                self.TCP=float(round((self.soap_price + self.FC_price + self.FW_price + self.HS_price + self.HG_price + self.BL_price),2))
                self.tcp.set(self.TCP)
                self.TGP=float(round((self.rice_price + self.oil_price + self.daal_price + self.wheat_price + self.sugar_price + self.tea_price),2))
                self.tgp.set(self.TGP)
                self.TCDP=float(round((self.TU_price + self.S_price + self.P_price + self.RB_price + self.COCA_price + self.Soda_price),2))
                self.tcdp.set(self.TCDP)
                # price of tax 
                self.TCT=float(round((self.TCP*0.05),2))
                self.TGT=float(round((self.TGP*0.1),2))
                self.TCDT=float(round((self.TCDP*0.1),2))
                self.tcpt.set(self.TCT)
                self.tgpt.set(self.TGT)
                self.tcdpt.set(self.TCDT)
                self.generate_bill()
                
        def generate_bill(self):
                self.bill_txt.delete(1.0,END)
                if self.c_name.get()=="" and  self.c_phone.get()=="" and  self.c_bill.get()=="":
                        messagebox.showwarning(" ","Fill Customer Name ,Customer Phone and Customer Bill NO. First")
                else:
                                
                        self.bill_txt.insert(END,"\tWelcome Billing System ")
                        self.bill_txt.insert(END,"\nCustomer Number:{}".format(self.c_bill.get()))
                        self.bill_txt.insert(END,"\nCustomer Name:{}".format(self.c_name.get()))
                        self.bill_txt.insert(END,"\nCustomer Phone:{}".format(self.c_phone.get()))
                        self.bill_txt.insert(END,"\n===============================")
                        self.bill_txt.insert(END,"\nProduct\t\tQTY\t\tPrice")
                        self.bill_txt.insert(END,"\n===============================")
                        if self.soap.get()!=0:       
                                self.bill_txt.insert(END,"\n Bath Soap\t\t {} \t\t {}".format(self.soap.get(),self.soap_price))
                        if self.fracecreame.get()!=0:
                                self.bill_txt.insert(END,"\n Face Creame \t\t {} \t\t {}".format(self.fracecreame.get(),self.FC_price))
                        if self.fw.get()!=0:
                                self.bill_txt.insert(END,"\n Face Wash \t\t {} \t\t {}".format(self.fw.get(),self.FW_price))
                        if self.hs.get()!=0:
                                self.bill_txt.insert(END,"\n Hair Spray \t\t {} \t\t {}".format(self.hs.get(),self.HS_price))
                        if self.HG.get()!=0:
                                self.bill_txt.insert(END,"\n Hair Gell \t\t {} \t\t {}".format(self.HG.get(),self.HG_price))
                        if self.BL.get()!=0:
                                self.bill_txt.insert(END,"\n Body Loshan \t\t {} \t\t {}".format(self.BL.get(),self.BL_price))
                        if self.rice.get()!=0:
                                self.bill_txt.insert(END,"\n Rice \t\t {} \t\t {}".format(self.rice.get(),self.rice_price))
                        if self.oil.get()!=0:
                                self.bill_txt.insert(END,"\n Food Oil \t\t {} \t\t {}".format(self.oil.get(),self.oil_price))
                        if self.daal.get()!=0:
                                self.bill_txt.insert(END,"\n Daal \t\t {}\t\t {}".format(self.daal.get(),self.daal_price))
                        if self.wheat.get()!=0:
                                self.bill_txt.insert(END,"\n Wheat \t\t {}\t\t {}".format(self.wheat.get(),self.wheat_price))
                        if self.sugar.get()!=0:
                                self.bill_txt.insert(END,"\n Sugar \t\t {}\t\t {}".format(self.sugar.get(),self.sugar_price))
                        if self.tea.get()!=0:
                                self.bill_txt.insert(END,"\n Tea \t\t {}\t\t {}".format(self.tea.get(),self.tea_price))
                        if self.Tu.get()!=0:
                                self.bill_txt.insert(END,"\n Thums Up \t\t {}\t\t {}".format(self.Tu.get(),self.TU_price))
                        if self.s.get()!=0:
                                self.bill_txt.insert(END,"\n Sprite \t\t {}\t\t {}".format(self.s.get(),self.S_price))
                        if self.P.get()!=0:
                                self.bill_txt.insert(END,"\n Pepsi \t\t {}\t\t {}".format(self.P.get(),self.P_price))
                        if self.RB.get()!=0:
                                self.bill_txt.insert(END,"\n Red Bull \t\t {}\t\t {}".format(self.RB.get(),self.RB_price))
                        if self.Coca.get()!=0:
                                self.bill_txt.insert(END,"\n Coca \t\t {}\t\t {}".format(self.Coca.get(),self.COCA_price))
                        if self.soda.get()!=0:
                                self.bill_txt.insert(END,"\n Soda \t\t {}\t\t {}".format(self.soda.get(),self.Soda_price))
                        self.bill_txt.insert(END,"\n===============================")
                        # total price with taxes
                        self.total=float(round((self.TCP+self.TGP+self.TCDP+self.TCT+self.TGT+self.TCDT),2))
                        # print(self.total)
                        if self.total !=0.0:
                                self.bill_txt.insert(END,"\n Total price:Rs.{}".format(self.total))
                                self.bill_txt.insert(END,"\n======== Thanks Visit Again =========")
                        else:
                                self.bill_txt.delete(1.0,END)
                                messagebox.showerror(title="error",message="You do not selected any product")  
                        self.save_bill()
        def clear_data(self):
                self.bill_txt.delete(1.0,END)
                self.c_name.set("")
                self.c_phone.set("")
                self.c_bill.set("")
                self.soap.set("")
                self.fracecreame.set("")
                self.fw.set("")
                self.hs.set("")
                self.HG.set("")
                self.BL.set("")
                self.rice.set("")
                self.oil.set("")
                self.daal.set("")
                self.wheat.set("")
                self.sugar.set("")
                self.tea.set("")
                self.Tu.set("")
                self.s.set("")
                self.P.set("")
                self.RB.set("")
                self.Coca.set("")
                self.soda.set("")
                self.tcp.set("")
                self.tgp.set("")
                self.tcdp.set("")
                self.tcpt.set("")
                self.tgpt.set("")
                self.tcdpt.set("")
        def save_bill(self):
                o=messagebox.askyesno("Save Bill","do you want to save ?")
                if o > 0:        
                        self.bill_data=self.bill_txt.get('1.0',END)
                        # print(self.bill_data)
                        f1=open("bills/"+str(self.c_bill.get())+".txt","w")
                        f1.write(self.bill_data)
                        f1.close()
                        messagebox.showinfo("save","saved successfully")
                else:
                        return

        def search_bills(self):
                present="no"
                for i in os.listdir("bills/"):
                        if i.split(".")[0]==self.c_bill.get():
                                f1=open(f"bills/{i}","r")
                                self.bill_txt.delete("1.0",END)
                                for d in f1:
                                        self.bill_txt.insert(END,d)
                                f1.close()
                                present="yes"
                if present=="no":
                        messagebox.showerror("error","invallid Bill No.")
        def exit_app(self):
                exit()
        def send_bill(self):
                self.url='https://www.fast2sms.com/dev/bulk'
                self.params={
                        'authorization':'dCiQaJFmWhYe3ur0sbVI9K58GPSfBRX1H6nvkTOoZUqp7Mwyg2w4oj65faX2MAm7enlx0bgruBvFiIds',
                        'sender_id':'FSTSMS',
                        'message':'{}'.format(self.bill_txt.get('1.0',END)),
                        'route':'p',
                        'numbers':'{}'.format(self.c_phone.get()),
                        'language':'english'
                }
                requests.get(url=self.url,params=self.params)
                messagebox.showinfo("send message","message send successfully")
root=Tk()
b=billing_system(root)
root.mainloop()

