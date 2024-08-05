import tkinter as tk

class Stopwatch:
    """A simple stopwatch application."""

    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")

        self.time_elapsed = 0
        self.running = False

        self.label = tk.Label(root, text="00:00:00", font=("Arial", 24))
        self.label.pack(pady=20)

        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=20)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack(side=tk.LEFT, padx=20)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=20)

    def start(self):
        """Start the stopwatch."""
        if not self.running:
            self.running = True
            self.update_time()

    def stop(self):
        """Stop the stopwatch."""
        self.running = False

    def reset(self):
        """Reset the stopwatch."""
        self.time_elapsed = 0
        self.label.config(text="00:00:00")

    def update_time(self):
        """Update the time display."""
        if self.running:
            self.time_elapsed += 1
            minutes, seconds = divmod(self.time_elapsed, 60)
            hours, minutes = divmod(minutes, 60)
            self.label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
            self.root.after(1000, self.update_time)

def main():
    root = tk.Tk()
    stopwatch = Stopwatch(root)
    root.mainloop()

if __name__ == "__main__":
    main()
