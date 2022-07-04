import time

def selection_sort(data,drawData,timeTick):
    for j in range(len(data)):
        min_index = j
        for i in range(j, len(data)):
            if data[i] < data[min_index]:
                min_index = i
                drawData(data, ['yellow' if x == min_index else "green" if x <= j else  "red" for x in range(len(data))])
                time.sleep(timeTick)
        drawData(data, ['blue' if x == min_index or x == iter else "green" if x <= j else "red" for x in range(len(data))])
        time.sleep(timeTick)
        data[min_index], data[j] = data[j], data[min_index]
    drawData(data, ['green' for x in range(len(data))])
