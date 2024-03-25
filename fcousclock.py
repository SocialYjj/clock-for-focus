import tkinter as tk
from datetime import datetime
import time

class SpecialClock:
    def __init__(self, master):
        self.master = master
        self.master.title("Special Clock")

        self.time_label = tk.Label(master, font=('Helvetica', 48))
        self.time_label.pack(pady=20)

        self.update_time()

    def update_time(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        self.time_label.config(text=current_time)
        self.master.after(1000, self.update_time)

def main():
    root = tk.Tk()
    clock = SpecialClock(root)
    root.mainloop()

if __name__ == "__main__":
    main()
