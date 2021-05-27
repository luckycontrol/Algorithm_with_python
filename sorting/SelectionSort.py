def run():
    arr_size = 8
    arr = [1, 9, 2, 3, 4, -1, 10, 5]

    newArr = selectionSort(arr, arr_size)
    print(newArr)

def selectionSort(arr, size):
    for i in range(size - 1):
        smallest = i
        for j in range(i+1, size):
            if arr[j] < arr[smallest]: smallest = j
        
        tmp = arr[i]
        arr[i] = arr[smallest]
        arr[smallest] = tmp

    return arr


if __name__ == "__main__":
    run()