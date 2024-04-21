import tkinter as tk
from tkinter import messagebox as msgbox


#create main window
root= tk.Tk()
root.title("Delivery information")
root.geometry("500x300")

#Create Weight label and entry
weight_label = tk.Label(root, text ="Enter weight of your package(Kg) :")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

#create password label and entry
location_label = tk.Label(root, text ='''Enter 1 for Ibeju lekki,Enter 2 for Epe :''')
location_label.pack()
location_entry = tk.Entry(root)
location_entry.pack()

result_label = tk.Label(root, text="")
result_label.pack()


#handling button click event
def button_click():
    weight = int(weight_entry.get())
    location = int(location_entry.get())
    #show an information message box
    
    if weight >= 10 and location == 1:
        result_label.config(text="\n Your delivery fee is N5,000")
    elif weight < 10 and location == 1:
        result_label.config(text="\n Your delivery fee is N3,500")
    elif weight >= 10 and location == 2:
        result_label.config(text="\nYour delivery fee is N10,000")
    elif weight < 10 and location == 2:
        result_label.config(text="\nYour delivery fee is N5,000")
    else :
        msgbox.showinfo(''' Unfortunately your request is unavailable''')

#button widget
button = tk.Button(root, text="Enter", command=button_click)
button.pack()

#Run the main event loop
root.mainloop()



