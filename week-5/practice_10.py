import tkinter as tk
from tkinter import messagebox as msgbox


#handling button click event
def button_click():
    #print("Button clicked!")

    #show an information message box
    msgbox.showinfo("Info", "Welcome to COS 102 GUI App!\n")

    #Ask for user confirmation
    result = msgbox.askyesno("Confirmation","Do you want to continue?")

#create the main window
root = tk.Tk()
root.title("Home page")
root.geometry("300x100")

#add a label widget
label = tk.Label(root, text="Hello Friend \n")
label.pack()

# add a button widget 
button = tk.Button(root, text="Click Me!", command=button_click)
button.pack()

# styling the button widget
button.config(fg="red", bg="yellow")

#start the event loop
root.mainloop()
