import tkinter as tk
from pymongo import MongoClient

uri = "mongodb+srv://tannu01:tannu01@test.14ykbbe.mongodb.net/?retryWrites=true&w=majority"
mongo_client = MongoClient(uri)
mongo_db = mongo_client['test']
mongo_collection = mongo_db['test']

def update_listbox():
    orders = mongo_collection.find()  # Retrieve all orders from MongoDB
    pending_orders_listbox.delete(0, tk.END)  # Clear previous entries
    for order in orders:
        if 'date' in order and 'food_name' in order:
            order_text = f"{order['date']},  {order['food_name']}"
            pending_orders_listbox.insert(tk.END, order_text)
        else:
            pending_orders_listbox.insert(tk.END, "Invalid Order Entry")

    # Schedule the update_listbox function to run again after a delay (e.g., 5 seconds)
    root.after(5000, update_listbox)

# Tkinter window
root = tk.Tk()
root.title("Order Management System")

# Frames for pending and delivered orders
pending_frame = tk.Frame(root)
pending_frame.pack(side=tk.LEFT, padx=10, pady=10)

delivered_frame = tk.Frame(root)
delivered_frame.pack(side=tk.RIGHT, padx=10, pady=10)

# Pending Orders Section
pending_label = tk.Label(pending_frame, text="Pending Orders")
pending_label.pack()

# Listbox to display pending orders
pending_orders_listbox = tk.Listbox(pending_frame, width=50, height=20)
pending_orders_listbox.pack()

# Call the update_listbox function to initially populate the listbox and start the periodic updates
update_listbox()

# Button to deliver selected order
deliver_button = tk.Button(pending_frame, text="Deliver Selected Order")
deliver_button.pack(pady=10)

# Delivered Orders Section
delivered_label = tk.Label(delivered_frame, text="Delivered Orders")
delivered_label.pack()

# Listbox to display delivered orders
delivered_orders_listbox = tk.Listbox(delivered_frame, width=50, height=20)
delivered_orders_listbox.pack()

root.mainloop()
