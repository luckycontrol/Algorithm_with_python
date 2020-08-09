# A + B 구하기

# 두 정수 A와 B를 입력받은 다음, A + B를 출력하는 프로그램.

# 첫째 줄에 A와 B가 주어집니다.
# ex) 1 2

def checkInputNums(num1, num2):
    if num1, num2 > 0 and num1, num2 < 10:
        return True
    else:
        return False

while True:

    nums = map(int, input().split())
    