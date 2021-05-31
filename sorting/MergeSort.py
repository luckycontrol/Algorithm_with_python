def run():
    arr = [2, 4, 1, 3, 7, 5]
    newArr = mergeSort(arr)
    
    print(newArr)

def merge(left, right):
    result = []

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        
        else:
            result.append(right[0])
            right = right[1:]
        
    if len(left) > 0:
        for i in left:
            result.append(i)
        
    else:
        for i in right:
            result.append(i)

    return result

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)

if __name__ == "__main__":
    run()