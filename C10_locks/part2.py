import threading
import time
from threading import Thread , Lock, Event

def cpu_load(x,event:Event):
    start = time.time()
    end=start + 2
    while end > time.time():
        x * x
    event.wait()
    event.clear()
    print(f'{threading.current_thread().name}')
    event.set()

if __name__ == "__main__":
    event=Event()
    event.set()
    for i in range (60):
        process = Thread(target=cpu_load,args=(100,event))
        process.start()