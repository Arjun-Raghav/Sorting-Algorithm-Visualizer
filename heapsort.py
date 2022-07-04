import time

def heap_sort(data,drawData,timeTick):
    for index in range(len(data) // 2 - 1, -1, -1):
        to_heap(data, index, len(data),drawData,timeTick)
    for i in range(len(data) - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        to_heap(data, 0, i,drawData,timeTick)
        drawData(data, ['green' if x >= i else 'red' for x in range(len(data))])
        time.sleep(timeTick)
    drawData(data, ['green' for x in range(len(data))])
