
# Create application with GUI in python that allows user to specify several
# timezones and will pull show time in UI for each timezone user provides
#
# - documentation and type hints (20p)
# - UI for user input of timezones (10p)
# - UI for user input of timezones (10p)
# - retrieve information from API server (10p)
# - use of parallel execution to pull multiple time zones (20p)
# - application correctly processes input and returns time (30)
import json
import tkinter
from multiprocessing import Process

import requests


class TimeGUI:
    """application with GUI in python that allows user to specify several
        timezones and will pull show time in UI for each timezone user provides"""

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.zones = []
        self.process_list = []
        # self.my_list = [1,2,3]
        # self.text1 = tkinter.Text(self.main_window)
        # self.text1.grid()
        # self.button1 = tkinter.Button(self.main_window, command=self.insert_text)
        # self.button1.grid()

    def run(self):
        self.main_window.mainloop()

    # def insert_text(self):
    #     print(self.my_list.pop())
    #     print(self.my_list)
    #     self.text1.insert('0.0', str(self.my_list))

    def timezone_getter(self, location='Europe'):
        response = requests.get(f'http://worldtimeapi.org/api/timezone/{location}')
        my_timezone_str = response.text
        my_timezone = json.loads(my_timezone_str)
        for item in my_timezone:
            self.zones.append(str(item).split('/')[1])
        print(self.zones)

    def time_getter(self):
        response = requests.get(f'http://worldtimeapi.org/api/timezone/Europe/{str(self.zones.pop())}')
        my_timezone_str = response.text
        my_timezone = json.loads(my_timezone_str)
        print(my_timezone)

    def time_multi(self):
        self.process_list = [Process(target=self.time_getter) for i in range(4)]
        for pr in self.process_list:
            pr.start()
        for pr in self.process_list:
            pr.join()

if __name__ == "__main__":
    time_gui = TimeGUI()
    time_gui.timezone_getter()
    time_gui.time_multi()

"""Traceback (most recent call last):
  File "C:\Users\bogda\Desktop\Projects\PycharmProjects\PYM2\Test\app01.py", line 64, in <module>
    time_gui.time_multi()
  File "C:\Users\bogda\Desktop\Projects\PycharmProjects\PYM2\Test\app01.py", line 57, in time_multi
    pr.start()
  File "C:\Users\bogda\AppData\Local\Programs\Python\Python39\lib\multiprocessing\process.py", line 121, in start
    self._popen = self._Popen(self)
  File "C:\Users\bogda\AppData\Local\Programs\Python\Python39\lib\multiprocessing\context.py", line 224, in _Popen
    return _default_context.get_context().Process._Popen(process_obj)
  File "C:\Users\bogda\AppData\Local\Programs\Python\Python39\lib\multiprocessing\context.py", line 327, in _Popen
    return Popen(process_obj)
  File "C:\Users\bogda\AppData\Local\Programs\Python\Python39\lib\multiprocessing\popen_spawn_win32.py", line 93, in __init__
    reduction.dump(process_obj, to_child)
  File "C:\Users\bogda\AppData\Local\Programs\Python\Python39\lib\multiprocessing\reduction.py", line 60, in dump
    ForkingPickler(file, protocol).dump(obj)
TypeError: cannot pickle '_tkinter.tkapp' object

Process finished with exit code 1"""
