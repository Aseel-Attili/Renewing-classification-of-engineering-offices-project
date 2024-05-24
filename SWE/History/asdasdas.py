import customtkinter as ctk
from tkinter import messagebox
from tkinter import PhotoImage
import sqlite3
import os
from Dictionary import Word
import office_official_one


File = 'DataBase.db'
if not os.path.exists(File):
    connection = sqlite3.connect(File)
    
    #-------------------------------------------
    # [1] Create Office Table 
    # ------------------------------------------
    connection.execute('''CREATE TABLE IF NOT EXISTS Office(Office_Name TEXT NOT NULL,
                                                            Classification_Number INTEGER PRIMARY KEY,
                                                            Office_Specialization TEXT NOT NULL,
                                                            Rank TEXT NOT NULL,
                                                            Date_of_Establishment TEXT NOT NULL,
                                                            Request_Renewing_Year INTEGER NOT NULL,
                                                            Office_Annual_subscription INTEGER,
                                                            Office_Outstanding_loans INTEGER,
                                                            Other_financial_receivables INTEGER,
                                                            City_OR_Town Text NOt NULL,
                                                            Street_OR_Bulding Text NOt NULL,
                                                            Telphone_Number Interger Unique,
                                                            Cellular_Number Interger Unique NOT NULL,
                                                            Fax_Number Interger Unique,
                                                            Postal_Code Text NOT NULL,
                                                            Email Text NOT NULL Unique,
                                                            Office_Area Real NOT NULL);        
                       ''')
    #-------------------------------------------
    # [2] Create Engineers Table 
    # ------------------------------------------
    connection.execute('''CREATE TABLE IF NOT EXISTS Engineers(Registration_Number INTEGER PRIMARY KEY,
                                                               Eng_First_Name TEXT NOT NULL,
                                                               Eng_Middle_Name TEXT NOT NULL,
                                                               Eng_Last_Name TEXT NOT NULL,
                                                               Eng_Specializations TEXT NOT NULL,
                                                               Graduation_Year INTEGER NOT NULL,
                                                               Eng_Annual_subscription INTEGER,
                                                               Eng_Outstanding_loans INTEGER,
                                                               Classification_Number INTEGER NOT NULL,
                                                               Job_title TEXT NOT NULL,
                                                               FOREIGN KEY (Classification_Number) REFERENCES Office(Classification_Number) ON DELETE CASCADE ON UPDATE CASCADE);
                       ''')
    #-------------------------------------------
    # [3] Create Founders Table 
    # ------------------------------------------
    connection.execute('''CREATE TABLE IF NOT EXISTS Founders(F_First_Name TEXT NOT NULL, 
                                                              F_Middle_Name TEXT NOT NULL,
                                                              F_Last_Name TEXT NOT NULL,
                                                              F_ID INTEGER PRIMARY KEY,
                                                              Classification_Number INTEGER NOT NULL,
                                                              FOREIGN KEY (Classification_Number) REFERENCES Office(Classification_Number) ON DELETE CASCADE ON UPDATE CASCADE);
                       ''')
    #-------------------------------------------
    # [4] Create Engineers – Founders  Table 
    # ------------------------------------------
    connection.execute('''CREATE TABLE IF NOT EXISTS Eng_Fnd(Eng_Registration_Number INTEGER PRIMARY KEY,
                                                             F_ID INTEGER UNIQUE);
                       ''')
    #-------------------------------------------
    # [5] Create Workers other than engineers Table 
    # ------------------------------------------
    connection.execute('''CREATE TABLE IF NOT EXISTS Workers(W_First_Name TEXT NOT NULL,
                                                             W_Middle_Name TEXT NOT NULL,
                                                             W_Last_Name TEXT NOT NULL,
                                                             W_ID INTEGER PRIMARY KEY,
                                                             Job_title TEXT NOT NULL,
                                                             Scientific_Qualification TEXT,
                                                             Classification_Number INTEGER NOT NULL,
                                                             FOREIGN KEY (Classification_Number) REFERENCES Office(Classification_Number) ON DELETE CASCADE ON UPDATE CASCADE);
                       ''')
    #-------------------------------------------
    # [6] Create Final Decision Table 
    # ------------------------------------------
    connection.execute('''CREATE TABLE IF NOT EXISTS Final_Decision(Session_Number INTEGER PRIMARY KEY,
                                                                    Session_Date TEXT NOT NULL,
                                                                    Final_Decision BOOLEAN NOT NULL,
                                                                    Head_of_the_Authority TEXT NOT NULL);
                       ''')
    #-------------------------------------------
    # [7] Create Office – Final Table 
    # ------------------------------------------
    connection.execute('''CREATE TABLE IF NOT EXISTS Office_Final(Session_Number INTEGER,
                                                                  Classification_Number INTEGER,
                                                                  PRIMARY KEY(Session_Number,Classification_Number),
                                                                  FOREIGN KEY (Session_Number) REFERENCES Final_Decision(Session_Number) ON DELETE CASCADE ON UPDATE CASCADE,
                                                                  FOREIGN KEY (Classification_Number) REFERENCES Office(Classification_Number) ON DELETE CASCADE ON UPDATE CASCADE);
                       ''')                   
    #-------------------------------------------
    # [8] Bill Table 
    # ------------------------------------------
    connection.execute('''CREATE TABLE IF NOT EXISTS Bill(Bill_Number INTEGER PRIMARY KEY,
                                                          Bill_Date TEXT NOT NULL,
                                                          Fees_paid INTEGER NOT NULL,
                                                          Classification_Number INTEGER NOT NULL,
                                                          FOREIGN KEY (Classification_Number) REFERENCES Office(Classification_Number) ON DELETE CASCADE ON UPDATE CASCADE);
                       ''')                   
    #-------------------------------------------
    # [9] Users Table 
    # ------------------------------------------
    connection.execute('''CREATE TABLE IF NOT EXISTS Users(Login_ID INTEGER PRIMARY KEY,
                                                           Password TEXT NOT NULL,
                                                           Class TEXT NOT NULL,
                                                           User_Name Text NOT NULL);
                                            
                       ''')                  
    #-------------------------------------------
    # [10] Create Office – Login Table 
    # ------------------------------------------
    connection.execute('''CREATE TABLE IF NOT EXISTS Office_Login(Login_ID INTEGER,
                                                                  Classification_Number INTEGER,
                                                                  PRIMARY KEY(Login_ID,Classification_Number),
                                                                  FOREIGN KEY (Login_ID) REFERENCES Users(Login_ID) ON DELETE CASCADE ON UPDATE CASCADE,
                                                                  FOREIGN KEY (Classification_Number) REFERENCES Office(Classification_Number) ON DELETE CASCADE ON UPDATE CASCADE);
                       ''') 
    connection.commit()
    connection.close()
    

