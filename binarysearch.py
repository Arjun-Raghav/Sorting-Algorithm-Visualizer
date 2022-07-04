import time


def binary_search(data, element, drawData, timeTick):
    l = 0
    r = len(data) - 1
    code_binarysearch(data, element, drawData, timeTick, l, r)


def code_binarysearch(data, element, drawData, timeTick, l, r):
    if (l > r):
        drawData(data, ["black" for x in range(len(data))])
        time.sleep(timeTick)
        return
    mid = (l + r) // 2
    if (data[mid] == element):
        drawData(data, ['green' if x == mid else "white" for x in range(len(data))])
        time.sleep(timeTick)
        return
    elif (data[mid] < element):
        new_l = mid + 1
        drawData(data, ['blue' if x == l else "red" if x == r else "white" for x in range(len(data))])
        time.sleep(timeTick)
        code_binarysearch(data, element, drawData, timeTick, new_l, r)
    else:
        new_r = mid - 1
        drawData(data, ['blue' if x == l else "red" if x == r else "white" for x in range(len(data))])
        time.sleep(timeTick)
        code_binarysearch(data, element, drawData, timeTick, l, new_r)

