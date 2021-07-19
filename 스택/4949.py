import sys

while True:
    new_s = []
    stack = []

    s = sys.stdin.readline().rstrip()

    if s == '.':
        exit(0)

    for i in s:
        if i == '[' or i == ']' or i == '(' or i == ')':
            new_s.append(i)

    for i in new_s:
        stack.append(i)

        if stack[0] == ']' or stack[0] == ')':
            break
        else:
            if (i == ']' and stack[-2] == '[') or (i == ')' and stack[-2] == '('):
                stack.pop()
                stack.pop()

    if len(stack) == 0: print('yes')
    else: print('no')