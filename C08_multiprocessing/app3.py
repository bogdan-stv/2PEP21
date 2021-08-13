import os
import random
import time
from multiprocessing import Process, Queue, Pipe


def generate_numbers(q, p):
    for i in range(5):
        q.put(random.randint(0, 500))
        time.sleep(1)

def power(q, p):
    x = q.get()
    print(f'{os.getpid()} proccesing for 1 second')
    time.sleep(1)
    p[0].send(x*x)
    time.sleep(3)
    p[0].close()

if __name__ == '__main__':
    q = Queue()
    p = Pipe()
    process1 = Process(target=generate_numbers, args=(q,p))
    process_list = [process1]
    for i in range(3):
        process = Process(target=power, args=(q,p))
        process_list.append(process)
    for process in process_list:
        process.start()
    time.sleep(0.1)
    print(p[1].recv())
    for process in process_list:
        print(type(process.join()))





