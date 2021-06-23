from collections import deque

N = int(input())
TEXT = input()
NUMBERS = [int(input()) for _ in range(N)]

stack = deque([])

for word in TEXT:
    if "A" <= word <= "Z": stack.append(NUMBERS[ord(word) - ord("A")])
    else:
        num1 = stack.pop()
        num2 = stack.pop()

        if word == "+":
            stack.append(num1 + num2)

        elif word == "-":
            stack.append(num2 - num1)

        elif word == "*":
            stack.append(num1 * num2)

        elif word == "/":
            stack.append(num2 / num1)

print("%.2f" % stack[0])