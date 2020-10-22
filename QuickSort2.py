def run():
    result = quick_sort([4, 2, 5, 10, 3, 1, 9])
    print(result)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    less_arr, equal_arr, greater_arr = [], [], []

    for num in arr:
        if pivot > num:
            greater_arr.append(num)
        elif pivot < num:
            less_arr.append(num)
        else:
            equal_arr.append(num)

    return quick_sort(less_arr) + equal_arr + quick_sort(greater_arr)

if __name__ == "__main__":
    run()