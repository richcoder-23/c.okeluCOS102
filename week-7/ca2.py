import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

#  calculate the total price with discounts
def calculate_total(order):
    total_price = sum(item[1] * item[2] for item in order)
    if total_price < 1000:
        return total_price
    elif total_price < 2500:
        return total_price * 0.9
    elif total_price < 5000:
        return total_price * 0.85
    else:
        return total_price * 0.75

# add an item to the order
def add_to_order():
    item_index = item_combobox.current()
    item_name = menu_items[item_index][0]
    item_price = menu_items[item_index][1]
    quantity = int(quantity_entry.get())
    order.append((item_name, item_price, quantity))
    update_order_display()

# Function to update the displayed order
def update_order_display():
    order_text = ""
    for item in order:
        order_text += f"{item[0]} x {item[2]} = {item[1] * item[2]:.2f} NGN\n"
    order_display.config(text=order_text)
    total_price = calculate_total(order)
    total_price_label.config(text=f"Total Price: {total_price:.2f} NGN")

# Main function to create  GUI
def main():
    root = tk.Tk()
    root.title("Order Calculator")

    # Load the background image
    background_image = Image.open("background.png")
    background_photo = ImageTk.PhotoImage(background_image)

    # Create a label to hold the background image
    background_label = tk.Label(root, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.image = background_photo

    # Menu items
    global menu_items
    menu_items = [
    ("Jollof Rice", 350.00),
    ("Coconut Fried Rice", 350.00),
    ("Jollof Spaghetti", 350.00),
    ("Savoury Beans", 350.00),
    ("Roasted Sweet Potatoes", 300.00),
    ("Fried Plantains", 150.00),
    ("Mixed Vegetable Salad", 150.00),
    ("Boiled Yam", 150.00),
    ("Eba", 100.00),
    ("Poundo Yam", 100.00),
    ("Semo", 100.00),
    ("Atama soup", 450.00),
    ("Egusi soup", 480.00),
    ("Sweet Chill Chicken", 1100.00),
    ("Grilled Chicken Wings", 400.00),
    ("Fried Beef", 400.00),
    ("Fried Fish", 500.00),
    ("Boiled Egg", 200.00),
    ("Saunted Sausages", 200.00),
    ("Water", 200.00),
    ("Glass Drink", 150.00),
    ("PET Drink", 300.00),
    ("PET Drink", 350.00),
    ("Glass or Canned Malt", 500.00),
    ("Fresh Yo", 600.00),
    ("Pineaple Juice", 350.00),
    ("Mango Juice", 350.00),
    ("Zobo Drink", 350.00),
]


    # Combo box for menu items
    global item_combobox
    item_combobox = ttk.Combobox(root, values=[item[0] for item in menu_items], state="readonly")
    item_combobox.place(relx=0.5, rely=0.3, anchor="center")

    # Entry for quantity
    global quantity_entry
    quantity_entry = tk.Entry(root, width=10)
    quantity_entry.place(relx=0.5, rely=0.4, anchor="center")

    # Button to add item to order
    add_button = tk.Button(root, text="Add to Order", command=add_to_order)
    add_button.place(relx=0.5, rely=0.5, anchor="center")

    # to Display order
    global order_display
    order_display = tk.Label(root, text="", justify="left")
    order_display.place(relx=0.5, rely=0.7, anchor="center")

    # Total price label
    global total_price_label
    total_price_label = tk.Label(root, text="Total Price: 0.00 NGN")
    total_price_label.place(relx=0.5, rely=0.8, anchor="center")

    root.mainloop()

if __name__ == "__main__":
    order = []  # Initialize order list
    main()
