from tkinter import *
from tkinter import messagebox as m
import pymysql as db

root=Tk()
root.title("BMI CALCULATOR")
def bmi():
    x=float(inp.get())/(float(inp2.get())**2)
    y=int(x)
    u=nm_entry.get()
    print('''%s your BMI is: %d'''%(u,y))
    if y in range(18,26):
        m.showinfo("Hello %s"%u,'''
        Your BMI = %d
        Congrats you are healthy!
        EAT-SLEEP-REPEAT
         '''%y)
    elif y in range(25,30):
    	m.showwarning("BMI Calculation",'''
        Your BMI = %d
        You fall in overweight category
        Start exercise..
         '''%y)
    elif y in range(2,18):
    	m.showwarning("BMI Calculation",'''
        Your BMI = %d
        You fall in Underweight category
        Consume Calories
         '''%y)
    elif y in range(30,35):
    	m.showerror("BMI Calculation",'''
        Your BMI = %d
        Alert You fall in Obese Class I
        Start Exercising
         '''%y)
    elif y in range(35,40):
    	m.showerror("BMI Calculation",'''
        Your BMI = %d
        Alert You fall in Obese Class II
        Start Exercising, Stop Fast fooding
         '''%y)
    elif (y>40):
    	m.showerror("BMI Calculation",'''
        Your BMI = %d
        Alert You fall in Obese Class III
        Consult Doctor ASAP
         '''%y)
    elif (y==0):
    	m.showwarning("ALert","Please enter Weight in KGS and Height in 'm'")

def con():
	name=nm_entry.get()
	age_in=int(age_en.get())
	bid=int(id_en.get())
	wt=int(inp.get())
	ht=float(inp2.get())
	bm=int(float(inp.get())/(float(inp2.get())**2))
	conn = db.connect( host="localhost", user="your_username_here", port=3306, passwd="your_password_here", database="your_db_name_here")
	cur = conn.cursor()
	sql_insert_query="""INSERT INTO `bmi`(`id`,`name`, `age` , `weight`, `height`, `bmi`) VALUES (%d,"%s",%d,%d,%.4f,%d)"""%(bid,name,age_in,wt,ht,bm)
	cur.execute(sql_insert_query)
	cur.close()
	conn.commit()
	conn.close()
	m.showinfo("Database Connected","Your data has been saved on server")

def ser_bmi():
	id_num=p_en.get()
	conn2= db.connect( host="localhost", user="your_username_here", port=3306, passwd="your_password_here", database="your_db_name_here")
	cur2 = conn2.cursor()
	sql_fetch_query='''SELECT * FROM `bmi` WHERE id=%d'''%id_num
	cur2.execute(sql_fetch_query)
	result = cur2.fetchall()
	results=list(result)
	m.showinfo("Patient Record Data",'''
	Details of Patient:
	ID: %d
	Name: "%s"
	Age: %d
	Weight: %d
	Height: %.4f
	BMI: %d'''%(results[0]))

	conn2.close()
	cur2.close()

def ser():
	search=Tk()
	search.title("Search")
	tit=Label(search,text="Search using Patient's ID",bg='yellow')
	tit.grid(row=0,columnspan=2)
	pid=Label(search,text="Patients ID")
	pid.grid(row=1,column=0)
	p_en=Entry(search)
	p_en.grid(row=1,column=1)
	ser_but=Button(search,text="SEARCH",bg='green',command=ser_bmi)
	ser_but.grid(row=3,columnspan=2)
	search.mainloop()

weight=Label(root,text="Weight (in KGS)")
id1=Label(root,text="Patient's ID")
id1.grid(row=2,column=0)
id_en=Entry(root)
id_en.grid(row=2,column=1)
name=Label(root,text="Full Name")
age=Label(root,text="Age")
calc=Label(root,text="BMI CALCULATOR",bg="yellow")
weight1=Label(root,text="Height (in m)")
name.grid(row=3,column=0)
age.grid(row=4,column=0)
nm_entry=Entry(root)
age_en=Entry(root)
calc.grid(row=0,column=0,columnspan=2)
weight.grid(row=5,column=0)
weight1.grid(row=6,column=0)
inp=Entry()
inp.grid(row=5,column=1)
nm_entry.grid(row=3,column=1)
inp2=Entry()
inp2.grid(row=6,column=1)
age_en.grid(row=4,column=1)
but=Button(root,text="BMI",bg="green", command=bmi)
but2=Button(root,text="SAVE",bg="orange", command=con)
but3=Button(root,text="SEARCH",bg="red", command=ser)
but.grid(row=7,column=0)
but2.grid(row=7,columnspan=2)
but3.grid(row=7,column=1)
root.mainloop()