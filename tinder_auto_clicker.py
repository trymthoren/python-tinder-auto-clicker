import tkinter as tk
import pyautogui
import random
import time
import threading

class AutoKeyPresser:
    def __init__(self, root):
        self.root = root
        self.running = False

        tk.Label(root, text="Number of Key Presses:").pack()
        self.num_presses_entry = tk.Entry(root)
        self.num_presses_entry.pack()

        tk.Label(root, text="Minimum Delay (seconds):").pack()
        self.min_delay_entry = tk.Entry(root)
        self.min_delay_entry.pack()

        tk.Label(root, text="Maximum Delay (seconds):").pack()
        self.max_delay_entry = tk.Entry(root)
        self.max_delay_entry.pack()

        self.start_button = tk.Button(root, text="Start Pressing", command=self.start_key_presses)
        self.start_button.pack()

        self.stop_button = tk.Button(root, text="Stop Pressing", command=self.stop_key_presses, state=tk.DISABLED)
        self.stop_button.pack()

    def perform_key_presses(self):
        num_presses = int(self.num_presses_entry.get())
        min_delay = float(self.min_delay_entry.get())
        max_delay = float(self.max_delay_entry.get())

        for _ in range(num_presses):
            if not self.running:
                break
            delay = random.uniform(min_delay, max_delay)
            time.sleep(delay)
            pyautogui.press('right')  # Simulate right arrow key press

        self.stop_key_presses()

    def start_key_presses(self):
        self.running = True
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
root.mainloop()

