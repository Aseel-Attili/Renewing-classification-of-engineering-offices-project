import sqlite3
import os

File = 'DataBase.db'
if not os.path.exists(File):
    connection = sqlite3.connect(File)
    
    #-------------------------------------------
    # [1] Create Office Table 
    # ------------------------------------------
    connection.execute('''CREATE TABLE IF NOT EXISTS Office(Office_Name TEXT NOT NULL,
                                                            Classification_Number INTEGER PRIMARY KEY,
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

    def add_office_entry():
    connection = sqlite3.connect(File)
    cursor = connection.cursor()
    print("plz enter these value:")
    
    Office_name = input("Office name: ")
    
    Classification_number = input("Classification number: ")
    
    Office_specialization = input("Office specialization: ")
    
    Rank = input("Rank ")
    
    Date_of_Establishment = input("Date of establishment: ")
    
    Request_Renewing_Year = input("Request renewing year: ")
    
    Office_Annual_subscription = input("Office annual subscription: ")
    
    Office_Outstanding_loans = input("Office Outstanding loans: ")
    
    Other_financial_receivables = input("Other financial receivables: ")
    
    City_OR_Town = input("City/Town: ")
    
    Street_OR_Bulding = input("Street/Bulding: ")
    
    Telphone_Number = input("Telphone number: ")
    
    Cellular_Number = input("Cellular number: ")
    
    Fax_Number = input("Fax number: ")
    
    Postal_Code = input("Postal code: ")
    
    Email = input("Email: ")
    
    Office_Area = input("Office area: ")
    
    try:
        cursor.execute("""insert into Office(Office_Name, Classification_Number, Office_Specialization,Rank,Date_of_Establishment,Request_Renewing_Year,Office_Annual_subscription,Office_Outstanding_loans,Other_financial_receivables,City_OR_Town,Street_OR_Bulding,Telphone_Number,Cellular_Number,Fax_Number,Postal_Code,Email,Office_Area) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",(Office_name,Classification_number,Office_specialization,Rank,Date_of_Establishment,Request_Renewing_Year,Office_Annual_subscription,Office_Outstanding_loans,Other_financial_receivables,City_OR_Town,Street_OR_Bulding,Telphone_Number,Cellular_Number,Fax_Number,Postal_Code,Email,Office_Area))
        print("the office " + Office_name  + " added successfully")
        connection.commit()
        
    except sqlite3.IntegrityError as e:
        print("you entered an existing user(an existing userID)! ,please re-enter a non existing one.")