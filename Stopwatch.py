import time

class Timer:
    def __init__(self, seconds):
        self.seconds = seconds
        self.start = time.time()
        self.end = self.start + self.seconds
        self.paused = False
    
    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

    def reset(self):
        self.start = time.time()
        self.end = self.start + self.seconds
        self.paused = False

    def stop(self):
        self.end = self.start
        self.paused = True
    
    def get_time_left(self):
        if self.paused:
            return self.end - self.start
        else:
            return self.end - time.time()

    def is_finished(self):
        return time.time() >= self.end

# Example usage:
timer = Timer(10) # 10 seconds

while not timer.is_finished():
    time_left = timer.get_time_left()
    print(f"Time left: {time_left:.2f} seconds")
    time.sleep(1)

print("Time's up!")
