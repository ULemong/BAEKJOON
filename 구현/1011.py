for _ in range(int(input())):
    x, y = map(int, input().split())
    distance = y - x
    count = 0
    move = 1
    sum = 0

    while sum < distance:
        count += 1
        sum += move
        if count % 2 == 0:
            move += 1

    print(count)