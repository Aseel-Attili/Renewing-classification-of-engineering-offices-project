import customtkinter as ctk
import tkinter.messagebox as tkmb
from tkinter import PhotoImage

# Set the appearance mode and default color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# Create the main application window
app = ctk.CTk()

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

# Function to set background image
def set_background_image():
    # Load the background image
    image_path = "C:/Users/coldw/Desktop/best login gui/pattern.png"  # Replace with the actual path to your PNG image
    background_image = PhotoImage(file=image_path)

    # Create a label to display the background image
    background_label = ctk.CTkLabel(app, image=background_image)
    background_label.place(relwidth=1, relheight=1)  # Cover the entire window

    # Send the label to the back so other widgets are visible
    background_label.lower()

# Call the function to set the background image
set_background_image()

# Function to handle login
def login():
    username = "Geeks"
    password = "12345"
    new_window = ctk.CTkToplevel(app)
    new_window.title("New Window")
    new_window.geometry("500x500")

    if user_entry.get() == username and user_pass.get() == password:
        tkmb.showinfo(title="Login Successful", message="You have logged in Successfully")
        ctk.CTkLabel(new_window, text="GeeksforGeeks is best for learning ANYTHING !!").pack()
    
    elif user_entry.get() == username and user_pass.get() != password:
        tkmb.showwarning(title='Wrong password', message='Please check your password')
    
    elif user_entry.get() != username and user_pass.get() == password:
        tkmb.showwarning(title='Wrong username', message='Please check your username')
    
    else:
        tkmb.showerror(title="Login Failed", message="Invalid Username and password")


# Create a CTkFont object with a modern sign-like font
custom_font = ctk.CTkFont(family="Bauhaus 93", size=25)

# Create the label and apply the style
label = ctk.CTkLabel(app, text="Syndicate System", font=custom_font)
label.pack(pady=20)

frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=40, fill='both', expand=True)

label = ctk.CTkLabel(master=frame, text='Modern Login System UI')
label.pack(pady=12, padx=10)

user_entry = ctk.CTkEntry(master=frame, placeholder_text="Username")
user_entry.pack(pady=12, padx=10)

user_pass = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
user_pass.pack(pady=12, padx=10)

button = ctk.CTkButton(master=frame, text='Login', command=login)
button.pack(pady=12, padx=10)

checkbox = ctk.CTkCheckBox(master=frame, text='Remember Me')
checkbox.pack(pady=12, padx=10)

# Start the main loop
app.mainloop()
