import tkinter as tk
from tkinter import messagebox

# Function to display welcome message based on department
def welcomeMessage(username, department):
    window = tk.Toplevel(root)
    window.title("Admin Box")
    window.geometry("800x400")

    label_1 = tk.Label(window, text=f"Welcome {username}\n")
    label_1.pack()
    label_2 = tk.Label(window, text="These are the other members of your department")
    label_2.pack()

    # Display department members based on department
    if department == "Logistics":
        members = ["Adeniran Oluwatamilore", "Agbakwuru Chiemeziem", "Arnika Osose", "Chukuma Nedi", "Ezeonye Makuochukwu", "Giwa Moyosore", "Nwokolo Chijindu", "Nwokolo Joseph", "Okoro Derek", "Peter Owoede"]
    elif department == "Accounting":
        members = ["Adewumi Ayomide", "Agbakuru-Nwogu Chukwunonye", "Akinde Oluwatimehin", "Ebi Stephanie", "Icha Ayonete", "Ikpati Eche", "Obasogie Daisy", "Obi Samuel", "Obialor Betha", "Olowokere Akorede", "Olubuade Rasheed", "Osemeke Daniel"]
    elif department == "Delivery":
        members = ["Adoh-Ajagbe Oshim", "Atelly Daniel", "Azogu Onyekachi", "Beture Shalom", "Ejedimu Edward", "Iloenyosi Michael", "Iyawe Oluwadamilola", "Ogbonna Boluwatife", "Oigbochie Mary", "Quadri Oluwafikunmi", "Ude-Ibe Uchenna"]
    elif department == "Administration":
        members = ["Egboro Jason", "Eleri Otu", "Eze Onyinyechi", "Okocha-Ojeah Raphael", "Okolo Victor", "Umeh Ejike"]
    else:
        members = []

    members_text = "\n".join(members)
    label_3 = tk.Label(window, text=members_text)
    label_3.pack()

# Function to handle form submission
def submit():
    username = username_entry.get().strip().capitalize()
    department = password_entry.get().strip().capitalize()

    # Check if the username and password are valid
    if (username, department) in [("Oluwatamilore", "Logistics"), ("Chiemeziem", "Logistics"), ("Osose", "Logistics"), ("Nedi", "Logistics"), ("Makuochukwu", "Logistics"), ("Moyosore", "Logistics"), ("Chijindu", "Logistics"), ("Joseph", "Logistics"), ("Derek", "Logistics"), ("Owoede", "Logistics"), ("Mary-cynthia", "Logistics")]:
        welcomeMessage(username, department)
    elif (username, department) in [("Ayomide", "Accounting"), ("Chukwunonye", "Accounting"), ("Oluwatimehin", "Accounting"), ("Stephanie", "Accounting"), ("Ayonete", "Accounting"), ("Eche", "Accounting"), ("Daisy", "Accounting"), ("Samuel", "Accounting"), ("Betha", "Accounting"), ("Akorede", "Accounting"), ("Rasheed", "Accounting"), ("Daniel", "Accounting")]:
        welcomeMessage(username, department)
    elif (username, department) in [("Oshim", "Delivery"), ("Daniel", "Delivery"), ("Onyekachi", "Delivery"), ("Shalom", "Delivery"), ("Edward", "Delivery"), ("Michael", "Delivery"), ("Oluwadamilola", "Delivery"), ("Boluwatife", "Delivery"), ("Mary", "Delivery"), ("Oluwafikunmi", "Delivery"), ("Uchenna", "Delivery")]:
        welcomeMessage(username, department)
    elif (username, department) in [("Jason", "Administration"), ("Otu", "Administration"), ("Onyinyechi", "Administration"), ("Raphael", "Administration"), ("Victor", "Administration"), ("Ejike", "Administration")]:
        welcomeMessage(username, department)
    else:
        messagebox.showerror("Login", "Invalid username or department")

# Create main window
root = tk.Tk()
root.title("Login Form")
root.geometry("500x250")

# Create username label and entry
username_label = tk.Label(root, text="Firstname:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Create department label and entry
password_label = tk.Label(root, text="Department:")
password_label.pack()
password_entry = tk.Entry(root)
password_entry.pack()

# Create submit button
submit_button = tk.Button(root, text="Enter", command=submit)
submit_button.pack()

# Display warning message
warning_1 = tk.Label(root, text="Please, start every word with a capital letter")
warning_1.pack()

# Run the main event loop
root.mainloop()
