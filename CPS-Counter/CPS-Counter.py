import time
import keyboard
import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk

class CPSCounter:
    def __init__(self, duration):
        self.duration = duration
        self.clicks = 0
        self.cps = 0
        self.high_score = 0
        self.is_running = False
        self.start_time = 0
        self.end_time = 0
        self.root = tk.Tk()
        self.root.title("CPS Counter")
        self.root.geometry("300x200")
        self.root.config(bg="#1E1E1E")
        self.font = font.Font(family="Helvetica", size=12, weight="bold")
        self.label = tk.Label(self.root, text="Press Start to begin", font=self.font, bg="#1E1E1E", fg="#FFFFFF")
        self.label.pack(pady=20)
        self.start_button_image = Image.open("CPS-counter/start_button.png")
        self.start_button_image = self.start_button_image.resize((100, 50), Image.BICUBIC)
        self.start_button_photo = ImageTk.PhotoImage(self.start_button_image)
        self.start_button = tk.Button(self.root, image=self.start_button_photo, bg="#1E1E1E", bd=0, command=self.start)
        self.start_button.pack(pady=10)
        self.high_score_label = tk.Label(self.root, text=f"High Score: {self.high_score:.2f}", font=self.font, bg="#1E1E1E", fg="#FFFFFF")
        self.high_score_label.pack(pady=10)
        self.root.mainloop()

    def start(self):
        self.is_running = True
        self.start_time = time.time()
        self.end_time = self.start_time + self.duration
        self.clicks = 0
        self.update_label()
        self.start_button.config(state="disabled")
        self.root.after(100, self.check_key_press)

    def check_key_press(self):
        if self.is_running and time.time() < self.end_time:
            if keyboard.is_pressed('space') and not self.spacebar_pressed:
                self.spacebar_pressed = True
                self.clicks += 1
            elif not keyboard.is_pressed('space'):
                self.spacebar_pressed = False
            self.root.after(10, self.check_key_press)
        else:
            self.is_running = False
            self.cps = self.clicks / self.duration
            self.update_label()
            self.start_button.config(state="normal")

    def update_label(self):
        if self.is_running:
            time_left = int(self.end_time - time.time())
            milliseconds_left = int((self.end_time - time.time()) * 100) % 100
            self.label.config(text=f"Time Left: {time_left:02d}.{milliseconds_left:02d} s\nClicks: {self.clicks}\nCPS: {self.cps:.2f}")
            self.root.after(100, self.update_label)
        else:
            self.label.config(text=f"You clicked {self.clicks} times in {self.duration} seconds.\nYour clicks per second (CPS) is {self.cps:.2f}.")

duration = 10
cps_counter = CPSCounter(duration)  