import numpy as np
import matplotlib.pyplot as plt
import sys

arr = np.random.randint(0,100, 20)
AMOUNT = 20
col = []

arr2 = [10,8,3,2,4,6,7,9,2,1] #small arr for quick visual and testing purp only

for x in range(20):
    col.append((0, 0, 0.1+(0.025*(x+1))))

def bub(arr):
    try:
        x = np.arange(0, AMOUNT,1)
        small = 0
        big = 1
        for q in range(len(arr)):
            for y in range(0, len(arr)-1):
                z = plt.bar(x, arr)
                for i in z:
                    if i.get_height() == small and z.index(i) == y-1:
                        z[z.index(i)].set_color("r")
                    if i.get_height() == big and z.index(i) == y:
                        z[z.index(i)].set_color("g")
                plt.pause(0.1)
                plt.clf()
                if arr[y] > arr[y+1]:
                    arr[y], arr[y+1] = arr[y+1], arr[y]
                    big = arr[y+1]
                    small = arr[y]
        plt.show()
    except KeyboardInterrupt:
        sys.exit()


bub(arr)

