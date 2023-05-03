import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk

 # Create a connection to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="attendance"
)

# Create a cursor to execute MySQL commands
mycursor = mydb.cursor()
class Attendance:
    def __init__(self):   
         #---------------Initial Window-------#
        self.root=tk.Tk()
        #-----------variables for all the interface-------------#
        self.username_for_login_var=tk.StringVar() #for login only
        self.password_for_login_var=tk.StringVar() #for login only
        self.password_for_signup_var=tk.StringVar() #for signup only
        #----title-----#
        self.root.title("Attendance Management System")
        #----geometry----#
        self.root.geometry('500x300')
        #-----resizeable----#
        self.root.resizable(False,False)
        #----title of this program----#
        title_of_this_program=tk.Label(self.root,text="Attendance Management System",font=('sans serif',10),fg='blue')
        title_of_this_program.place(x=250,y=10)
        #--------labels and titles for login------#
        username_login_label=tk.Label(self.root,text="Username")
        username_login_label.place(x=300,y=40)
        username_login_entry=ttk.Entry(self.root,textvariable=self.username_for_login_var)
        username_login_entry.place(x=270,y=60)
        username_login_entry.focus()
        #------labels and entry for passwords-----#
        password_login_label=tk.Label(self.root,text="Password")
        password_login_label.place(x=300,y=90)
        password_login_entry=ttk.Entry(self.root,textvariable=self.password_for_login_var,show="*")
        password_login_entry.place(x=270,y=110)
        
        image1 = Image.open("Aha-Soft-Security-Secrecy.256.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tk.Label(image=test)
        label1.image = test
        label1.place(x=-10, y=0)
        #----------callback functions------#

        def login():
            self.loggedin(self.username_for_login_var.get(),self.password_for_login_var.get())
        def signup():
            self.signup()
        #------loginbutton----------#
        login_button=ttk.Button(self.root,text="Login",command=login)
        login_button.place(x=295,y=140)
        #-----signupbutton---------#
        signup_button=ttk.Button(self.root,text="Signup",command=signup)
        signup_button.place(x=295,y=170)
        #----------database connection-----------#
        try:
            self.connection = mysql.connector.connect(host="localhost",password="",username="root",database="attendance")
        except:
            messagebox.showerror("Database not found","Couldnot connect to database")
            self.root.destroy()
        self.root.mainloop()
    def loggedin(self,username,password):
       cursor = self.connection.cursor()
       query=f"SELECT * FROM admins where username='{username}' and password='{password}'"
       try:
           cursor.execute(query)
           data = cursor.fetchone()
           if data[0]==username and data[1]==password:
               messagebox.showinfo("Sucess","Login Sucess")
               self.login_sucess(data[0])
           else:
               messagebox.showerror("Login Failed","Please Check your Details Again")
       except:
           messagebox.showerror("Login Failed","Your Account Doesnot exists")
    def signup(self):
        #-----signup interface--------#
        signup_interface=tk.Tk()
        #-----variables for signup----#
        self.username_for_signup_var=tk.StringVar() #for signup only
        #-------title-----------#
        signup_interface.title("Create Account")
        #----geometry-----#
        signup_interface.geometry('300x300')
        signup_interface.resizable(False,False)
        #-------lables for username and entry------#
        username_for_signup_label=tk.Label(signup_interface,text="Define Username")
        username_for_signup_label.place(x=105,y=40)
        username_entry_for_signup=ttk.Entry(signup_interface,textvariable=self.username_for_signup_var)
        username_entry_for_signup.place(x=90,y=60)
        #-------------lables for password and entry-----#
        password_for_signup_label=tk.Label(signup_interface,text="Define Password")
        password_for_signup_label.place(x=105,y=90)
        password_entry_for_signup=ttk.Entry(signup_interface,textvariable=self.password_for_signup_var,show="*")
        password_entry_for_signup.place(x=90,y=110)
        #----callback function----#
        def createaccount():
            self.createaccountwithus(username_entry_for_signup.get(),password_entry_for_signup.get())
        #-----create account button------#
        create_account_button=ttk.Button(signup_interface,text="Create Account",command=createaccount)
        create_account_button.place(x=105,y=140)
        signup_interface.mainloop()
    def createaccountwithus(self,username,password):
        if username and password:
            if username.isalpha()==True:
                query=f"INSERT INTO admins values('{username}','{password}')"
                cursor=self.connection.cursor()
                try:
                    cursor.execute(query)
                    messagebox.showinfo("Account Created","Account Created Sucess,Proceed towards login")
                    self.connection.commit()
                except:
                    messagebox.showerror("Username already in use","This username is already in use choose another username")
            else:
                messagebox.showerror("Username Error","Username must be alphabet")
        else:
            messagebox.showerror("Required","Username and Password Required")
    def login_sucess(self,username):
        self.root.destroy()
    
if __name__=="__main__":
  a= Attendance()

# Create a connection to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="attendance"
)

# Create a cursor to execute MySQL commands
mycursor = mydb.cursor()

# Create the Attendance System GUI
root = tk.Tk()
root.title("Attendance Management System")

# Create a form for the user to enter their name and select their attendance status
tk.Label(root, text="Name:").grid(row=0)
tk.Label(root, text="Division:").grid(row=1)
tk.Label(root, text="Sem:").grid(row=2)
tk.Label(root, text="Subject:").grid(row=3)

tk.Label(root, text="Attendance Status").grid(row=4)

name_entry = tk.Entry(root)
division_entry = tk.Entry(root)
Sem_entry = tk.Entry(root)
Subject_entry = tk.Entry(root)
attendance_status_var = tk.StringVar(value="Absent")

attendance_status_present = tk.Radiobutton(root, text="Present", variable=attendance_status_var, value="Present")
attendance_status_absent = tk.Radiobutton(root, text="Absent", variable=attendance_status_var, value="Absent")

name_entry.grid(row=0, column=1)
division_entry.grid(row=1, column=1)
Sem_entry.grid(row=2, column=1)
Subject_entry.grid(row=3, column=1)
attendance_status_present.grid(row=4, column=1)
attendance_status_absent.grid(row=4, column=2)

# Create a function to insert the attendance record into the MySQL database
def submit_attendance():
    name = name_entry.get()
    division = division_entry.get()
    sem = Sem_entry.get()
    Subject = Subject_entry.get()
    attendance_status = attendance_status_var.get()
    sql = "INSERT INTO attendance (Name,Division,Sem,Subject, Date, Attendance_Status) VALUES (%s,%s,%s,%s, CURDATE(), %s)"
    val = (name, division,sem,Subject,attendance_status)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

submit_button = tk.Button(root, text="Submit", command=submit_attendance)
submit_button.grid(row=5, column=1)

root.mainloop()

