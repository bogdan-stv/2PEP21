# do not execute function if time is between 10 am and 10 pm

import time

def workinghours(start_time, end_time):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            if(start_time>"10:00" and end_time<"22:00"):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@workinghours("10:01", "18:00")
def working(work: str):
    print("doing some work")
    time.sleep(3)

working("ceva")