import tkinter as tk
from tkinter import messagebox

#create main window

#Create weight label and entry
weight_label = tk.Label(root, text ="what is the weight?:")
weight_label.pack()
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

