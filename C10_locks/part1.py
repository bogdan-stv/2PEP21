import time
import threading
from threading import Thread, Lock

def cpu_load(x, lock:Lock):
    start = time.time()
    end = start + 4
    while end > time.time():
        x * x
    while lock.locked():
        time.sleep(0.1)
    lock.acquire()
    print(f'{threading.current_thread().getName()}')
    lock.release()

if __name__ == '__main__':
    lock = Lock()
    for i in range(20):
        process = Thread(target=cpu_load, args=(100, lock))
        process.start()
