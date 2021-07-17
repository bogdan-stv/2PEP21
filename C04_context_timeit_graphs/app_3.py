from app_2 import timing
import matplotlib.pyplot as plt

x, y = timing()

fig1, ay1 = plt.subplots(nrows=1, ncols=1, sharex='all')
ay1.plot([i for i in range(1, 999)], x, y, label="factorial")
plt.xlabel('it')
plt.ylabel('time')
plt.title("factorial")
ay1.legend()

plt.show()