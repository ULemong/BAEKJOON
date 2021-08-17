stack_push = []
count = 1
answer = ''

for i in range(int(input())):
    n = int(input())

    while count <= n:
        stack_push.append(count)
        count += 1
        answer += '+'

    if stack_push[-1] != n:
        print('NO')
        exit(0)

    stack_push.pop()
    answer += '-'

print('\n'.join(answer))
