import numpy as np
import matplotlib.pyplot as plt
import sys

def ins(arr):
    u = np.arange(0, AMOUNT, 1)
    for x in range(len(arr) - 1):
        if arr[x] > arr[x + 1]:
            val = arr[x + 1]
            y = x + 1
            while (arr[y - 1] > val and y > 0):
                arr[y] = arr[y - 1]
                z = plt.bar(u, arr)
                #z[y].set_color('g')
                z[y-1].set_color('r')
                plt.pause(0.1)
                plt.clf()
                y -= 1
            arr[y] = val
            z = plt.bar(u, arr)
            z[y].set_color('g')
            plt.pause(0.5)
            plt.clf()

    plt.show()
    return arr


arr = np.random.randint(1,100, 10)
AMOUNT = 10

ins(arr)
