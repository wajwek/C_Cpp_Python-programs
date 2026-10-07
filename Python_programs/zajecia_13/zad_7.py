import time

class Timer():
    def __init__(self):
        self.start_time = 0
        self.end_time = 0

    def start(self):
        self.start_time = time.time()
    def stop(self):
        self.end_time = time.time()
    def elapsed(self):
        return f"{self.end_time - self.start_time:.2f}"

t = Timer()
t.start()
time.sleep(1)
t.stop()
print(f"Zmierzony czas: {t.elapsed()} s")