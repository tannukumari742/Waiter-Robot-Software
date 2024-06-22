import tkinter as tk
from pymongo import MongoClient

# MongoDB connection details

uri = "mongodb+srv://tannu01:tannu01@test.14ykbbe.mongodb.net/?retryWrites=true&w=majority"
mongo_client = MongoClient(uri)
mongo_db = mongo_client['test']
mongo_collection = mongo_db['test']



orders = mongo_collection.find()  # Retrieve all orders from MongoDB
order_text = ""
for order in orders:
    if 'date' in order and 'food_name' in order:
        order_text += f"{order['date']},  {order['food_name']}\n"
    else:
        order_text += "Invalid Order Entry\n"

    # Create a new window to display orders
order_window = tk.Tk()
order_window.title("Orders Display")

    # Create a label to display orders text
orders_label = tk.Label(order_window, text=order_text, padx=20, pady=20)
orders_label.pack()

order_window.mainloop()






