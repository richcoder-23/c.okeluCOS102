import tkinter as tk

def admit_candidate():
    name = name_entry.get()
    jamb_score = int(jamb_score_entry.get())
    credits = [int(entry.get()) for entry in credit_entry_list]
    interview_score = int(interview_score_entry.get())

    total_credits = sum(credits)
    total_score = jamb_score + total_credits + interview_score

    # Example criteria for admission
    if total_score >= 200:
        result_label.config(text=f"Congratulations {name}! You are admitted.")
    else:
        result_label.config(text=f"Sorry {name}, you are not admitted.")

# Initialize the GUI
root = tk.Tk()
root.title("Admit Candidate")

# Create input fields using a grid layout
name_label = tk.Label(root, text="Name:", font=("Arial", 14, "bold"))
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root, font=("Arial", 14), width=30)
name_entry.grid(row=0, column=1, padx=10, pady=10)

jamb_score_label = tk.Label(root, text="JAMB Score:", font=("Arial", 14, "bold"))
jamb_score_label.grid(row=1, column=0, padx=10, pady=10)
jamb_score_entry = tk.Entry(root, font=("Arial", 14), width=10)
jamb_score_entry.grid(row=1, column=1, padx=10, pady=10)

credit_label = tk.Label(root, text="Credits scores:", font=("Arial", 14, "bold"))
credit_label.grid(row=2, column=0, padx=10, pady=10)
credit_entry_list = []
for i in range(5):
    credit_entry = tk.Entry(root, font=("Arial", 14), width=10)
    credit_entry.grid(row=2, column=i+1, padx=10, pady=10)
    credit_entry_list.append(credit_entry)

interview_score_label = tk.Label(root, text="Interview Score:", font=("Arial", 14, "bold"))
interview_score_label.grid(row=3, column=0, padx=10, pady=10)
interview_score_entry = tk.Entry(root, font=("Arial", 14), width=10)
interview_score_entry.grid(row=3, column=1, padx=10, pady=10)

# Create a button to admit the candidate
admit_button = tk.Button(root, text="Admit Candidate", font=("Arial", 14), command=admit_candidate)
admit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=20)

# Create a label to display the result
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
