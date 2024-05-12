#Attendance project
import tkinter as tk
import random

employees = ["Mary Evans", "Eyo Ishan", "Durojaiye Dare", "Adams Ali", "Andrew Ugwu", "Stella Mankinde", "Jane Akibo", "Ago James", "Michell Taiwo", "Abraham Jones" , "Nicole Anide", "Kosi Korso", "Adele Martins", "Emmanuel Ojo", "Ajayi Fatima"]
tasks = ["Loading", "Transporting", "Reveiwing Orders", "Customer Service", "Delivering Items"]

class Employee:
    def _init_(self, master):
        self.master = master
        self.master.title("Employee System")

        self.label = tk.Label(self.master, text="Enter your name:")
        self.label.pack()

        self.entry = tk.Entry(self.master)
        self.entry.pack()

        self.button = tk.Button(self.master, text="Submit", command=self.check_employee)
        self.button.pack()

    def check_employee(self):
        name = self.entry.get()
        if name in employees:
            self.take_attendance(name)
            self.assign_task(name)
        else:
            self.refuse_access()

    def take_attendance(self, name):
        print(f"{name} has taken attendance for the day.")

    def assign_task(self, name):
        task = random.choice(tasks)
        print(f"{name} has been assigned the task: {task}")

    def refuse_access(self):
        print("Access denied. Invalid employee.")
Employee()