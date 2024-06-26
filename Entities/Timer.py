import tkinter as tk
class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer")

        self.time_left_var = tk.StringVar()
        self.time_left_var.set("00:00:00")

        self.label = tk.Label(root, textvariable=self.time_left_var, font=("Helvetica", 48))
        self.label.pack(pady=20)

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
        self.time_left_var.set("00:00:00")
        self.running = False

    def update_timer(self):
        if self.running:
            # Calcola ore, minuti e secondi
            mins, secs = divmod(self.elapsed_time, 60)
            hours, mins = divmod(mins, 60)
            self.time_left_var.set(f"{hours:02d}:{mins:02d}:{secs:02d}")
            self.elapsed_time += 1
            # Chiama di nuovo update_timer dopo 1 secondo
            self.root.after(1000, self.update_timer)