import random

# 1. 맨 우측 인덱스가 피벗이 된다.
# 2. 피벗을 제외한 나머지를 둘로 나눈다.
# 3. 나눌 것이 더이상 없을 경우 정렬을 시작한다. ( 오름차순 )
def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than the pivot 
        if   arr[j] < pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 



lst_str = input('숫자들을 입력하세요: ( 공백으로 구분 ) \n')
lst = lst_str.split(' ')
quickSort(lst, 0, len(lst) - 1)
print(lst)