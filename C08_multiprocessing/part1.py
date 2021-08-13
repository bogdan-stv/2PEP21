from time import sleep
from multiprocessing import Process

def sleep1(time):
    sleep(time)
    print('done with sleep')


    for i in range(value):
        sleep(1)
        print(f'done with count: {i}')

process1 = Process(target=count1, args=(3,), kwargs={})
process2 = Process(target=sleep1, args=(4,), kwargs={})

if __name__ == "__main__":
    process2.start()
    process1.start()
    process1.join()
    print('All done')




