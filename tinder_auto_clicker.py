import tkinter as tk
import pyautogui
import random
import time
import threading

class AutoKeyPresser:
    def __init__(self, root):
        self.root = root
        self.running = False
        self.popup_detected = False

        # Set the background color and text color
        bg_color = "#2D2D2D"  # Dark gray
        text_color = "#FFA500"  # Orange

        root.configure(bg=bg_color)  # Set the background color of the root window

        # Configure labels with dark mode colors
        tk.Label(root, text="Number of Key Presses:", bg=bg_color, fg=text_color).pack()
        self.num_presses_entry = tk.Entry(root)
        self.num_presses_entry.pack()

        tk.Label(root, text="Minimum Delay (milliseconds):", bg=bg_color, fg=text_color).pack()
        self.min_delay_entry = tk.Entry(root)
        self.min_delay_entry.pack()

        tk.Label(root, text="Maximum Delay (milliseconds):", bg=bg_color, fg=text_color).pack()
        self.max_delay_entry = tk.Entry(root)
        self.max_delay_entry.pack()

        # Configure buttons with dark mode colors
        self.start_button = tk.Button(root, text="Start Pressing", command=self.start_key_presses, bg="#333333", fg=text_color)
        self.start_button.pack()

        self.stop_button = tk.Button(root, text="Stop Pressing", command=self.stop_key_presses, state=tk.DISABLED, bg="#333333", fg=text_color)
        self.stop_button.pack()


    def perform_key_presses(self):
        num_presses = int(self.num_presses_entry.get())
        min_delay = float(self.min_delay_entry.get()) / 1000  # Convert milliseconds to seconds
        max_delay = float(self.max_delay_entry.get()) / 1000  # Convert milliseconds to seconds
        tinder_popup = 'super_like_popup.png'  # Screenshot of superlike ad popup

        for _ in range(num_presses):
            if not self.running:
                break
            delay = random.uniform(min_delay, max_delay)
            time.sleep(delay)

            # Check for the Tinder popup only if it has not been detected yet
            if not self.popup_detected:
                try:
                    if pyautogui.locateOnScreen(tinder_popup, confidence=0.6) is not None:
                        pyautogui.press('esc')
                        self.popup_detected = True  # Set the flag to True after pressing 'esc'
                        print("Popup detected and closed.")
                        time.sleep(1)  # Sleep for 1 second after closing the popup
                except pyautogui.ImageNotFoundException:
                    pass  # If the popup is not found, do nothing

            # Simulate right arrow key press
            pyautogui.press('right')

        self.stop_key_presses()

    def start_key_presses(self):
        self.running = True
        self.popup_detected = False  # Reset the flag each time we start since the popup seems to only appear once
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        threading.Thread(target=self.perform_key_presses).start()

    def stop_key_presses(self):
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Auto Key Presser")


app = AutoKeyPresser(root)

# Optionally, set the geometry of the root window for a more modern look
root.geometry("400x200")  # Can be adjusted as needed

root.mainloop()
