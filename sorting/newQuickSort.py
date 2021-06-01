def run():
    arr = [4, 2, 3, 1, 7, 6]
    newArr = quickSort(arr)

    print(newArr)

def quickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = []
    right = []

    for val in arr[1:]:
        if val <= pivot:
            left.append(val)
        
        else:
            right.append(val)
    
    left = quickSort(left)
    right = quickSort(right)

    return left + [pivot] + right

if __name__ == "__main__":
    run()