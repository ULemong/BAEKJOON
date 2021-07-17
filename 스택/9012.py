import sys

for _ in range(int(input())):
    stack = []
    s = sys.stdin.readline().rstrip()

    for i in range(len(s)):
        stack.append(s[i])

        if stack[0] == ')':
            break
        else:
            if s[i] == ')' and stack[-2] == '(':
                stack.pop()
                stack.pop()

    if len(stack) == 0: print('YES')
    else: print('NO')