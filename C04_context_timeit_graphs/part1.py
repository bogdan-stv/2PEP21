# context manager
# with class -------------------------------------

class FileOpener:

    def __init__(self, file_name, mode):
        self.my_file = open(file_name, mode)

    def __enter__(self):
        print("in enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("in exit")
        self.my_file.close()
        if exc_type == AttributeError:
            print("We will ignore this exception")
            return True

    def write_something(self):
        self.my_file.write("something")


# with FileOpener("textfile.txt", "w") as file:
#     file.write_something()
#     raise AttributeError

# with generator ---------------------------------

from contextlib import contextmanager

@contextmanager
def file_opener(file_name, mode):
    my_file = open(file_name, mode)
    try:
        yield my_file
    except AttributeError:
        print("We will ignore this exception")
    finally:
        print("in exit")
        my_file.close()

# with file_opener("textfile.txt", "w") as file:
#     file.write("something2")
#     raise AttributeError

# check methods
# print(dir(file_opener))

#------------------------------------------------------#
# timing execution
import timeit
import time

# x = timeit.timeit('print("x")')

# import timeit
# import time
#
# def factorial(n):
#     result = 1
#     for i in range(1,n+1):
#         result *=i
#     return result
#
# def factorial2(n):
#     if n<=1:
#         return 1
#     else:
#         return n*factorial2(n-1)
#
# def timing():
#     a=[]
#     b=[]
#     for i in range(1,999):
#         y=time.time()
#         factorial(i)
#         z=time.time()
#         a.append(z-y)
#     for i in range(1,999):
#         y=time.time()
#         factorial(i)
#         z=time.time()
#         b.append(z-y)
#     return a,b
#
#
# print(timing())

#factorial(3)
#x=timeit.timeit('factorial(3)')
#print(x)

















