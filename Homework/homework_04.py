""" Create a context manager that will time how long it took to execute the context and display a graph with
execution time when the context ends.
Since the same instance can be used in multiple contexts make sure that the graph will show data for each time the
object was used in a context
"""
from contextlib import contextmanager
from time import time
import matplotlib.pyplot as plt

x, l_x, l_y = 0, [], []
@contextmanager
def timing():
    global x
    start_time = time()
    try:
        yield
    finally:
        # time to execute
        end_time = time() - start_time
        # display the graph
        l_x.append(x+1), l_y.append(end_time)
        plt.plot(l_x, l_y)
        plt.show()
        x += 1

with timing():
    my_list0 = [i for i in range(100000)]

with timing():
    my_list2 = [i for i in range(1000000)]

with timing():
    my_list3 = [i for i in range(10000000)]



