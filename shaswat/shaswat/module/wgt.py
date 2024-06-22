import tkinter as tk
import speech_recognition as sr
import datetime
import json
from difflib import get_close_matches
import cv2
import threading
import subprocess
from random import choice
from PIL import Image, ImageTk
import os
from gtts import gTTS
import pygame  # to play audio

bg_colour = "#8B4513"

# Initialize pygame mixer
pygame.mixer.init()


# Function to display the menu
def display_menu():
    root.destroy()  # Close the original GUI window
    subprocess.Popen(["python", "/home/ras2024/Downloads/shaswat/shaswat/menu+-final.py"])  # Open menu.py using subprocess


class DateTime:
    @staticmethod
    def currentTime():
        time = datetime.datetime.now()
        x = " A.M."
        if time.hour > 12:
            x = " P.M."
        time = str(time)
        time = time[11:16] + x
        return time

    @staticmethod
    def currentDate():
        now = datetime.datetime.now()
        day = now.strftime('%A')
        date = now.strftime('%d')
        month = now.strftime('%B')
        year = str(now.year)
        result = f'{day}, {date} {month}, {year}'
        return result


def wishMe():
    now = datetime.datetime.now()
    hr = now.hour
    if hr < 12:
        wish = "Good Morning, welcome to Shaswat Restaurant. I am here to take your order."
    elif 12 <= hr < 16:
        wish = "Good Afternoon, welcome to Shaswat Restaurant. I am here to take your order."
    else:
        wish = "Good Evening, welcome to Shaswat Restaurant. I am here to take your order."
    return wish


def containsKeyword(text, keywords):
    for word in keywords:
        if word in text:
            return True
    return False


def chat(text):
    dt = DateTime()
    result = ""

    if containsKeyword(text, ['good']):
        result = wishMe()
    elif containsKeyword(text, ['time']):
        result = "Current Time is: " + dt.currentTime()
    elif containsKeyword(text, ['date', 'today', 'day', 'month']):
        result = dt.currentDate()
    elif containsKeyword(text, ['order', 'food']):
        # Extract the food item from the user's input
        food_item = text.split("order", 1)[-1].strip()

        return f"Order received for {food_item}. Thank you!"
    else:
        result = reply(text)

    return result


def reply(query):
    if query in data:
        response = data[query]
    else:
        matches = get_close_matches(query, data.keys(), n=2, cutoff=0.6)
        if not matches:
            return "I'm sorry, I don't understand that."
        response = data[matches[0]]

    return choice(response)


food_items = ["pizza", "burger", "pasta", "maggie", "rolls", "naan", "drinks"]


def refresh_gui():
    pass  # You can leave this blank for now, or implement it later if needed


def on_send():
    user_input = user_input_entry.get()
    chatbot_response = chat(user_input)
    speak(chatbot_response)
    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, f"You: {user_input}\nBot: {chatbot_response}\n\n")
    chat_display.config(state=tk.DISABLED)
    user_input_entry.delete(0, tk.END)


# Function to speak out the response
def speak(text, lang='en'):
    if lang == 'en':
        tts_lang = 'en'
    elif lang == 'hi':
        tts_lang = 'hi'
    else:
        print("Unsupported language:", lang)
        return

    tts = gTTS(text=text, lang=tts_lang)
    tts.save("output.mp3")
    os.system("mpg321 output.mp3")
    os.remove("output.mp3")





def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            user_input = recognizer.recognize_google(audio, language='hi-IN,en-US')
            user_input_entry.delete(0, tk.END)
            user_input_entry.insert(0, user_input)
            on_send()
        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio")
            speak("Sorry, I couldn't understand what you said.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            speak("Sorry, there was an error with the Speech Recognition service. Please try again later.")
        except Exception as e:
            print(f"Error during voice input processing: {e}")
            speak("Sorry, there was an unexpected error. Please try again.")


def face_detection():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Assuming face detection triggers conversation
            stop_face_detection(cap)
            start_conversation()

        cv2.imshow('Face Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def stop_face_detection(cap):
    cap.release()


def start_conversation():
    welcome_message = wishMe()
    speak(welcome_message)
    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, f"Bot: {welcome_message}\n\n")
    chat_display.config(state=tk.DISABLED)


def run_face_detection():
    face_detection_thread = threading.Thread(target=face_detection)
    face_detection_thread.start()


# Load JSON data
with open("/home/ras2024/Downloads/shaswat/shaswat/assets/normal_chat.json",
          encoding='utf-8') as json_file:
    data = json.load(json_file)

# Run face detection in a separate thread
run_face_detection()

# Create the GUI
root = tk.Tk()
root.configure(bg=bg_colour)
root.title("dataintelliage waiter")

# Function to display image
def display_image():
    # Load the image
    image = Image.open(
        "/home/ras2024/Downloads/shaswat/shaswat/botimg.jpg")  # Replace "path/to/your/image.jpg" with the actual path to your image file

    # Resize the image to fit the GUI
    image.thumbnail((200, 200))

    # Convert the image to Tkinter-compatible format
    photo = ImageTk.PhotoImage(image)

    # Create a label to display the image
    image_label = tk.Label(root, image=photo, bg=bg_colour)
    image_label.image = photo  # Keep a reference to the image to prevent garbage collection

    # Place the label on the GUI
    image_label.pack(pady=5, )


# Call the function to display the image
display_image()

# User input entry
user_input_entry = tk.Entry(root, width=100, font=('Arial', 24))
user_input_entry.pack(pady=10)

# Buttons
send_button = tk.Button(root, text="SEND", command=listen, font=('Arial', 20), bg="#28393a", fg="white",
                        cursor="hand2", activebackground="#badee2", activeforeground="black")
send_button.pack(pady=15)

# Button to display the menu
menu_button = tk.Button(root, text="MENU", command=display_menu, font=('Arial', 20), bg="#28393a", fg="white",
                        cursor="hand2", activebackground="#badee2", activeforeground="black")
menu_button.pack(pady=15)

voice_button = tk.Button(root, text="VOICE", command=listen, font=('Arial', 20), bg="#28393a", fg="white",
                         cursor="hand2", activebackground="#badee2", activeforeground="black")
voice_button.pack(pady=15)

# Chat display
chat_display = tk.Text(root, height=20, width=50, font=('Arial', 24), wrap=tk.WORD)
chat_display.pack(pady=20)
chat_display.config(state=tk.DISABLED)

# Close event listener for the main GUI window
def on_closing():
    root.destroy()  # Close the main GUI window
    # Call the function to start the third file (order display module)


root.protocol("WM_DELETE_WINDOW", on_closing)  # Set the listener for window close event

#root.attributes('-fullscreen', True)
# Run the GUI
root.mainloop()
