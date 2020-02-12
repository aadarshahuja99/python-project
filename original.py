from tkinter import *
from PIL import ImageTk,Image
import sqlite3
from tkinter import messagebox as ms
root=Tk()
root.title("Login page")
root.geometry("1366x768")
f=Frame(root,height=768,width=1366)
f.propagate(0)
f.pack()
img=ImageTk.PhotoImage(Image.open("final.jpg"))
l1= Label(f,image=img)
l1.place(x=0, y=0, relwidth=1, relheight=1)
e1=StringVar()
e2=StringVar()
def open_window():
    uname="pc"
    paswrd="aadarsh"
    name=e1.get()
    passwd=e2.get()
    if(name==uname and passwd==paswrd):
        top1=Toplevel(bg='FLORAL WHITE')
        top1.overrideredirect(True)
        top1.geometry("1366x732")
        img1=ImageTk.PhotoImage(Image.open("1.png"))
        l1= Label(top1,image=img1)
        l1.place(x=0, y=0, relwidth=1, relheight=1)
        l1.image=img1
        r1=Radiobutton(top1,font=('calibri',16),text="Place Order",bg='FLORAL WHITE',activebackground='FLORAL WHITE',activeforeground='FLORAL WHITE',command=Place_Order)
        r2=Radiobutton(top1,font=('calibri',16),text="New Customer",bg='FLORAL WHITE',activebackground='FLORAL WHITE',activeforeground='FLORAL WHITE',command=New_Customer)
        r3=Radiobutton(top1,font=('calibri',16),text="Previous Details",bg='FLORAL WHITE',activebackground='FLORAL WHITE',activeforeground='FLORAL WHITE',command=Previous_Details)
        r1.place(x=130,y=240)
        r2.place(x=130,y=340)
        r3.place(x=130,y=440)
        b1=Button(top1,width=10,height=1,bg='FLORAL WHITE',text="Close app",command=root.destroy)
        b1.place(x=30,y=50)
    else:
        ms.showerror("OOPS!","Username or password did not match")
val1=StringVar()
val2=StringVar()
val3=StringVar()
val4=StringVar()
def New_Customer():
    top3=Toplevel(bg='FLORAL WHITE')
    top3.overrideredirect(True)
    top3.geometry("1366x732")
    img1=ImageTk.PhotoImage(Image.open("2.jpg"))
    l1= Label(top3,image=img1)
    l1.place(x=0, y=0, relwidth=1, relheight=1)
    l1.image=img1
    l1=Label(top3,text="Name",bg='FLORAL WHITE')
    e11=Entry(top3,width=18,textvar=val1,font=('Arial',16))
    l1.place(x=30,y=90)
    e11.place(x=100,y=90)
    l2=Label(top3,text="E-mail",bg='FLORAL WHITE')
    e12=Entry(top3,width=18,textvar=val2,font=('Arial',16))
    l2.place(x=30,y=150)
    e12.place(x=100,y=150)
    def check_email(event):
        
        s1=e12.get()
        
        s2=re.fullmatch('\w[a-zA-z0-9_.]*@gmail[.]com',str(s1))
        if(s2!=None):
            pass
        else:
            l10=Label(top3,text="Please Enter Valid Email",width=60,height=1,font=('Arial',-20,'bold'))
            l10.place(x=600,y=450)

    e12.bind("<Return>",check_email)
    l3=Label(top3,text="Phone Number",bg='FLORAL WHITE')
    e13=Entry(top3,width=18,textvar=val3,font=('Arial',16))
    l3.place(x=30,y=210)
    e13.place(x=130,y=210)
    def check(event):
        s=e13.get()
        s=str(s)
        s1=re.fullmatch('[6-9][0-9]{9}',s)
        if(s1!=None):
            pass
        else:
            l10=Label(top3,text="Please Enter Valid Mobile No!",width=60,height=1,font=('Arial',-20,'bold'))
            l10.place(x=600,y=525)

    e13.bind("<Return>",check)
    l4=Label(top3,text="GST Number",bg='FLORAL WHITE')
    e14=Entry(top3,width=18,textvar=val4,font=('Arial',16))
    l4.place(x=30,y=270)
    e14.place(x=130,y=270)
    infolabel1=Label(top3,text="PRESS ENTER BEFORE MOVING AHEAD [FOR EMAIL SYNTAX VERIFICATION]",bg='FLORAL WHITE',font=('Arial','-15','bold'),width=100,height=2,)
    infolabel1.place(x=500,y=150)
    infolabel2=Label(top3,text="PRESS ENTER BEFORE MOVING AHEAD [FOR PHONE NUMBER SYNTAX VERIFICATION]",bg='FLORAL WHITE',font=('Arial','-15','bold'),width=100,height=2,)
    infolabel2.place(x=500,y=210)
    n1=val1.get()
    n2=val2.get()
    n3=val3.get()
    n4=val4.get()
    def Save_Details():
        n1=val1.get()
        n2=val2.get()
        n3=val3.get()
        n4=val4.get()

        
        if(val1.get!="" and val2.get!="" and val3.get()!="" and val4.get!=""):
            conn=sqlite3.connect('trade.db')
            with conn:
                cursor=conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS trade_data1 (NAME TEXT ,E_MAIL TEXT,PHONE_NUMBER TEXT,GST_NUMBER TEXT)')
            find_user=("SELECT * FROM trade_data1 WHERE GST_NUMBER=?")
            cursor.execute(find_user,[(val4.get())])
            result=cursor.fetchall()
 
            cursor.execute('INSERT INTO trade_data1 (NAME,E_MAIL,PHONE_NUMBER,GST_NUMBER) VALUES(?,?,?,?)',(n1,n2,n3,n4))
            conn.commit()
            conn.close()
    b3=Button(top3,width=10,height=1,bg='FLORAL WHITE',text="Previous Page",command=open_window)
    b3.place(x=30,y=50)
    b1=Button(top3,width=16,height=1,bg='FLORAL WHITE',text="Save to Database",command=Save_Details)
    b1.place(x=130,y=430)
    b4=Button(top3,width=10,height=1,bg='FLORAL WHITE',text="Home Page",command=open_window)
    b4.place(x=400,y=430)

