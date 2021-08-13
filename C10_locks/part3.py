import time
import random
import threading
from multiprocessing import  Queue
from threading import Thread

def cpu_load(x, queue:Queue):
    start = time.time()
    end = start + random.randint(1, 10)
    while end > time.time():
        x * x
    queue.get()
    start = time.time()
    while not queue.empty():
        time.sleep(0.1)
    end = time.time()
    print(f'{end - start} {threading.current_thread().getName()}')

if __name__ == '__main__':
    queue = Queue()
    for i in range(20):
        queue.put(True)
    for i in range(20):
        process = Thread(target=cpu_load, args=(100, queue))
        process.start()
