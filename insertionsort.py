import time

def insertion_sort(arr, drawData, timeTick):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]
        j = i - 1
        k = i
        drawData(arr, ['black' if x == i else 'red' for x in range(len(arr))])
        time.sleep(timeTick)
        while j >= 0 and key < arr[j]:


            drawData(arr, ['yellow' if x == j else 'blue' if x == k else 'red' for x in range(len(arr))])
            arr[j + 1],arr[j]=arr[j],arr[j+1]
            j -= 1
            k-=1

            time.sleep(timeTick)
        arr[j + 1] = key
    drawData(arr, ['green' for x in range(len(arr))])