v4=StringVar() 
v5=StringVar()
v6=StringVar()
va1=StringVar()
va2=StringVar()
va3=StringVar()

def Place_Order():
    
    
    top5=Toplevel(bg='FLORAL WHITE')
    top5.overrideredirect(True)
    top5.geometry("1366x732")
    img1=ImageTk.PhotoImage(Image.open("12.jpg"))
    l11= Label(top5,image=img1)
    l11.place(x=0, y=0, relwidth=1, relheight=1)
    l11.image=img1
    label1=Label(top5,text="EMAIL",bg='FLORAL WHITE')
    label1.place(x=30,y=90)
    e1=Entry(top5,width=20,font=('Arial',16),textvariable=v4)
    e1.place(x=100,y=90)
    def check_email1(event):
        
        
        s1=e1.get()
        
        s2=re.fullmatch('\w[a-zA-z0-9_.]*@gmail[.]com',str(s1))
        if(s2!=None):
            pass
        else:
            l10=Label(top6,text="Please Enter Valid Email",width=60,height=1,font=('Arial',-20,'bold'))
            l10.place(x=600,y=450)

    e1.bind("<Return>",check_email1)
     


    l2=Label(top5,text="ORDER PLACED ON",bg='FLORAL WHITE')
    l2.place(x=400,y=90)
    e2=Entry(top5,width=10,font=('Arial',16),textvariable=v5)
    e2.place(x=530,y=90)

    l3=Label(top5,text="EXPECTED ORDER DELIVERY",bg='FLORAL WHITE')
    l3.place(x=770,y=90)
    e3=Entry(top5,width=10,font=('Arial',16),textvariable=v6)
    e3.place(x=950,y=90)


    l1=Label(top5,text="SELECT TYPE OF JEANS",font=('Arial',12))
    l1.place(x=50,y=150)

    
    
    s1=Spinbox(top5,values=("SKINNY FIT","REGULAR FIT","SLIM FIT","LOOSE FIT","NARROW FIT"),textvariable=va1,width=20,font=('Arial',16),bg="FLORAL WHITE")
    s1.place(x=50,y=220)


    b1=Button(top5,width=10,height=1,bg='FLORAL WHITE',text="Previous Page",command=open_window)
    b1.place(x=20,y=40)


    l2=Label(top5,text="SELECT SIZE RESPECTIVELY",font=('Arial',12))
    l2.place(x=50,y=300)
    s2=Spinbox(top5,values=("28","30","32","34","36"),textvariable=va2,width=20,font=('Arial',16),bg="FLORAL WHITE")
    s2.place(x=50,y=370)


    l3=Label(top5,text="SELECT QUANTITY RESPECTIVELY",font=('Arial',12))
    l3.place(x=50,y=450)
    s3=Spinbox(top5,values=("500","1000","1500","2000","2500","3000"),textvariable=va3,width=20,font=('Arial',16),bg="FLORAL WHITE")


    s3.place(x=50,y=520)
    def saveorder():
        n1=v4.get()
        n2=va1.get()
        n3=va2.get()
        n4=va3.get()
        n5=v5.get()
        n6=v6.get()
     
        if(v4.get!="" and va1.get!="" and va2.get()!="" and va3.get!="" and v5.get!="" and v6.get!=""):
        
            conn=sqlite3.connect('trade.db')
            with conn:
                cursor=conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS orders1 (EMAIL TEXT ,TYPE TEXT,SIZE INTEGER,QUAN INTEGER,DOO TEXT,DOD TEXT)')
 
            cursor.execute('INSERT INTO orders1 (EMAIL,TYPE,SIZE,QUAN,DOO,DOD) VALUES(?,?,?,?,?,?)',(str(n1),str(n2),str(n3),str(n4),str(n5),str(n6)))
            conn.commit()
            conn.close()
        n7=int(n4)
        amt=n7*750
        l3=Label(top5,text="AMOUNT TO BE PAID="+str(amt),font=('Arial',12))
        l3.place(x=120,y=650)
    
    
    button=Button(top5,width=15,height=1,text="Confirm Order",bg='FLORAL WHITE',command=saveorder)
    button.place(x=500,y=570)
    
            
