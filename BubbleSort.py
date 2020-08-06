def bubble(list):
    sorted = False
    length = len(list) - 1

    while not sorted:
        sorted = True
        for i in range(length):
            if list[i] > list[i+1]:
                sorted = False
                list[i], list[i+1] = list[i+1], list[i]
    
    return list

lst_str = input('임의의 숫자들을 입력하세요. ( 띄어쓰기로 구분 ) \n')
lst = lst_str.split(' ')
print('정렬 결과: ', ' '.join(bubble(lst)))