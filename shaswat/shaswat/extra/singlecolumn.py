import tkinter as tk

# Function to handle button clicks
def button1_click():
    print("Button 1 clicked")

def button2_click():
    print("Button 2 clicked")

# Tkinter window
root = tk.Tk()
root.title("GUI with 5 columns")

# Calculate the screen resolution to set window size approximately 10x10 inches
screen_width = root.winfo_screenmmwidth() / 25.4  # Convert from millimeters to inches
screen_height = root.winfo_screenmmheight() / 25.4  # Convert from millimeters to inches

# Calculate the size in pixels to get approximately 10 inches by 10 inches
width_pixels = int((10 / screen_width) * root.winfo_screenwidth())
height_pixels = int((10 / screen_height) * root.winfo_screenheight())

# Set the window size
root.geometry(f"{width_pixels}x{height_pixels}")

# Set column weights to evenly spread them
for i in range(5):
    root.grid_columnconfigure(i, weight=1)

# Labels for columns
labels = []
label_texts = ["Table No.", "Order ID", "Date", "Time", "Food Item"]
for i, text in enumerate(label_texts):
    label = tk.Label(root, text=text, padx=10, pady=5)
    label.grid(row=0, column=i, sticky="nsew")

# Buttons
button1 = tk.Button(root, text="Order Received", command=button1_click, width=10, height=2)
button1.grid(row=5, column=4, sticky="se", padx=(0,10), pady=(0,5))  # Set row to 5 for button1

button2 = tk.Button(root, text="Order Delivered", command=button2_click, width=10, height=2)
button2.grid(row=6, column=4, sticky="se", padx=(0,10), pady=(0,10))  # Set row to 6 for button2

root.mainloop()
