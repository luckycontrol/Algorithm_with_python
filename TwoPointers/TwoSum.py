numbers = [2, 7, 11, 15]
target = 9

first = 0
last = len(numbers) - 1

while first < last:
    firstNum = numbers[first]
    lastNum = numbers[last]

    if firstNum + lastNum == target:
        print([first + 1, last + 1])
        break
    
    if firstNum + lastNum < target:
        first += 1
    else:
        last -= 1