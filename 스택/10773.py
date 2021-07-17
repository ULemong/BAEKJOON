import sys
stack = []

for i in range(int(input())):
    n = int(sys.stdin.readline())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))