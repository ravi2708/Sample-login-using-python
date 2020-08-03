from tkinter import *
import mysql.connector


mydb= mysql.connector.connect(host="localhost", user="root", password="", database="projectloginpage")
cursor= mydb.cursor()

def addpeople():
    fullname = e5.get()
    username = e3.get()
    password = e4.get()

    sql = "INSERT INTO people VALUES(%s, %s, %s)"
    cursor.execute(sql,(fullname, username, password))
    mydb.commit()
    print("Person added")
    return True

def displaypeople():
    username = e1.get()
    password = e2.get()
    sql = "SELECT * FROM people WHERE username = %s and password = %s"
    cursor.execute(sql,(username, password))
    result = cursor.fetchall()
    if not result:
        print("Wrong username or password")
    else:
        print("You are logged in")


def Login():

    window1 = Tk()
    window1.title("LOGIN")
    window1.geometry("500x300")
    global e1,e2

    l1 = Label(window1,text= "Login System", font="Arial", bg="black", fg="White")
    l1.grid()

    f1=Frame(window1)
    l2=Label(f1,text="USERNAME")
    e1=Entry(f1)
    l3=Label(f1,text="Password")
    e2=Entry(f1)

    l2.grid(column=1,row=1)
    e1.grid(column=2,row=1)
    l3.grid(column=1,row=2)
    e2.grid(column=2,row=2)

    s2 = Button(window1, text="Login", command=displaypeople)

    f1.grid()
    s2.grid()


    window1.mainloop()

def Signup():
    window2 = Tk()
    window2.title("SIGNUP")
    window2.geometry("500x300")
    global e3,e4,e5

    l5 = Label(window2, text="SIGN UP", font="Arial", bg="black", fg="White")
    l5.grid()

    f2=Frame(window2)
    l8=Label(f2,text="Fullname")
    e5=Entry(f2)
    l6=Label(f2,text="USERNAME")
    e3=Entry(f2)
    l7=Label(f2,text="Password")
    e4=Entry(f2)

    l8.grid(column=1,row=0)
    e5.grid(column=2,row=0)
    l6.grid(column=1,row=1)
    e3.grid(column=2,row=1)
    l7.grid(column=1,row=2)
    e4.grid(column=2,row=2)

    s1=Button(window2, text="Submit", command=addpeople)

    f2.grid()
    s1.grid()

    window2.mainloop()


window = Tk()
window.title("LOGIN")
window.geometry("500x300")

l4=Label(window,text="Do you want to:", font="Arial")
l4.grid()
b1=Button(window,text="Login",command=Login)
b1.grid()
b2=Button(window,text="Sign Up", command=Signup)
b2.grid()



window.mainloop()