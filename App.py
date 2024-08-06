import tkinter as tk
import time

running = False
start_time = None

def update_time():
    """Update the stopwatch display every second."""
    if running:
        elapsed = time.time() - start_time
        minutes, seconds = divmod(elapsed, 60)
        label_time.config(text=f"{int(minutes):02}:{int(seconds):02}")
        root.after(1000, update_time)

def start():
    """Start the stopwatch."""
    global running, start_time
    if not running:
        running = True
        start_time = time.time() - sum_lap_times()
        update_time()

def stop():
    """Stop the stopwatch."""
    global running
    running = False

def reset():
    """Reset the stopwatch and lap times."""
    global start_time
    start_time = None
    label_time.config(text="00:00")
    listbox_laps.delete(0, tk.END)
    stop()

def lap():
    """Record a lap time."""
    if running:
        elapsed = time.time() - start_time
        minutes, seconds = divmod(elapsed, 60)
        listbox_laps.insert(tk.END, f"{int(minutes):02}:{int(seconds):02}")

def sum_lap_times():
    """Calculate the total lap time."""
    total = 0
    for lap_time in listbox_laps.get(0, tk.END):
        minutes, seconds = map(int, lap_time.split(":"))
        total += minutes * 60 + seconds
    return total

# Create the main window
root = tk.Tk()
root.title("Stopwatch with Lap Times")

# Create and place widgets
label_time = tk.Label(root, text="00:00", font=("Arial", 48))
label_time.pack()

frame_buttons = tk.Frame(root)
frame_buttons.pack()

button_start = tk.Button(frame_buttons, text="Start", command=start)
button_start.pack(side=tk.LEFT)

button_stop = tk.Button(frame_buttons, text="Stop", command=stop)
button_stop.pack(side=tk.LEFT)

button_reset = tk.Button(frame_buttons, text="Reset", command=reset)
button_reset.pack(side=tk.LEFT)

button_lap = tk.Button(frame_buttons, text="Lap", command=lap)
button_lap.pack(side=tk.LEFT)

listbox_laps = tk.Listbox(root, width=20, height=10)
listbox_laps.pack()

# Start the main loop
root.mainloop()
