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
        self.no_matches_detected = False  # New flag for 'no more potential matches'

        # UI Styling
        bg_color = "#2D2D2D"  # Dark gray
        text_color = "#FFA500"  # Orange

        root.configure(bg=bg_color)

        # Labels & Inputs
        tk.Label(root, text="Number of Key Presses:", bg=bg_color, fg=text_color).pack()
        self.num_presses_entry = tk.Entry(root)
        self.num_presses_entry.pack()

        tk.Label(root, text="Minimum Delay (milliseconds):", bg=bg_color, fg=text_color).pack()
        self.min_delay_entry = tk.Entry(root)
        self.min_delay_entry.pack()

        tk.Label(root, text="Maximum Delay (milliseconds):", bg=bg_color, fg=text_color).pack()
        self.max_delay_entry = tk.Entry(root)
        self.max_delay_entry.pack()

        # Buttons
        self.start_button = tk.Button(root, text="Start Pressing", command=self.start_key_presses, bg="#333333", fg=text_color)
        self.start_button.pack()

        self.stop_button = tk.Button(root, text="Stop Pressing", command=self.stop_key_presses, state=tk.DISABLED, bg="#333333", fg=text_color)
        self.stop_button.pack()

    def show_popup(self, message):
        """ Displays a popup message. """
        popup = tk.Toplevel(self.root)
        popup.title("Notification")
        popup.geometry("300x100")
        tk.Label(popup, text=message, padx=20, pady=10).pack()
        tk.Button(popup, text="OK", command=popup.destroy).pack(pady=5)

    def perform_key_presses(self):
        num_presses = int(self.num_presses_entry.get())
        min_delay = float(self.min_delay_entry.get()) / 1000
        max_delay = float(self.max_delay_entry.get()) / 1000

        tinder_popup = 'super_like_popup.png'
        no_matches_img = 'go_global.png'  # New image to detect "No more matches"

        for _ in range(num_presses):
            if not self.running:
                break
            delay = random.uniform(min_delay, max_delay)
            time.sleep(delay)

            # Check for "No More Matches"
            if not self.no_matches_detected:
                try:
                    if pyautogui.locateOnScreen(no_matches_img, confidence=0.8) is not None:
                        self.no_matches_detected = True
                        print("No more potential matches. Auto liking stopped.")
                        self.show_popup("No more potential matches.")
                        self.stop_key_presses()
                        return
                except pyautogui.ImageNotFoundException:
                    pass

            # Check for the Tinder Super Like popup
            if not self.popup_detected:
                try:
                    if pyautogui.locateOnScreen(tinder_popup, confidence=0.6) is not None:
                        pyautogui.press('esc')
                        self.popup_detected = True
                        print("Popup detected and closed.")
                        time.sleep(1)
                except pyautogui.ImageNotFoundException:
                    pass  

            # Simulate right arrow key press
            pyautogui.press('right')

        self.stop_key_presses()

    def start_key_presses(self):
        self.running = True
        self.popup_detected = False  # Reset flags
        self.no_matches_detected = False  
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
root.geometry("400x200")
root.mainloop()
