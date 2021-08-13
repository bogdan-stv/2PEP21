import time
import random
import threading
from threading import Thread, Barrier

def cpu_load(x, berrier:Barrier):
    start = time.time()
    end = start + random.randint(1, 10)
    while end > time.time():
        x * x
    start = time.time()
    berrier.wait()
    end = time.time()
    print(f'{end - start} {threading.current_thread().getName()}')

if __name__ == '__main__':
    barrier = Barrier(20)
    for i in range(20):
        process = Thread(target=cpu_load, args=(100, barrier))
        process.start()
