import time
import threading

def stopwatch():
    """A simple command-line stopwatch."""
    def timer():
        """Run the stopwatch timer."""
        start_time = time.time()
        while running:
            elapsed_time = time.time() - start_time
            print(f"\rElapsed time: {elapsed_time:.2f} seconds", end="")
            time.sleep(0.1)

    global running
    running = True

    # Start the timer thread
    timer_thread = threading.Thread(target=timer)
    timer_thread.start()

    # Wait for user input to stop the stopwatch
    input("\nPress Enter to stop the stopwatch...")
    running = False
    timer_thread.join()
    print("\nStopwatch stopped.")

if __name__ == "__main__":
    stopwatch()
