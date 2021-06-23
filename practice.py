def run():
    arr = [-1, 10, 2, 6, 5, 4, 9]
    newArr = quickSort(arr)

    print(newArr)

# 선택 정렬
def selectionSort(arr):
    length = len(arr)

    for i in range(length):
        smallest = i

        for j in range(i, length):
            if arr[j] < arr[smallest]:
                smallest = j

        tmp = arr[i]
        arr[i] = arr[smallest]
        arr[smallest] = tmp

    return arr

# 삽입 정렬
def insertionSort(arr):
    length = len(arr)

    for i in range(1, length):
        key = arr[i]

        for j in range(i-1, -1, -1):
            if arr[j] > key:
                arr[j+1] = arr[j]
                arr[j] = key

            else: arr[j+1] = key; break

    return arr

# 퀵 정렬
def quickSort(arr):
    length = len(arr)
    if length <= 1: return arr

    pivot = arr[0]

    left = []
    right = []

    for i in range(1, length):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    left = quickSort(left)
    right = quickSort(right)

    return left + [pivot] + right


if __name__ == "__main__":
    run()