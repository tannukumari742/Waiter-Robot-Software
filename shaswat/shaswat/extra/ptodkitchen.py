import tkinter as tk
from pymongo import MongoClient

uri = "mongodb+srv://tannu01:tannu01@test.14ykbbe.mongodb.net/?retryWrites=true&w=majority"
mongo_client = MongoClient(uri)
mongo_db = mongo_client['test']
mongo_collection = mongo_db['test']

def update_listbox():
    orders = mongo_collection.find()  # Retrieve all orders from MongoDB
    for widget in pending_orders_frame.winfo_children():
        widget.destroy()  # Clear previous entries
        
    for order in orders:
        if 'date' in order and 'food_name' in order:
            order_frame = tk.Frame(pending_orders_frame)
            order_frame.pack(fill=tk.X)
            
            order_text = f"{order['date']},  {order['food_name']}"
            order_label = tk.Label(order_frame, text=order_text, width=40)
            order_label.pack(side=tk.LEFT)
            
            # Create a "Done" button for each order
            done_button = tk.Button(order_frame, text="Done", command=lambda order_id=order['_id']: mark_order_as_delivered(order_id))
            done_button.pack(side=tk.LEFT)
            
    # Update the scroll region of the canvas
    pending_orders_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # Schedule the update_listbox function to run again after a delay (e.g., 5 seconds)
    root.after(5000, update_listbox)



def mark_order_as_delivered(order_id):
    # Update order status to delivered
    mongo_collection.update_one({"_id": order_id}, {"$set": {"status": "delivered"}})
    
    # Move the order to the delivered listbox
    order = mongo_collection.find_one({"_id": order_id})
    if order:
        order_text = f"{order['date']},  {order['food_name']}"
        delivered_orders_listbox.insert(tk.END, order_text)

    # Remove the specific order frame from the pending orders section
    for frame in pending_orders_frame.winfo_children():
        if frame.winfo_name() == str(order_id):  # Match the order ID with the name of the frame
            frame.destroy()
            break  # Exit loop after deleting the frame
            
    # Change the color of the "Done" button to red
    for item in delivered_orders_listbox.get(0, tk.END):
        if order_text in item:
            delivered_orders_listbox.itemconfig(delivered_orders_listbox.get(0, tk.END).index(item), {'bg': 'red'})


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

# Frame to contain pending orders
pending_orders_frame = tk.Frame(pending_frame)
pending_orders_frame.pack()

# Create a Canvas widget
canvas = tk.Canvas(pending_frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Add a scrollbar to the Canvas
scrollbar = tk.Scrollbar(pending_frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame inside the Canvas for the orders
pending_orders_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=pending_orders_frame, anchor=tk.NW)

# Call the update_listbox function to initially populate the listbox and start the periodic updates
update_listbox()

# Delivered Orders Section
delivered_label = tk.Label(delivered_frame, text="Delivered Orders")
delivered_label.pack()

# Listbox to display delivered orders
delivered_orders_listbox = tk.Listbox(delivered_frame, width=50, height=20)
delivered_orders_listbox.pack()

root.mainloop()
