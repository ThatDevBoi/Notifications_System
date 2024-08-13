import time
import requests
import tkinter as tk
from tkinter import messagebox

SERVER_URL = 'http://127.0.0.1:5000/get-notification'  # Update to your server URL

def get_latest_notification():
    try:
        response = requests.get(SERVER_URL)
        if response.status_code == 200:
            data = response.json()
            return data.get('message')
    except Exception as e:
        print(f"Error fetching notification: {e}")
    return None

def show_notification(message):
    # Create a simple pop-up window using tkinter
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    messagebox.showinfo("IT Notification", message)
    root.destroy()

def main():
    last_message = None
    while True:
        message = get_latest_notification()
        if message and message != last_message:
            show_notification(message)
            last_message = message
        time.sleep(30)  # Check every 30 seconds

if __name__ == '__main__':
    main()
