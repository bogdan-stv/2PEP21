import json
import requests
import time
from multiprocessing import Process, Value, Array

url1 = 'http://worldtimeapi.org/api/timezone/Europe/{}'
url2 = f'http://worldtimeapi.org/api/timezone'

ZONES = []

def timezone_getter(location='Europe'):
    response = requests.get(url2)
    my_timezone_str = response.text
    my_timezone = json.loads(my_timezone_str)
    ZONES.extend(list(filter(lambda t: t, map(lambda z: z.rsplit('/', maxsplit=1)[-1] if location in z else None, my_timezone))))
    return ZONES

def time_getter(ZONES):
    while not ZONES:
        time.sleep(0.1)
    response = requests.get(url1.format(ZONES.pop()))
    my_time_str = response.text
    return json.loads(my_time_str)

process1 = Process(target=timezone_getter)
process_list = [Process(target=time_getter) for _ in range(4)]

if __name__ == '__main__':
    process1.start()
    for process in process_list:
        process.start()