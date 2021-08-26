for _ in range(int(input())):
    N, M = map(int, input().split())
    data = map(int, input().split())

    data = [(value, index) for index, value in enumerate(data)]
    count = 0

    while True:
        if data[0][0] == max(data, key=lambda x: x[0])[0]:
            count += 1
            if M == data[0][1]:
                break
            else:
                data.pop(0)
        else:
            data.append(data.pop(0))

    print(count)