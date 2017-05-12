import random
arr = random.sample(xrange(1, 101), 10)

def bubbleSort(arrList):
    for i in range(0, len(arrList)-1):
        for j in range(0, len(arrList) - 1 - i):
            if arrList[j] > arrList[j+1]:
                arrList[j], arrList[j+1] = arrList[j+1], arrList[j]

    return arrList

print   " ".join(map(str, bubbleSort(arr)))