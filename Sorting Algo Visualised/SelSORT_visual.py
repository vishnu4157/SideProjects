import numpy as np
import matplotlib.pyplot as plt

def sel(arr, start, end, u):
    z = plt.bar(u, arr)
    if start >= end:
        return arr
    mini = arr[start]
    index = start
    for x in range(start+1, end, 1):
        if arr[x] < mini:
            mini = arr[x]
            index = x
    z[start].set_color('g')
    z[index].set_color('r')
    temp = arr[start]
    arr[start] = mini
    arr[index] = temp
    z[start].set_color('r')
    z[index].set_color('g')
    plt.pause(0.5)
    plt.clf()
    return sel(arr, start+1, end,u)



arr = [10,9,8,7,6,5,4,3,2,1]

def visual_sel_sort(arr):
    u = np.arange(0, 10, 1)
    ins(arr,0,10,u)
    plt.show()
    print(arr)

visual_sel_sort(arr)
