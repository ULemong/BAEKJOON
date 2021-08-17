for _ in range(int(input())):

    data = input()
    left = []
    right = []

    for i in data:
        if i == '<':
            if left:
                right.append(left.pop())
        elif i == '-':
            if left:
                left.pop()
        elif i == '>':
            if right:
                left.append(right.pop())
        else:
            left.append(i)

    left.extend(reversed(right))
    print(''.join(left))