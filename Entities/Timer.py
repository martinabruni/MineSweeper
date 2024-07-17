import tkinter as tk


class TimerApp:
    def __init__(self, frame: tk.Frame):
        self.frame = frame

        self.time_passed = tk.StringVar()
        self.time_passed.set("00:00:00")

        self.label = tk.Label(self.frame, textvariable=self.time_passed, font=("Terminal", 30), bg="black", fg="red")
        self.label.pack(side="top", pady=20)

        self.elapsed_time = 0
        self.running = False

    def start_timer(self):
        if self.running == False:
            self.running = True
            self.update_timer()

    def stop_timer(self):
        if self.running:
            # Arresta il timer
            self.running = False

    def reset_timer(self):
        self.elapsed_time = 0
        self.time_passed.set("00:00:00")
        self.running = False

    def update_timer(self):
        if self.running:
            # Calcola ore, minuti e secondi
            mins, secs = divmod(self.elapsed_time, 60)
            hours, mins = divmod(mins, 60)
            self.time_passed.set(f"{hours:02d}:{mins:02d}:{secs:02d}")
            self.elapsed_time += 1
            # Chiama di nuovo update_timer dopo 1 secondo
            self.frame.after(1000, self.update_timer)