# Set the appearance mode and default color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# Create the main application window
app = ctk.CTk()

''' *********************************************** '''
''' Login DEf'''
''' *********************************************** '''



def LogIn_GUI():  
    # Set window dimensions
    window_width = 777
    window_height = 600

    # Get screen dimensions
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()

    # Calculate the x and y coordinates for the window to be centered
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2

    # Set window geometry to be centered on the screen
    app.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    app.title("Login UI")
    
    ''' *********************************************** '''
    ''' open_second DEf'''
    ''' *********************************************** '''
    
    def open_second_gui():
        app.withdraw()  # Hide the login GUI
        office_official_one.office_official_one()
    
    ''' *********************************************** '''
    ''' check DEf'''
    ''' *********************************************** '''
    
    def check():
        connection = sqlite3.connect(File)
        cursor = connection.cursor()
        
        ID = user_entry.get()
        Pass = user_pass.get()
        
        if ID == "":
            messagebox.showwarning(title='Empty Field', message='Please check your ID')
            return 
        
        elif Pass == "":
            messagebox.showwarning(title='Empty Field', message='Please check your Password')
            return 
        
        else:
            try:
                # Convert the text to an integer
                user_id = int(ID)
            
            except ValueError:
                messagebox.showwarning(title='Wrong ID', message='Please check your ID')
                return
            
            cursor.execute(""" select * from Users where Login_ID = ?""" , (user_id,))
            find = cursor.fetchone()
            if find == None:
                messagebox.showerror(title='Wrong ID', message='Please check your ID')
                return
            
            cursor.execute(""" select Password from Users where Login_ID = ?""" , (user_id,))
            find = cursor.fetchone()[0]
            if find != Pass:
                messagebox.showerror(title='Wrong Password', message='Please check your Password')
                return
            
            Word["User_ID"] = user_id
            
            cursor.execute(""" select Class from Users where Login_ID = ?""" , (user_id,))
            Word["User_Class"]= cursor.fetchone()[0]
            
            cursor.execute(""" select User_Name from Users where Login_ID = ?""" , (user_id,))
            Word["User_Name"] = cursor.fetchone()[0]
            
            if ID[0] == 1 and ID[1] == 1:
                open_second_gui()
                
                
                
                

            
    ''' *********************************************** '''
    ''' set_background_image DEf'''
    ''' *********************************************** '''
        
    # Function to set background image
    def set_background_image():
        # Load the background image
        image_path = "pattern.png"  # Replace with the actual path to your PNG image
        background_image = PhotoImage(file=image_path)
        # Create a label to display the background image
        background_label = ctk.CTkLabel(app)
        background_label.place(relwidth=1, relheight=1)  # Cover the entire window

        # Send the label to the back so other widgets are visible
        background_label.lower()
        
   

    # Call the function to set the background image
    set_background_image()

    # Create a CTkFont object with a modern sign-like font
    custom_font = ctk.CTkFont(family="Bauhaus 93", size=25)

    # Create the label and apply the style
    label = ctk.CTkLabel(app, text="Syndicate System", font=custom_font)
    label.pack(pady=20)

    frame = ctk.CTkFrame(master=app)
    frame.pack(pady=20, padx=40, fill='both', expand=True)

    label = ctk.CTkLabel(master=frame, text='LogIn to your account')
    label.pack(pady=12, padx=10)

    user_entry = ctk.CTkEntry(master=frame, placeholder_text="ID")
    user_entry.pack(pady=12, padx=10)

    user_pass = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
    user_pass.pack(pady=12, padx=10)

    button = ctk.CTkButton(master=frame, text='Login',command=check)
    button.pack(pady=12, padx=10)

''' *********************************************** '''
''' main'''
''' *********************************************** ''' 


LogIn_GUI()

app.mainloop()
   
    
    
    