import json
import requests
import time
from multiprocessing import Process, Queue, SimpleQueue

url1 = 'http://worldtimeapi.org/api/timezone/Europe/{}'
url2 = f'http://worldtimeapi.org/api/timezone'


def timezone_getter(q,location='Europe'):
    response = requests.get(url2)
    my_timezone_str = response.text
    my_timezone = json.loads(my_timezone_str)
    zone_list = list(filter(lambda t: t, map(lambda z: z.rsplit('/', maxsplit=1)[-1] if location in z else None, my_timezone)))
    for zone in zone_list:
        q.put(zone)
        # length = ZONES.qsize()
        # print(length)

def time_getter(q):
    while q.empty():
        time.sleep(1)
    response = requests.get(url1.format(q.get()))
    my_time_str = response.text
    print(json.loads(my_time_str))


if __name__ == '__main__':
    ZONES = Queue()
    process1 = Process(target=timezone_getter, args=(ZONES,))
    process_list = [Process(target=time_getter, args=(ZONES,)) for _ in range(10)]
    process1.start()
    started_processes = [process1]
    for process in process_list:
        process.start()
        started_processes.append(process)
    for i in range(100):
        if ZONES.qsize() < 43:
            for j in started_processes:
                j.terminate()
        time.sleep(1)
