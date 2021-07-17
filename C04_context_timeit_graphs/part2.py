# generate graphs

import matplotlib.pyplot as plt

fig1, (ay1, ay2) = plt.subplots(nrows=2, ncols=1, sharex='all')
fig1.dp1 = 200.0

ay1.plot([1,2,3], [5,5,5], label='Test1')
ay1.legend()
ay2.plot([3,4,5], [4,4,5], label='Test2')
ay2.legend()
plt.xlabel('seconds')
plt.ylabel('$')
plt.title('Money over time')

plt.show()

