import sys
stack = []

for i in range(int(input())):
    s = sys.stdin.readline().rstrip().split()
    if s[0] == 'push':
        stack.append(int(s[1]))
    elif s[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif s[0] == 'size':
        print(len(stack))
    elif s[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    else:
        if len(stack) == 0:
            print(1)
        else:
            print(0)