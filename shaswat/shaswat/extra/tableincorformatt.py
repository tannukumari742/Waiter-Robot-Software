import tkinter as tk
from tkinter import ttk
from pymongo import MongoClient

def update_treeview():
    # Clear existing data
    pending_tree.delete(*pending_tree.get_children())
    delivered_tree.delete(*delivered_tree.get_children())
    
    # Retrieve all orders from MongoDB
    orders = mongo_collection.find()  
    for order in orders:
        if 'date' in order and 'food_item' in order and 'table_number' in order:
            # Insert a new row into the corresponding treeview
            table_number = order.get('table_number', '')  # Get 'table_number' or set to '' if not present
            date = order.get('date', '')  # Get 'date' or set to '' if not present
            food_item = order.get('food_item', '')  # Get 'food_item' or set to '' if not present
            status = order.get('status', '')  # Get 'status' or set to '' if not present
            
            if status == 'delivered':
                delivered_tree.insert('', tk.END, values=(table_number, date, food_item))
            else:
                pending_tree.insert('', tk.END, values=(table_number, date, food_item))

    # Schedule the update_treeview function to run again after a delay (e.g., 5 seconds)
    root.after(5000, update_treeview)

# Tkinter window
root = tk.Tk()
root.title("Order Management System")

# Frame for delivered orders
delivered_frame = tk.Frame(root)
delivered_frame.pack(side=tk.BOTTOM, padx=20, pady=20)

# Create a Treeview widget for delivered orders
delivered_tree = ttk.Treeview(delivered_frame, columns=('Table Number', 'Date', 'Food Item'), show='headings')
delivered_tree.heading('Table Number', text='Table Number')
delivered_tree.heading('Date', text='Date')
delivered_tree.heading('Food Item', text='Food Item')
delivered_tree.pack(fill='both', expand=True)

# Frame for pending orders
pending_frame = tk.Frame(root)
pending_frame.pack(side=tk.TOP, padx=20, pady=20)

# Create a Treeview widget for pending orders
pending_tree = ttk.Treeview(pending_frame, columns=('Table Number', 'Date', 'Food Item'), show='headings')
pending_tree.heading('Table Number', text='Table Number')
pending_tree.heading('Date', text='Date')
pending_tree.heading('Food Item', text='Food Item')
pending_tree.pack(fill='both', expand=True)

# MongoDB connection
uri = "mongodb+srv://tannu01:tannu01@test.14ykbbe.mongodb.net/?retryWrites=true&w=majority"   
mongo_client = MongoClient(uri)
mongo_db = mongo_client['test']
mongo_collection = mongo_db['test']

# Call the update_treeview function to initially populate the treeviews and start the periodic updates
update_treeview()

root.mainloop()
