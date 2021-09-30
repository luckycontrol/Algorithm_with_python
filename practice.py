def run():
    arr = [2, 1, 9, 3, 5, 4, 12, 10]

    h = Heap()
    for element in arr: h.insert(element)

    print(h.delete())
    print(h.delete())
    print(h.delete())
    print(h.delete())
    print(h.delete())
    print(h.delete())

def SelectionSort(arr: [int]):
    length = len(arr)

    for i in range(length):
        smallest = i

        for j in range(i, length):
            if arr[j] < arr[smallest]: smallest = j

        arr[i], arr[smallest] = arr[smallest], arr[i]

def InsertionSort(arr: [int]):
    length = len(arr)

    for i in range(1, length):
        pick = arr[i]
        idx = i

        for j in range(i - 1, -1, -1):
            if arr[j] > pick:
                arr[j + 1] = arr[j]
                idx = j

        arr[idx] = pick

def BubbleSort(arr: [int]):
    length = len(arr)

    for i in range(length - 1):
        for j in range(i, length - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def QuickSort(arr: [int]):
    if len(arr) <= 1: return arr

    pivot = arr[0]

    left  = []
    right = []

    for element in arr[1:]:
        if element < pivot  : left.append(element)
        else                : right.append(element)

    newLeft = QuickSort(left)
    newRight = QuickSort(right)

    return newLeft + [pivot] + newRight

class Heap:
    def __init__(self):
        self.arr = [0]

    def insert(self, n):
        idx = len(self.arr)
        self.arr.append(n)

        while idx != 1 and n < self.arr[idx // 2]:
            self.arr[idx] = self.arr[idx // 2]
            idx //= 2

        self.arr[idx] = n

    def delete(self):
        returnValue = self.arr[1]
        lastValue   = self.arr.pop()

        parentIdx   = 1
        childIdx    = 2

        while childIdx < len(self.arr) - 1:
            if self.arr[childIdx + 1] < self.arr[childIdx]:
                childIdx += 1

            if lastValue < self.arr[childIdx]: break

            self.arr[parentIdx] = self.arr[childIdx]
            parentIdx = childIdx
            childIdx *= 2

        self.arr[parentIdx] = lastValue
        return returnValue


if __name__ == "__main__":
    run()