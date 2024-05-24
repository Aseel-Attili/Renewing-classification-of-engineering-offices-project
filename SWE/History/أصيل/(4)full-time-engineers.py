import customtkinter as ctk
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
app = ctk.CTk()
app.title('Founders Information')
app.geometry('900x570')
app.config(bg = '#161C25')
app.resizable(False , False)
font1 = ('Arial' , 20 , 'bold')
font2 = ('Arial' , 16 , 'bold')
name_label = ctk.CTkLabel(app, font = font1, text = 'Name:', text_color='yellow', bg_color='#161C25')
name_label.place(x = 20 , y = 20)
name_entry = ctk.CTkEntry(app, font = font1, text_color='#000',fg_color='#fff',border_color='#0C9295', border_width=2, width = 180)
name_entry.place(x = 180 , y = 20)
specialization_label = ctk.CTkLabel(app, font = font1, text = 'Specialization:', text_color='yellow', bg_color='#161C25')
specialization_label.place(x = 20 , y = 80)
specialization_entry = ctk.CTkEntry(app, font = font1, text_color='#000',fg_color='#fff',border_color='#0C9295', border_width=2, width = 180)
specialization_entry.place(x = 180 , y = 80)
registration_number_label = ctk.CTkLabel(app, font = font1, text = 'Registration number:', text_color='yellow', bg_color='#161C25')
registration_number_label.place(x = 480 , y = 20)
registration_number_entry = ctk.CTkEntry(app, font = font1, text_color='#000',fg_color='#fff',border_color='#0C9295', border_width=2, width = 180)
registration_number_entry.place(x = 700 , y = 20)
graduation_year_label = ctk.CTkLabel(app, font = font1, text = 'Graduation year:', text_color='yellow', bg_color='#161C25')
graduation_year_label.place(x = 520 , y = 80)
graduation_year_entry = ctk.CTkEntry(app, font = font1, text_color='#000',fg_color='#fff',border_color='#0C9295', border_width=2, width = 180)
graduation_year_entry.place(x = 700 , y = 80)
def add_to_treeview():
    nm = name_entry.get()
    sp = specialization_entry.get()
    rg = registration_number_entry.get()
    gu = graduation_year_entry.get()
    tree.insert('', "end", values=(nm,sp,rg,gu))
def insert_button_function():
    print('insert button is pressed')
    add_to_treeview()
def on_enter(event):
    insert_button.invoke()
insert_button = ctk.CTkButton(app, font = font1, text_color='#fff', text = 'Insert Data', fg_color='#05A312', hover_color='#00850B', bg_color='#161C25', cursor = 'hand2', corner_radius=15,width = 260, command = insert_button_function)
insert_button.place(x =17 ,y =520)
app.bind("<Return>", on_enter)
def nextPage():
    print('go to the next page')
next_button = ctk.CTkButton(app, font = font1, text_color='#fff', text = 'Next Page', fg_color='#161C25', hover_color='#FF5002', bg_color='#161C25',border_color='#F15704',border_width=2, cursor = 'hand2', corner_radius=15, width = 260, command = nextPage)
next_button.place(x =320 ,y =520)
def finishing():
    app.destroy()
close_button = ctk.CTkButton(app, font = font1, text_color='#fff', text = 'Close', fg_color='#E40404', hover_color='#AE0000', bg_color='#161C25',border_color='#E40404',border_width=2, cursor = 'hand2', corner_radius=15, width = 260, command = finishing)
close_button.place(x =623 ,y =520)
style = ttk.Style(app)
style.theme_use('clam')
style.configure('Treeview', font = font2, foreground = '#fff', background = '#000',fieldbackground = '#313837', rowheight=40)# Increase font size for Treeview structure via rowheight
style.configure('Treeview.Heading', font=('Arial', 18))# Increase the font size for column names
style.map('Treeview', background = [('selected', '#1A8F2D')])
tree = ttk.Treeview(app,height = 10)
tree['columns'] = ('name', 'specialization' , 'registration number', 'Graduation year')
tree.column('#0', width = 0, stretch= tk.NO) # to hide the default first column of the treeview
tree.column('name', anchor = tk.CENTER, width = 269)
tree.column('specialization', anchor = tk.CENTER, width = 269)
tree.column('registration number', anchor = tk.CENTER, width = 269)
tree.column('Graduation year', anchor = tk.CENTER, width = 269)
tree.heading('name',text = 'name')
tree.heading('specialization',text = 'specialization')
tree.heading('registration number',text = 'registration number')
tree.heading('Graduation year',text = 'Graduation year')
tree.place(x =22, y = 180 )
app.mainloop()