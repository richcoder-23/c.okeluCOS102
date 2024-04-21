import tkinter as tk
from tkinter import messagebox
'''from PIL import Image, ImageTk'''

def welcomeMessage(username):
    #create a tkinter window
    window = tk.Toplevel(root)
    window.title("Admin Box")
    window.geometry("500x200")

    label_1 = tk.Label(window, text=f"Welcome {username}\n")
    label_1.pack()
    label_2 = tk.Label(window, text="This is Python GUI with Tkinter")
    label_2.pack()


    # run the Tkinter even loop
    window.mainloop()

def submit():
    username = username_entry.get()
    password = password_entry.get() 

    if username == "Mary" and password == "cos102":
        welcomeMessage(username)
    else:
        messagebox.showerror("Login", "Invalid unsername or password")

# create main window 
root = tk.Tk()
root.title("Login Form")
root.geometry("500x200")


#Create username label and entry
username_label = tk.Label(root, text ="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

#create password label and entry
password_label = tk.Label(root, text ="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

#create submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

#Run the main event loop
root.mainloop()
