stack = []
answer = []
count = 1

for _ in range(int(input())):
    n = int(input())

    while count <= n:
        stack.append(count)
        answer.append('+')
        count += 1
    if stack[-1] == n:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        exit(0)

print('\n'.join(answer))