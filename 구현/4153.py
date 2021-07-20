while True:
    n = list(map(int, input().split()))

    if n == [0, 0, 0]:
        exit(0)

    m = max(n)
    n.remove(m)

    if n[0]**2 + n[1]**2 == m**2: print('right')
    else: print('wrong')