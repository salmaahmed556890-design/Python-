import threading
import time

sema = threading.Semaphore(2)

def process(name):
    print(f"{name} waiting...")
    with sema:
        print(f"{name} acquired semaphore")
        time.sleep(1)
        print(f"{name} released semaphore")

threads = []

for i in range(5):
    t = threading.Thread(target=process, args=(f"Thread {i+1}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
