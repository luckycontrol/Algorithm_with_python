# 1로 만들기

# 정수 X에 사용할 수 있는 연산은 다음 3가지이다.
#  1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
#  2. X가 2로 나누어 떨어지면, 2로 나눈다.
#  3. 1을 뺀다.

# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다.
# 연산을 사용하는 횟수의 최솟값을 출력하시오.

# 입력 - 첫째 줄에 1보다 크거나 같고, 10^6보다 작거나 같은 정수 N이 주어진다.
# 출력 - 첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

def checkInputNumber(num):
    if num >= 1 and num <= 1000000:
        return True
    else:
        return False

def getNumberOne(num):
    count = 0

    while not num == 1:
        if num % 3 > 1:
            if num % 2 == 0:
                num = num / 2
                count += 1
            
            else:
                num = (num - 1) / 2
                count += 2
        
        elif num % 3 == 1:
            num = (num - 1) / 3
            count = count + 2
        
        elif num % 3 == 0:
            num = num / 3
            count += 1
        
        else:
            num = num / 2
            count += 1
    
    return count

while True:
    n = input()
    
    if(checkInputNumber(int(n))):
        break

print(getNumberOne(int(n)))
