import time

def to_heap(array, chosen_root, n, display, speed):
    time.sleep(speed)
    index = chosen_root
    l = 2 * chosen_root + 1
    r = 2 * chosen_root + 2

    if l < n and array[index] < array[l]:
        index = l
    if r < n and array[index] < array[r]:
        index = r
    if index != chosen_root:
        display(array,
                ['blue' if x == chosen_root or x == index else 'green' if x >= n else 'red' for x in range(len(array))])
        array[index], array[chosen_root] = array[chosen_root], array[index]
        to_heap(array, index, n, display, speed)


def heap_sort(data,drawData,timeTick):
    for index in range(len(data) // 2 - 1, -1, -1):
        to_heap(data, index, len(data),drawData,timeTick)
    for i in range(len(data) - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        to_heap(data, 0, i,drawData,timeTick)
        drawData(data, ['green' if x >= i else 'red' for x in range(len(data))])
        time.sleep(timeTick)
    drawData(data, ['green' for x in range(len(data))])
