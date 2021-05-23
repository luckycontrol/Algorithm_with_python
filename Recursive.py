import sys

def run():
    hanoi_tower(4, 'A', 'B', 'C')

def recursiveSum(n):
    if n == 1: return 1
    return n + recursiveSum(n - 1)

def getMaxInList(arr):
    return max(arr)

def power(x, n):
    if n == 0: return 1
    elif n % 2 == 0: return power(x * x, n / 2)
    else: return x * power(x * x, (n - 1) / 2)

def hanoi_tower(n, _from, _tmp, _to):
    if n == 1: print(f'원판 1을 {_from} 에서 {_to}로 옮긴다.')
    else:
        hanoi_tower(n, _from, _to, _tmp)
        print(f'원판 {n}을 {_from} 에서 {_to}로 옮긴다.')
        hanoi_tower(n, _tmp, _from, _to)

if __name__ == "__main__":
    sys.setrecursionlimit(100000000)
    run()