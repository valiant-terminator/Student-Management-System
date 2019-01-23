import tkinter as tk
import sqlite3
from tkinter import ttk
from tkinter import *

name1:str = ""
college1:str = ""
address1:str = ""
phone1:int = 0


class Student:
    def __init__(self):
            mainWindow=tk.Tk()
            mainWindow.title("Student Management System")
            mainWindow.geometry("800x500+400+100")

            heading1=tk.Label(mainWindow,text="Welcome to Student Management System!!",fg="green")
            heading1.grid()
            heading1.config(font=("Courier",20))


            heading2=tk.Label(mainWindow,text="Enter Student Name::")
            heading2.grid(row=1,column=0)
            Name=tk.Entry(mainWindow)
            Name.grid(row=1,column=4,pady=(0, 10))

            heading3=tk.Label(mainWindow,text="Enter Student's College::")
            heading3.grid(row=4,column=0,pady=(0, 10))
            College=tk.Entry(mainWindow)
            College.grid(row=4,column=4)

            heading4 = tk.Label(mainWindow, text="Enter Student's Address::")
            heading4.grid(row=7,column=0,pady=(0, 10))
            Address = tk.Entry(mainWindow)
            Address.grid(row=7,column=4)

            heading5=tk.Label(mainWindow, text="Enter Student's PhoneNo.::")
            heading5.grid(row=10,column=0,pady=(0, 10))
            PhoneNo=tk.Entry(mainWindow)
            PhoneNo.grid(row=10,column=4)

            def getvalues():
                global name1, college1, address1, phone1
                name1=(Name.get())
                college1=(College.get())
                address1=(Address.get())
                phone1=int(PhoneNo.get())
                getinfo(name1,college1,address1,phone1)
                Name.delete('0',tk.END)
                College.delete('0',tk.END)
                Address.delete('0',tk.END)
                PhoneNo.delete('0',tk.END)

                #print("The Name of the Student is:",name1,"\nThe Course Student had Opted is:",course1,"\nThe PhoneNo of Student is:",phone1)

            button1=tk.Button(mainWindow,text="Submit",fg="red",command=lambda: getvalues())
            button1.grid(row=13,column=0,pady=(0, 10))

            button2=tk.Button(mainWindow, text="Show Values",fg="red",command=lambda: showvalues())
            button2.grid(row=15,column=0)

            def showvalues():

                connection = sqlite3.connect("student1.db")  # file name
                print("Database opened successfully")

                TABLE_NAME = "student_table"
                STUDENT_ID = "student_id"
                STUDENT_NAME = "student_name"
                STUDENT_COLLEGE = "student_college"
                STUDENT_ADDRESS = "student_address"
                STUDENT_PHONE = "student_phone"

                connection.execute(
                    " CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + STUDENT_ID + " INTEGER PRIMARY KEY AUTOINCREMENT, " + STUDENT_NAME +
                    " TEXT, " + STUDENT_COLLEGE + " TEXT, " + STUDENT_ADDRESS + " TEXT, " + STUDENT_PHONE + " INTEGER); ")

                secondWindow=tk.Tk()

                secondWindow.title("Display Results")

                appLabel=tk.Label(secondWindow,text="Student Management System",fg="green")
                appLabel.config(font=("Sylfaen",30))
                appLabel.pack()

                tree = ttk.Treeview(secondWindow)
                tree["columns"]=("one","two","three","four")

                tree.heading("one",text="Student Name")
                tree.heading("two",text="College Name")
                tree.heading("three",text="Address")
                tree.heading("four",text="Phone Number")

                cursor=connection.execute(" SELECT * FROM "+ TABLE_NAME +" ;")
                i=0

                for row in cursor:
                    tree.insert('',i,text=" Student "+ str(row[0]), values=(row[1], row[2], row[3], row[4]))
                    i=i+1

                tree.pack()

            def getinfo(name2,college2,address2,phone2):
                connection = sqlite3.connect("student1.db")  # file name
                print("Database opened successfully")

                TABLE_NAME = "student_table"
                STUDENT_ID = "student_id"
                STUDENT_NAME = "student_name"
                STUDENT_COLLEGE = "student_college"
                STUDENT_ADDRESS = "student_address"
                STUDENT_PHONE = "student_phone"

                connection.execute(
                    " CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + STUDENT_ID + " INTEGER PRIMARY KEY AUTOINCREMENT, " + STUDENT_NAME +
                    " TEXT, " + STUDENT_COLLEGE + " TEXT, " + STUDENT_ADDRESS + " TEXT, " + STUDENT_PHONE + " INTEGER); ")
                print("TABLE CREATED SUCCESSFULLY.")

            # insert new record
            # connection.execute("INSERT INTO "+ TABLE_NAME + " ( " + STUDENT_NAME + ", " + STUDENT_COLLEGE + ", " + STUDENT_ADDRESS + ", " +
            #                    STUDENT_PHONE + " ) VALUES ( 'ABHAY','U.P.E.S.','DEHRADUN,UTTRAKHAND',9760389540 ); ")
            # connection.commit()

                print(name2,college2,address2,phone2)
                connection.execute(
                    "INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + ", " + STUDENT_COLLEGE + ", " + STUDENT_ADDRESS + ", " +
                    STUDENT_PHONE + " ) VALUES ( '" + name2 + "','" + college2 + "','" + address2 + "','" + str(phone2) + "' ); ")
                connection.commit()
                print("Record Added Successfully.")
                check=1
                if(check==1):
                    heading6 = tk.Label(mainWindow, text="Record Entered Successfully!!")
                    heading6.grid(row=15, column=4)
                else:
                    heading6 = tk.Label(mainWindow, text="Error!!")
                    heading6.grid(row=15, column=4)


            mainWindow.mainloop()


b = Student()




