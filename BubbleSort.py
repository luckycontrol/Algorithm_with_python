def test(list):
    sorted = False
    length = len(list) - 1

    while not sorted:
        sorted = True
        for i in range(length):
            if list[i] > list[i+1]:
                sorted = False
                list[i], list[i+1] = list[i+1], list[i]
    
    return list

lst = [1, 3, -2, 70, 9]
print(test(lst))