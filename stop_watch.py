import time

class StopWatch:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0
        self.running = False
    
    def start(self):
        if not self.running:
            self.start_time = time.time()
            self.running = True
            print("Stopwatch started!")
        else:
            print("Stopwatch is already running.")
            
    def stop(self):
        if self.running:
            self.elapsed_time += time.time() - self.start_time
            self.running = False
            print("Stopwatch stopped!")
        else:
            print("Stopwatch is not running!")
            
    def reset(self):
        self.start_time = None
        self.elapsed_time = 0
        self.running  = False
        print("Stopwatch reset.")
    
    def display(self):
        if self.running:
            current_elapsed = self.elapsed_time + (time.time() - self.start_time)
        else:
            current_elapsed = self.elapsed_time
        
        hours = int(current_elapsed // 3600)
        minutes = int((current_elapsed % 3600)//60)
        seconds = int(current_elapsed % 60)
        milliseconds = int((current_elapsed % 1) * 1000)
        
        print(f"{hours:02d}:{minutes:02d}:{seconds:02d}:{milliseconds:03d}")
        
def main():
    stopWatch = StopWatch()
    
    while True:
        print("\n--- Stopwatch Menu ---")
        print("1. Start")
        print("2. Stop")
        print("3. Display")
        print("4. Reset")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            stopWatch.start()
        elif choice == "2":
            stopWatch.stop()
        elif choice == "3":
            stopWatch.display()
        elif choice == "4":
            stopWatch.reset()
        elif choice == "5":
            print("Exiting stopwatch. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nStopwatch terminated. Goodbye!")
