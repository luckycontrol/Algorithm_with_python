def run():
    arr = [2, 1, 5, 6, 4, 3, 9, 8, 10]
    size = 9
    newArr = cellSort(arr, size)

    print(newArr)

def cellSort(arr, size):

    _arr = arr

    gap = size // 2
    if gap != 0 and gap % 2 == 0: gap += 1

    while gap > 0:
        for i in range(gap):
            _arr = insertionSort(_arr, i, size-1, gap)
        
        gap = gap // 2
        if gap != 0 and gap % 2 == 0: gap += 1

    return _arr

def insertionSort(arr, first, last, gap):
    _arr = arr
    for i in range(first + gap, last + 1, gap):
        key = _arr[i]

        for j in range(i - gap, first, -gap):
            if arr[j] > key: arr[j + gap] = arr[j]
            else: arr[j + gap] = key; break
        
    return _arr


if __name__ == "__main__":
    run()