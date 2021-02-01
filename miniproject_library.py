class library:
    def __init__(self,name,list):
        self.name=name
        self.list=list
        self.addict={}
        
    def displaybook(self,list):
        print(f"Welcome in the library {self.name}")
        for i in list:
            print(i)
            
    def lend(self):
        name=input("Enter the name of book you want lend:")
        user=input("Enter the name of student:")
        if name==self.addict.keys():
            print(f"the book is already issue {self.user}")
        else:
            self.addict.update({user:name})
            print("book is issued successfully")
    def addbook(self):
        user1=input("Enter the name of book which you want to add::")
        f=open("library_name.txt","a+")
        f.write(user1)
        f.close()
        print("book added successfully")
        
    def removebook(self):
       user1=input("Enter the name of book which you want to add::")
       f=open("library_name.txt","w")
       f.replace("user1","")
       f.close()
       print("book is removed successfully")
    
f=open("library_name.txt")
str=[]
for i in f:
    str.append(i)
l=library("VIIT LIBRARY", str)
while(True):
    print("1.display books")
    print("2.issue books")
    print("3.addbook books")
    print("4.remove book books")
    print("5.exit")
    name1=input("Enter the your choice::")
    if name1=="1":
        l.displaybook(str)
    elif name1=="2":
        l.lend()
    elif name1=="3":
        l.addbook()
    elif name1=="4":
        l.removebook()
    elif name1=="5":
        exit()
    else:
        print("EnNter the chice in above option !!!!")