import timeit
import matplotlib.pyplot as plt

result1 = timeit.timeit('f"Numbers are:{[1,2,3,4,5,6,7,8,9,10]}"')
result2 = timeit.timeit('"Numbers are:{}".format([1,2,3,4,5,6,7,8,9,10])')

l1, l2 = [], []

def grafic():
    for _ in range(100):
        result1 = timeit.timeit('f"Numbers are:{[1,2,3,4,5,6,7,8,9,10]}"', number=100)
        l1.append(result1)
        result2 = timeit.timeit('"Numbers are:{}".format([1,2,3,4,5,6,7,8,9,10])', number=100)
        l2.append(result2)
    return (l1, l2)

y1, y2 = grafic()

# def remove_spikes(y1, y2):
#     sum1 =0
#     sum2 =0
#     for i in range(len(y1)):
#         sum1 += y1[i]
#         sum2 += y2[i]
#     x1 = sum1/len(y1)
#     x2 = sum2/len(y2)
#     print(x1,x2)

# remove_spikes(y1, y2)

fig1, (ay1, ay2) = plt.subplots(nrows=2, ncols=1, sharex='all')
fig1.dp1 = 200.0
ay1.plot([i for i in range(100)], y1)
ay2.plot([i for i in range(100)], y2)

plt.show()






