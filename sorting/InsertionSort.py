def run():
    size = 8
    arr = [1, 9, 2, 3, 4, -1, 10, 5]

    newArr = insertionSort(arr, size)
    print(newArr)

def insertionSort(arr, size):
    for i in range(1, size):
        key = arr[i]
        for j in range(i, -1, -1):
            if key > arr[j]:
                arr[j+1] = arr[j]
            else:
                arr[j+1] = key
                break
    
    return arr
        

if __name__ == "__main__":
    print(list(range(10, 1, -1)))