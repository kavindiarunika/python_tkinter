import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title("Login form")
root.geometry("340x440")
root.configure(bg='#333333')

frame=tk.Frame(bg='#333333')

def login():
    username="johnSmith"
    password="1234"
    if(usertname_entry.get()==username and password_entry.get() == password):
          messagebox.showinfo(title="login success",message="you successfully logged in" )
           
    else:
      messagebox.showinfo(title="invalid" ,message="invalid loggin")
        
login_lable = tk.Label(frame,text="Login",bg='#333333',fg='#a1157d',font=("Arial",25))
username_Label=tk.Label(frame,text="Username",bg='#333333',fg='#ffffff',font=("Arial",20))
usertname_entry = tk.Entry(frame,font=("Arial",20))
password_entry =tk.Entry(frame,show="*",font=("Arial",20))
password_label = tk.Label(frame,text="password",bg='#333333',fg='#ffffff',font=("Arial",20))
login_button=tk.Button(frame,text="login",bg='#C70039',fg='#ffffff',font=("Arial",16),command=login)


login_lable.grid(row = 0 , column= 0 ,columnspan=2,sticky="news",pady=40)
username_Label.grid(row=3, column= 0)
usertname_entry.grid(row= 3 , column=1,pady=20)
password_label.grid(row=4,column=0)
password_entry.grid(row=4,column=1,pady=20)
login_button.grid(row=5,column= 0 , columnspan=2,pady=20)




frame.pack()


frame.mainloop()



