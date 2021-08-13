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
    if threading.current_thread().getName() == 'Thread-3':
        raise AttributeError
    try:
        berrier.wait()
    except threading.BrokenBarrierError:
        pass
    end = time.time()
    print(f'{end - start} {threading.current_thread().getName()}')

if __name__ == '__main__':
    barrier = Barrier(20, timeout=11)
    for i in range(20):
        process = Thread(target=cpu_load, args=(100, barrier))
        process.start()