vs=StringVar()            
def Previous_Details():
    top6=Toplevel(bg='FLORAL WHITE')
    top6.overrideredirect(True)
    top6.geometry("1366x732")
    img1=ImageTk.PhotoImage(Image.open("records.jpg"))
    l11= Label(top6,image=img1)
    l11.place(x=0, y=0, relwidth=1, relheight=1)
    l11.image=img1
    b1=Button(top6,width=10,height=1,text="Previous Page",bg='FLORAL WHITE',command=open_window)
    b1.place(x=30,y=50)
    l1=Label(top6,text="Email Of Customer",bg='FLORAL WHITE')
    e1=Entry(top6,width=18,font=('Arial',16),textvariable=vs)
    l1.place(x=30,y=150)
    e1.place(x=180,y=150)
    def check_email(event):
        
        
        s1=e1.get()
        
        s2=re.fullmatch('\w[a-zA-z0-9_.]*@gmail[.]com',str(s1))
        if(s2!=None):
            pass
        else:
            l10=Label(top6,text="Please Enter Valid Email",width=60,height=1,font=('Arial',-20,'bold'))
            l10.place(x=600,y=450)

    e1.bind("<Return>",check_email)

    def recdisplay():
        n1=vs.get()  
        conn =sqlite3.connect('trade.db')
        with conn:
            cursor =conn.cursor()
        find_rec = ('SELECT * FROM orders1 WHERE EMAIL = ?')
        cursor.execute(find_rec,[str(n1)])
        result=cursor.fetchall()
        k=0
        if result:
            Mylabel=Label(top6,text="Email",bg="FLORAL WHITE",font=('Arial','-15','bold'),width=25,height=3).place(x=10,y=250)
            Mylabel=Label(top6,text="Jeans Type",bg="FLORAL WHITE",font=('Arial','-15','bold'),width=14,height=3).place(x=250,y=250)
            Mylabel=Label(top6,text="Size",bg="FLORAL WHITE",font=('Arial','-15','bold'),width=10,height=3).place(x=400,y=250)
            Mylabel=Label(top6,text="Quantity",bg="FLORAL WHITE",font=('Arial','-15','bold'),width=10,height=3).place(x=500,y=250)
            Mylabel=Label(top6,text="DOO",bg="FLORAL WHITE",font=('Arial','-15','bold'),width=10,height=3).place(x=600,y=250)
            Mylabel=Label(top6,text="DOD",bg="FLORAL WHITE",font=('Arial','-15','bold'),width=10,height=3).place(x=700,y=250) 
            for i in range(len(result)):
                for j in range(6):
                    if(j==0):
                        Mylabel=Label(top6,text=result[i][j],bg="FLORAL WHITE",font=('Arial','-15','bold'),width=25,height=1).place(x=10,y=350+k)
                    elif(j==1):
                        Mylabel=Label(top6,text=result[i][j],bg="FLORAL WHITE",font=('Arial','-15','bold'),width=14,height=1).place(x=250,y=350+k)
                    elif(j==2):
                        Mylabel=Label(top6,text=result[i][j],bg="FLORAL WHITE",font=('Arial','-15','bold'),width=10,height=1).place(x=400,y=350+k)
                    elif(j==3):
                        Mylabel=Label(top6,text=result[i][j],bg="FLORAL WHITE",font=('Arial','-15','bold'),width=10,height=1).place(x=500,y=350+k)
                    elif(j==4):
                        Mylabel=Label(top6,text=result[i][j],bg="FLORAL WHITE",font=('Arial','-15','bold'),width=10,height=1).place(x=600,y=350+k)
                    elif(j==5):
                        Mylabel=Label(top6,text=result[i][j],bg="FLORAL WHITE",font=('Arial','-15','bold'),width=10,height=1).place(x=700,y=350+k)     
                k+=50
                if(i==len(result)):
                    break
        else:
            l2=Label(top6,text="NO ENTRIES of "+str(n1)+" found!!",bg="FLORAL WHITE",font=('Arial','-15','bold'),width=100,height=1).place(x=10,y=250)
        return             
    b2=Button(top6,width=10,height=1,text="Search",bg='FLORAL WHITE',command=recdisplay)
    b2.place(x=30,y=600)
                  

    
    
label1=Label(f,text="Username",bg='FLORAL WHITE')
label2=Label(f,text="Password",bg='FLORAL WHITE')
e1=Entry(f,width=20,font=('Arial',16))
e2=Entry(f,width=20,font=('Arial',16),show='*')
label1.place(x=520,y=250)
e1.place(x=620,y=250)
label2.place(x=520,y=310)
e2.place(x=620,y=310)

b1=Button(f,width=10,height=1,text="Login",bg='FLORAL WHITE',command=open_window)
b1.place(x=683,y=420)
root.mainloop()
