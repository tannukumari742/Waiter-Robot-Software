import tkinter as tk
from PIL import ImageTk
import subprocess
import speech_recognition as sr
import threading

bg_colour = "#8B4513"
delmenu_process = None  # Variable to hold the subprocess

def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def start_second_file():
    # Call the second file using subprocess
    subprocess.run(["python", r"C:\Users\tannu\OneDrive\Desktop\restro\2wgt.py", "--root", str(root)])
    # Schedule the destruction of the current Tkinter window after a short delay
    root.after(1, root.destroy)

def green():
    global delmenu_process
    delmenu_process = subprocess.Popen(["python", r"C:\Users\tannu\OneDrive\Desktop\moving_bot\webcamtest.py", "--root", str(root)])

def back():
    global delmenu_process
    if delmenu_process is not None:
        delmenu_process.terminate()
        delmenu_process = None

def load_frame1():
    clear_widgets(frame2)
    frame1.tkraise()
    frame1.pack_propagate(False)
    logo_img = ImageTk.PhotoImage(file=r"C:\Users\tannu\OneDrive\Desktop\restro\assets\logo.png")
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_colour)
    logo_widget.image = logo_img
    logo_widget.pack(anchor='w', padx=20)
    tk.Label(frame1, text="Welcome to our restaurant", bg=bg_colour, fg="white", font=("Shanti", 14)).pack(anchor='w', padx=140)
    
    button_frame = tk.Frame(frame1, bg=bg_colour)
    button_frame.pack(anchor='w', padx=20, pady=20)
    
    # Start Button
    tk.Button(button_frame, text="Start", font=("Ubuntu", 30), width=20, bg="#28393a", fg="white", cursor="hand2", 
              activebackground="#badee2", activeforeground="black", command=start_second_file).pack(side='left', padx=10)
    
    # NAVIGATION Buttons

    # Button in the top right corner
    tk.Button(frame1, text="Green", font=("Ubuntu", 25), width=15, bg="green", fg="black", cursor="hand2", command=green,
              activebackground="#badee2", activeforeground="black").place(relx=1.0, rely=0.0, anchor='ne', x=-600, y=80)

    tk.Button(frame1, text="Stop", font=("Ubuntu", 25), width=15, bg="green", fg="black", cursor="hand2", command=back,
              activebackground="#badee2", activeforeground="black").place(relx=1.0, rely=0.0, anchor='ne', x=-200, y=80)
    
    tk.Button(frame1, text="Yellow", font=("Ubuntu", 25), width=15, bg="yellow", fg="black", cursor="hand2", 
              activebackground="#badee2", activeforeground="black").place(relx=1.0, rely=0.0, anchor='ne', x=-600, y=240)
    
    tk.Button(frame1, text="Stop", font=("Ubuntu", 25), width=15, bg="yellow", fg="black", cursor="hand2", 
              activebackground="#badee2", activeforeground="black").place(relx=1.0, rely=0.0, anchor='ne', x=-200, y=240)
    
    tk.Button(frame1, text="Red", font=("Ubuntu", 25), width=15, bg="red", fg="black", cursor="hand2", 
              activebackground="#badee2", activeforeground="black").place(relx=1.0, rely=0.0, anchor='ne', x=-600, y=400)
    
    tk.Button(frame1, text="Stop", font=("Ubuntu", 25), width=15, bg="red", fg="black", cursor="hand2", 
              activebackground="#badee2", activeforeground="black").place(relx=1.0, rely=0.0, anchor='ne', x=-200, y=400)

def listen_for_commands():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    
    while True:
        with microphone as source:
            print("Listening for commands...")
            audio = recognizer.listen(source)
        
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"Recognized command: {command}")
            if "green" in command:
                green()
            elif "stop" in command:
                back()
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError:
            print("Could not request results; check your network connection")

root = tk.Tk()
root.title("Dataintelliage")

# Set fullscreen   
root.attributes('-fullscreen', True)

frame1 = tk.Frame(root, bg=bg_colour)
frame2 = tk.Frame(root, bg=bg_colour)

for frame in (frame1, frame2):
    frame.place(relx=0, rely=0, relwidth=1, relheight=1)

load_frame1()

# Start the voice command listener in a separate thread
listener_thread = threading.Thread(target=listen_for_commands)
listener_thread.daemon = True
listener_thread.start()

root.mainloop()
