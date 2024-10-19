import tkinter as tk
from tkinter import ttk
import pycountry

root=tk.Tk()
root.title("data entry form")
root.geometry('500x500')

frame = tk.Frame(root)
frame.pack()

counties=[country.name for country in pycountry.countries]

user_info_frame = tk.LabelFrame(frame,text="user information")
user_info_frame.grid(row=0 , column=0,sticky="news")

fname_label=tk.Label(user_info_frame,text="First Name" )
fname_label.grid(row=0,column=0)
lname_label=tk.Label(user_info_frame,text="last Name")
lname_label.grid(row=0 ,column=1)

fname_entry=tk.Entry(user_info_frame)
fname_entry.grid(row=1,column=0)
lname_entry=tk.Entry(user_info_frame)
lname_entry.grid(row=1,column=1)

title_label=tk.Label(user_info_frame,text="title")
title_combobox=ttk.Combobox(user_info_frame,values=["Mr.","Mrs","Ms."])
title_label.grid(row=0,column=2)
title_combobox.grid(row=1 , column=2)

age_label=tk.Label(user_info_frame,text="Age")
age_label.grid(row=3,column=0)
age_spinbox = tk.Spinbox(user_info_frame,from_=2,to=110)
age_spinbox.grid(row=4,column=0)

nationality_label=tk.Label(user_info_frame,text="Nationality")
nationality_label.grid(row=3,column=1)
nationality_combbox=ttk.Combobox(user_info_frame,values=counties)
nationality_combbox.set("select a country")
nationality_combbox.grid(row=4,column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)


course_frame = tk.LabelFrame(frame,text="registation status")
course_frame.grid(row=1,column=0,sticky="news")

registered_label = tk.Label(course_frame,text="Registration Status")
registered_label.grid(row=0 , column=0)
registered_check = tk.Checkbutton(course_frame,text="currentty Registerd")
registered_check.grid(row=1 ,column=0)

numcourses_label=tk.Label(course_frame,text="# completed courses")
numcourses_spinbox=tk.Spinbox(course_frame,from_=0 , to='infinity')
numcourses_label.grid(row=0,column=1)
numcourses_spinbox.grid(row=1,column=1)

for widget in course_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

terms_frame = tk.LabelFrame(frame,text="terms & conditions")
terms_frame.grid(row= 2 , column=0 , sticky="news")

terms_check =tk.Checkbutton(terms_frame,text="i accept the term and conditions")
terms_check.grid(row=0 , column=0)

for widget in terms_frame.winfo_children():
    widget.grid_configure(padx=10 , pady=5)


button = tk.Button(frame ,text="Enter data")
button.grid(row=3 , column=0,sticky="news") 

root.mainloop()