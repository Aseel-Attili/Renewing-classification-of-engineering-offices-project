import customtkinter as ctk
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
app = ctk.CTk()
app.title('Founders Information')
app.geometry('900x345')
app.config(bg = '#161C25')
app.resizable(False , False)
font1 = ('Arial' , 20 , 'bold')
font2 = ('Arial' , 16 , 'bold')
name_label = ctk.CTkLabel(app, font = font1, text = 'Name:', text_color='yellow', bg_color='#161C25')
name_label.place(x = 20 , y = 20)
name_entry = ctk.CTkEntry(app, font = font1, text_color='#000',fg_color='#fff',border_color='#0C9295', border_width=2, width = 180)
name_entry.place(x = 180 , y = 20)
worker_id_label = ctk.CTkLabel(app, font = font1, text = 'Worker-ID:', text_color='yellow', bg_color='#161C25')
worker_id_label.place(x = 20 , y = 80)
worker_id_entry = ctk.CTkEntry(app, font = font1, text_color='#000',fg_color='#fff',border_color='#0C9295', border_width=2, width = 180)
worker_id_entry.place(x = 180 , y = 80)
Scientific_Qualification_label = ctk.CTkLabel(app, font = font1, text = 'Scientific qualification:', text_color='yellow', bg_color='#161C25')
Scientific_Qualification_label.place(x = 461 , y = 20)
Scientific_Qualification_entry = ctk.CTkEntry(app, font = font1, text_color='#000',fg_color='#fff',border_color='#0C9295', border_width=2, width = 180)
Scientific_Qualification_entry.place(x = 700 , y = 20)
Job_title_label = ctk.CTkLabel(app, font = font1, text = 'Job title:', text_color='yellow', bg_color='#161C25')
Job_title_label.place(x = 595 , y = 80)
Job_title_entry = ctk.CTkEntry(app, font = font1, text_color='#000',fg_color='#fff',border_color='#0C9295', border_width=2, width = 180)
Job_title_entry.place(x = 700 , y = 80)
def add_to_treeview():
    nm = name_entry.get()
    sq = Scientific_Qualification_entry.get()
    wi = worker_id_entry.get()
    jt = Job_title_entry.get()
    tree.insert('', "end", values=(nm,wi,sq,jt))
def insert_button_function():
    print('insert button is pressed')
    add_to_treeview()
def on_enter(event):
    insert_button.invoke()
insert_button = ctk.CTkButton(app, font = font1, text_color='#fff', text = 'Insert Data', fg_color='#05A312', hover_color='#00850B', bg_color='#161C25', cursor = 'hand2', corner_radius=15,width = 260, command = insert_button_function)
insert_button.place(x =17 ,y =294)
app.bind("<Return>", on_enter)
def nextPage():
    print('go to the next page')
next_button = ctk.CTkButton(app, font = font1, text_color='#fff', text = 'Next Page', fg_color='#161C25', hover_color='#FF5002', bg_color='#161C25',border_color='#F15704',border_width=2, cursor = 'hand2', corner_radius=15, width = 260, command = nextPage)
next_button.place(x =320 ,y =294)
def finishing():
    app.destroy()
close_button = ctk.CTkButton(app, font = font1, text_color='#fff', text = 'Close', fg_color='#E40404', hover_color='#AE0000', bg_color='#161C25',border_color='#E40404',border_width=2, cursor = 'hand2', corner_radius=15, width = 260, command = finishing)
close_button.place(x =623 ,y =294)
style = ttk.Style(app)
style.theme_use('clam')
style.configure('Treeview', font = font2, foreground = '#fff', background = '#000',fieldbackground = '#313837', rowheight=40)# Increase font size for Treeview structure via rowheight
style.configure('Treeview.Heading', font=('Arial', 18))# Increase the font size for column names
style.map('Treeview', background = [('selected', '#1A8F2D')])
tree = ttk.Treeview(app,height = 3)
tree['columns'] = ('name', 'Worker-ID' , 'Scientific_Qualification', 'Job title')
tree.column('#0', width = 0, stretch= tk.NO) # to hide the default first column of the treeview
tree.column('name', anchor = tk.CENTER, width = 269)
tree.column('Worker-ID', anchor = tk.CENTER, width = 269)
tree.column('Scientific_Qualification', anchor = tk.CENTER, width = 269)
tree.column('Job title', anchor = tk.CENTER, width = 269)
tree.heading('name',text = 'name')
tree.heading('Worker-ID',text = 'Worker-ID')
tree.heading('Scientific_Qualification',text = 'Scientific_Qualification')
tree.heading('Job title',text = 'Job title')
tree.place(x =22, y = 180 )
app.mainloop()