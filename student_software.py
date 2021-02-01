import tkinter as tk
from tkinter import ttk
import time
import mysql.connector as con
from tkinter import messagebox
class student_class:
    def __init__(self,root):
        self.connection=con.connect(host='localhost',user='root',password='root',database='student')
        print("connection done")
        self.name1=tk.StringVar()
        self.roll=tk.IntVar()
        self.GR=tk.IntVar()
        self.genderr=tk.StringVar()
        self.collegee=tk.StringVar()
        self.classs=tk.StringVar()
        self.div=tk.StringVar()
        self.per=tk.IntVar()
        self.statuss=tk.StringVar()
        
        self.search_txt=tk.StringVar()

        self.root=root
        bg_color="#ABCDEF"
        self.frame1=tk.Frame(self.root,width=660,height=100,borderwidth=15,bg=bg_color,relief="groove")
        self.label_title=tk.Label(self.frame1,bd=10,bg=bg_color,text="Welcome To Student Management System",font=("times new roman",40,"bold"))
        self.label_title.pack(padx=5,pady=5,expand=True)
        # self.label_time=tk.Label(self.frame1,text=time.strftime('%H:%M:%S'),font=15)
        # self.label_time.pack(side="right",padx=5,pady=5)
        self.frame1.pack(padx=5,pady=5,fill="x")
            
        self.frame2=tk.Frame(self.root,width=400,height=900,bd=10,borderwidth=15,bg=bg_color,relief="groove")
        self.frame2.pack(side="left",padx=5,pady=1,fill="y",ipadx=10,ipady=10)

        self.name=tk.Label(self.frame2,text="NAME",bg=bg_color,font=("times new roman",20,"bold"))
        self.name.grid(row=0,column=0,columnspan=1,padx=5,pady=10,rowspan=1,sticky=tk.E+tk.W+tk.N+tk.S)
        self.name_entry=tk.Entry(self.frame2,font=14,width=15,textvariable=self.name1)
        self.name_entry.grid(row=0,column=1,columnspan=1,padx=5,pady=10,rowspan=1,sticky=tk.E+tk.W+tk.N+tk.S)

        self.roll_no=tk.Label(self.frame2,text="ROLL NO",bg=bg_color,font=("times new roman",20,"bold"))
        self.roll_no.grid(row=1,column=0,columnspan=1,padx=5,pady=10,rowspan=1,sticky=tk.E+tk.W+tk.N+tk.S)
        self.roll_entry=tk.Entry(self.frame2,font=14,width=15,textvariable=self.roll)
        self.roll_entry.grid(row=1,column=1,columnspan=1,padx=5,pady=10,rowspan=1,sticky=tk.E+tk.W+tk.N+tk.S)

        self.GR_NO=tk.Label(self.frame2,text="GR NO",bg=bg_color,font=("times new roman",20,"bold"))
        self.GR_NO.grid(row=2,column=0,columnspan=1,padx=5,pady=10,rowspan=1,sticky=tk.E+tk.W+tk.N+tk.S)
        self.GR_entry=tk.Entry(self.frame2,font=14,width=15,textvariable=self.GR)
        self.GR_entry.grid(row=2,column=1,columnspan=1,padx=5,pady=10,rowspan=1,sticky=tk.E+tk.W+tk.N+tk.S)

        self.gender=tk.Label(self.frame2,text="GENDER",bg=bg_color,font=("times new roman",20,"bold"))
        self.gender.grid(row=3,column=0,columnspan=1,padx=5,pady=10,rowspan=1,sticky=tk.E+tk.W+tk.N+tk.S)
        self.gender_entry=tk.Entry(self.frame2,font=14,width=15,textvariable=self.genderr)
        self.gender_entry.grid(row=3,column=1,columnspan=1,padx=5,pady=10,rowspan=1,sticky=tk.E+tk.W+tk.N+tk.S)

        self.college=tk.Label(self.frame2,text="COLLEGE NAME",bg=bg_color,font=("times new roman",20,"bold"))
        self.college.grid(row=4,column=0,columnspan=1,padx=5,pady=10,rowspan=1,sticky=tk.E+tk.W+tk.N+tk.S)
        self.college_entry=tk.Entry(self.frame2,font=14,width=15,textvariable=self.collegee)
        self.college_entry.grid(row=4,column=1,columnspan=1,padx=5,pady=10,rowspan=1,sticky=tk.E+tk.W+tk.N+tk.S)

        self.class_name=tk.Label(self.frame2,text="CLASS",bg=bg_color,font=("times new roman",20,"bold"))
        self.class_name.grid(row=5,column=0,columnspan=1,padx=5,pady=10,rowspan=1,sticky=tk.E+tk.W+tk.N+tk.S)
        self.class_entry=tk.Entry(self.frame2,font=14,width=15,textvariable=self.classs)
        self.class_entry.grid(row=5,column=1,columnspan=1,padx=5,pady=10,rowspan=1,sticky=tk.E+tk.W+tk.N+tk.S)

        self.DIV=tk.Label(self.frame2,text="DIV",bg=bg_color,font=("times new roman",20,"bold"))
        self.DIV.grid(row=6,column=0,columnspan=1,padx=5,pady=10,rowspan=1,sticky=tk.E+tk.W+tk.N+tk.S)
        self.div_entry=tk.Entry(self.frame2,font=14,width=15,textvariable=self.div)
        self.div_entry.grid(row=6,column=1,columnspan=1,padx=5,pady=10,rowspan=1,sticky=tk.E+tk.W+tk.N+tk.S)

        self.percentage=tk.Label(self.frame2,text="PERCENTAGE",bg=bg_color,font=("times new roman",20,"bold"))
        self.percentage.grid(row=7,column=0,columnspan=1,padx=5,pady=10,rowspan=1,sticky=tk.E+tk.W+tk.N+tk.S)
        self.per_entry=tk.Entry(self.frame2,font=14,width=15,textvariable=self.per)
        self.per_entry.grid(row=7,column=1,columnspan=1,padx=5,pady=10,rowspan=1,sticky=tk.E+tk.W+tk.N+tk.S)

        self.status=tk.Label(self.frame2,text="STATUS",bg=bg_color,font=("times new roman",20,"bold"))
        self.status.grid(row=8,column=0,columnspan=1,padx=5,pady=10,rowspan=1,sticky=tk.E+tk.W+tk.N+tk.S)
        self.status_entry=tk.Entry(self.frame2,font=14,width=15,textvariable=self.statuss)
        self.status_entry.grid(row=8,column=1,columnspan=1,padx=5,pady=10,rowspan=1,sticky=tk.E+tk.W+tk.N+tk.S)

        self.add_button=tk.Button(self.frame2,text="ADD",font=10,width=8,height=1,command=self.add)
        self.add_button.grid(row=9,column=0,columnspan=1,padx=15,pady=15,rowspan=1,sticky=tk.E+tk.W+tk.N+tk.S)
        
        self.update_button=tk.Button(self.frame2,text="UPDATE",width=15,font=10,height=1,command=self.update)
        self.update_button.grid(row=9,column=1,columnspan=1,padx=15,pady=15,rowspan=1,sticky=tk.E+tk.W+tk.N+tk.S)

        self.delete_button=tk.Button(self.frame2,text="DELETE",width=8,font=10,height=1,command=self.delete)
        self.delete_button.grid(row=10,column=0,columnspan=1,padx=15,pady=15,rowspan=1,sticky=tk.E+tk.W+tk.N+tk.S)

        self.clear_button=tk.Button(self.frame2,text="CLEAR",width=15,font=10,height=1,command=self.clear)
        self.clear_button.grid(row=10,column=1,columnspan=1,padx=15,pady=15,rowspan=1,sticky=tk.E+tk.W+tk.N+tk.S)

        self.frame3=tk.Frame(self.root,width=1250,height=950,borderwidth=15,bg=bg_color,relief="groove")

        self.search_label=tk.Entry(self.frame3,text="ENTER VALUE FOR SEARCH",width=20,font=14,textvariable=self.search_txt)
        self.search_label.place(x=350,y=30)
        self.search_button=tk.Button(self.frame3,text="SEARCH",font=14,command=self.search_data)
        self.search_button.place(x=650,y=30)

        self.table=ttk.Treeview(self.frame3,height=200)
            
        self.table["columns"] = ("NAME","ROLL NO","GR NO","GENDER","COLLEGE NAME","CLASS","DIV","PERCENTAGE","STATUS") 
            # Defining heading 
        self.table['show'] = 'headings'
        # self.table.column(" ID", width = 90, anchor ='c') 
        self.table.column("NAME", width = 90, anchor ='c') 
        self.table.column("ROLL NO", width = 90, anchor ='se') 
        self.table.column("GR NO", width = 90, anchor ='se')
        self.table.column("GENDER", width = 90, anchor ='c') 
        self.table.column("COLLEGE NAME", width = 90, anchor ='se') 
        self.table.column("CLASS", width = 90, anchor ='se')
        self.table.column("DIV", width = 90, anchor ='c') 
        self.table.column("PERCENTAGE", width = 90, anchor ='se') 
        self.table.column("STATUS", width = 90, anchor ='se')

        # self.table.heading("ID",text="ID")
        self.table.heading("NAME",text="NAME")
        self.table.heading("ROLL NO",text="ROLL NO")
        self.table.heading("GR NO",text="GR NO")
        self.table.heading("GENDER",text="GENDER")
        self.table.heading("COLLEGE NAME",text="COLLEGE NAME")
        self.table.heading("CLASS",text="CLASS")
        self.table.heading("DIV",text="DIV")
        self.table.heading("PERCENTAGE",text="PERCENTAGE")
        self.table.heading("STATUS",text="STATUS")
        self.table.place(x=50,y=100)
        self.table.place_configure(height=500)
        self.frame3.pack(fill="both",expand=True)
        self.table.bind("<ButtonRelease-1>",self.get_cursor)
        self.clear()
        self.display()   
    def add(self):
        cursor=self.connection.cursor()
        query="insert into student_data values('{}',{},{},'{}','{}','{}','{}',{},'{}')".format(self.name1.get(),self.roll.get(),self.GR.get(),self.genderr.get(),self.collegee.get(),self.classs.get(),self.div.get(),self.per.get(),self.statuss.get())
        cursor.execute(query)
        self.connection.commit()
        self.clear()
        self.display()
        print("datasave successfully")
        
    def delete(self):
        cursor=self.connection.cursor()
        query="delete from student_data where Gr_NO= {}".format(self.GR.get())
        cursor.execute(query)
        print(query)
        self.connection.commit()
        self.clear()
        self.display()
        print("delete data successfully")

    def update(self):
        cursor=self.connection.cursor()
        query="update student_data SET name='{}',roll_no={},gender='{}',college_name='{}',class='{}',division='{}',percentage={},status='{}' where Gr_NO={}".format(self.name1.get(),self.roll.get(),self.genderr.get(),self.collegee.get(),self.classs.get(),self.div.get(),self.per.get(),self.statuss.get(),self.GR.get())
        # print(query)
        cursor.execute(query)
        self.connection.commit()
        self.clear()
        self.display()
        print("statuss:",self.statuss.get())
        print("data updated successfully")
        
    def clear(self):
        self.name1.set("")
        self.roll.set("")
        self.GR.set("")
        self.genderr.set("")
        self.collegee.set("")
        self.classs.set("")
        self.div.set("")
        self.per.set("")
        self.statuss.set("")
        # print("data clear successfully")

    def display(self):
        cursor=self.connection.cursor()
        query="select * from student_data"
        cursor.execute(query)
        result=cursor.fetchall()
        j=0
            # print(result)
        if len(result)!=0:
            self.table.delete(*self.table.get_children()) 
            for i in result:
                self.table.insert('',j,text="end",values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]))
        self.connection.commit()
        # print("data display successfully")
    def get_cursor(self,p):
        self.cursor_get=self.table.focus()
        self.contents=self.table.item(self.cursor_get)
        row=self.contents['values']
        # print(row)
        self.name1.set(row[0])
        self.roll.set(row[1])
        self.GR.set(row[2])
        self.genderr.set(row[3])
        self.collegee.set(row[4])
        self.classs.set(row[5])
        self.div.set(row[6])
        self.per.set(row[7])
        self.statuss.set(row[8])
    def search_data(self):
        cursor=self.connection.cursor()
        query="select * from student_data where Gr_NO={}".format(self.search_txt.get())
        # print(query)
        cursor.execute(query)
        result=cursor.fetchone()
        # print(cursor)
        j=0
        self.table.delete(*self.table.get_children()) 
        self.table.insert('',j,text="end",values=(result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8]))
        self.connection.commit()
if __name__ == "__main__":
    root=tk.Tk(className=" STUDENT MANAGEMENT SYSTEM")
    st=student_class(root)
    root.configure(bg="light blue")
    root.geometry("1530x800+0+0")
    root.mainloop()
