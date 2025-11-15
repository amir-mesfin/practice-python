import threading
import time

def worker(name):
    for i in range(3):
        time.sleep(1)
        print(f"{name} → {i}")

t1 = threading.Thread(target=worker, args=("Thread-1",))
t2 = threading.Thread(target=worker, args=("Thread-2",))

t1.start()
t2.start()

t1.join()
t2.join()

print("All threads finished!")
