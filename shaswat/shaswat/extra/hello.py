import tkinter as tk
from PIL import ImageTk
import subprocess
import firebase_admin
from firebase_admin import credentials, db

bg_colour = "#3d6466"

# Initialize Firebase with your credentials
cred = credentials.Certificate(r"C:\Users\HP\Desktop\smart\robot-f8bed-firebase-adminsdk-b95ir-c65c5beaab.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://robot-f8bed.firebaseio.com/'
})

def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def store_data_to_firebase(data):
    ref = db.reference('/food_items')
    ref.push(data)

def start_second_file():
    # Call the function to store data in Firebase
    data = {'name': 'Pizza', 'price': 10.99, 'description': 'Delicious pizza with cheese and toppings.'}
    store_data_to_firebase(data)
    
    # Call the second file using subprocess
    subprocess.run(["python", "module\waitermongocon.py"])

def load_frame1():
    clear_widgets(frame2)
    frame1.tkraise()
    frame1.pack_propagate(False)
    logo_img = ImageTk.PhotoImage(file="assets\RRecipe_logo.png")
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_colour)
    logo_widget.image = logo_img
    logo_widget.pack()
    tk.Label(frame1, text="welcome to our restaurant", bg=bg_colour, fg="white", font=("Shanti", 14)).pack()
    tk.Button(frame1, text="Start", font=("Ubuntu", 20), bg="#28393a", fg="white", cursor="hand2", 
              activebackground="#badee2", activeforeground="black", command=start_second_file).pack(pady=20)

root = tk.Tk()
root.title("Recipe Picker")
root.eval("tk::PlaceWindow . center")

frame1 = tk.Frame(root, width=500, height=600, bg=bg_colour)
frame2 = tk.Frame(root, bg=bg_colour)

for frame in (frame1, frame2):
    frame.grid(row=0, column=0, sticky="nesw")

load_frame1()
root.mainloop()
