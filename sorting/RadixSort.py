from collections import deque
from queue import Queue

BUCKET = 10
DIGIT = 2

def run():
    arr = [28, 93, 39, 81, 62, 72, 38, 26]
    newArr = radixSort(arr)

    print(newArr)

def radixSort(arr):
    queues = [deque() for _ in range(BUCKET)]
    factor = 1
    length = len(arr)

    for d in range(DIGIT):
        for i in range(length):
            idx = (arr[i] // factor) % 10
            queues[idx].append(arr[i])

        i = 0
        for b in range(BUCKET):
            while len(queues[b]) >= 1:
                arr[i] = queues[b].popleft()
                i += 1

        factor *= 10

    return arr

if __name__ == "__main__":
    run()