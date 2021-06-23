from collections import deque

TEXT = input()

stack = deque([])

for word in TEXT:
    if "A" <= word <= "Z": print(word, end="")
    else:
        if word == "*" or word == "/" or word =="(": stack.append(word)

        elif word == ")" or word =="+" or word =="-":
            while True:
                if stack:
                    pop = stack.pop()
                    if pop == "(": break
                    else: print(pop, end="")

                else: break

            if word == "+" or word =="-":
                stack.append(word)

while True:
    if stack:
        pop = stack.pop()
        print(pop, end="")

    else: break