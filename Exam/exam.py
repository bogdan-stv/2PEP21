import json
import tkinter
from multiprocessing import Queue
from functools import partial
from threading import Thread

import requests


class TimeUI:
    """ UI class that retrieves timezones"""

    def __init__(self):
        """constructor"""

        self.main_window = tkinter.Tk()
        self.main_window.title('Main Window')
        self.zones = []
        self.button0 = tkinter.Button(self.main_window, text='get timezones', command=self.buttons)
        self.button0.grid()
        self.process_list = []
        self.q = Queue()

        self.test_button = tkinter.Button(self.main_window, text='Test', command=self.return_string)
        self.test_button.grid()

    def timezone_getter(self, location='Europe'):
        """get timezones from api"""
        response = requests.get(f'http://worldtimeapi.org/api/timezone/{location}')
        my_timezone_str = response.text
        my_timezone = json.loads(my_timezone_str)
        self.zones = []
        for item in my_timezone:
            self.zones.append(str(item).split('/')[1])
        print(self.zones)

    def buttons(self):
        """create buttons"""
        self.timezone_getter()
        for city in self.zones[:10]:
            command = partial(self.get_time, str(city))
            button = tkinter.Button(self.main_window, text=f'{city}', command=command)
            button.grid()

    def time_getter(self, city:str):
        """gets time"""
        response = requests.get(f'http://worldtimeapi.org/api/timezone/Europe/{city}')
        my_timezone_str = response.text
        my_timezone = json.loads(my_timezone_str)
        self.q.put(my_timezone)
        return my_timezone

    def get_time(self, city:str):
        new_window = tkinter.Tk()
        new_window.title("new window")
        th1 = Thread(target=self.time_getter, args=(str(city),))
        th1.start()
        self.label1 = tkinter.Label(new_window,text=str(self.q.get()))
        self.label1.grid()

    def run(self):
        self.main_window.mainloop()

    def return_string(self):
        return 'abc'

time_ui = TimeUI()
time_ui.run()
