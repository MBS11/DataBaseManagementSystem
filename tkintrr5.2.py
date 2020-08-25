
import pymysql
n=pymysql.connect(host='localhost',user='root',password='',db='nap')
from tkinter import *
from tkinter.ttk import Combobox
window=Tk()
window.title("data")

f=Frame(window)
f.pack()

A=StringVar()
B=StringVar()
C=StringVar()
D=StringVar()
E=StringVar()

a=Label(f,text="First Name",width=10,font=("bold",10),bg='black',fg='white',bd=5)
a.grid(row=0,column=0)
b=Label(f,text="Last Name",width=10,font=("bold",10),bg='gray',fg='white',bd=5)
b.grid(row=1,column=0)
c=Label(f,text="Age",width=10,font=("bold",10),bg='black',fg='white',bd=5)
c.grid(row=2,column=0)
d=Label(f,text="Mobile No.",width=10,font=("bold",10),bg='gray',fg='white',bd=5)
d.grid(row=3,column=0)
e=Label(f,text="ID",width=10,font=("bold",10),bg='black',fg='white',bd=5)
e.grid(row=4,column=0)
a1=Entry(f,textvariable=A,bd=5)
a1.grid(row=0,column=2)
b1=Entry(f,textvariable=B,bd=5)
b1.grid(row=1,column=2)
c1=Entry(f,textvariable=C,bd=5)
c1.grid(row=2,column=2)
d1=Entry(f,textvariable=D,bd=5)
d1.grid(row=3,column=2)
e1=Entry(f,textvariable=E,bd=5)
e1.grid(row=4,column=2)

def which_selected():
    print("at{0}".format(select.curselection()))
    return int(select.curselection()[0])

def load():
    b=n.cursor()
    sql="SELECT * FROM `pan`"
    d=b.execute(sql)
    result=b.fetchall()
    n.commit()
    (e1,a1,b1,c1,d1)=result[which_selected()]
    E.set(e1)
    A.set(a1)
    B.set(b1)
    C.set(c1)
    D.set(d1)



   
def add():
     A=a1.get()
     B=b1.get()
     C=c1.get()
     D=d1.get()
     E=e1.get()
     m=n.cursor()
     sql="INSERT INTO `pan`(`id`,`First Name`, `Last Name`, `Age`, `Phone no.`) VALUES (%s,%s,%s,%s,%s)"
     gg=(E,A,B,C,D)
     o=m.execute(sql,gg)
     n.commit()
     a1.delete(0,'end')
     b1.delete(0,'end')
     c1.delete(0,'end')
     d1.delete(0,'end')
     e1.delete(0,'end')
     f()
    
def update():
    A=a1.get()
    B=b1.get()
    C=c1.get()
    D=d1.get()
    E=e1.get()
    b=n.cursor()
    sql='UPDATE `pan` SET `First Name`=%s,`Last Name`=%s,`Age`=%s,`Phone no.`=%s WHERE  `id`= %s'
    gg=(A,B,C,D,E)
    d=b.execute(sql,gg)
    n.commit()
    a1.delete(0,'end')
    b1.delete(0,'end')
    c1.delete(0,'end')
    d1.delete(0,'end')
    e1.delete(0,'end')

def refresh():
    f()
def delete():
    b=n.cursor()
    E=e1.get()
    sql="DELETE  FROM `pan` WHERE `id`= %s"
    d=b.execute(sql,E)
    n.commit()
    a1.delete(0,'end')
    b1.delete(0,'end')
    c1.delete(0,'end')
    d1.delete(0,'end')
    e1.delete(0,'end')

    

    
Button(f,text="ADD",bd=5,padx=10,command=add).grid(row=5,column=1)
Button(f,text="LOAD",bd=5,padx=10,command=load).grid(row=6,column=0)
Button(f,text="DELETE",bd=5,padx=10,command=delete).grid(row=8,column=1)
Button(f,text="UPDATE",bd=5,padx=10,command=update).grid(row=6,column=2)
Button(f,text="REFRESH",bd=5,padx=10,command=refresh).grid(row=9,column=1)

ff=Frame(window)
ff.pack()


scroll=Scrollbar(ff,orient=VERTICAL)
select=Listbox(ff,yscrollcommand=scroll.set,width=50,height=6)
scroll.config(command=select.yview)
scroll.pack(side=RIGHT,fill=Y)
select.pack(side=LEFT,fill=BOTH,expand=1)


def f():
    select.delete(0,END)

    b=n.cursor()
    sql="SELECT * FROM `pan`"
    d=b.execute(sql)
    result=b.fetchall()
    for i in result:
        select.insert(END,i)
        
    n.commit()
f()
window.mainloop()
