def run():
    size = 7
    arr = [1, 9, 2, 3, 4, 10, 5]

    newArr = bubbleSort(arr, size)
    print(newArr)

def bubbleSort(arr, size):
    for i in range(size - 1, -1, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
    
    return arr

if __name__ == "__main__":
    run()