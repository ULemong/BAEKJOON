for _ in range(int(input())):
    k = int(input())
    n = int(input())
    data = []

    for i in range(k):
        new = []
        if i == 0:
            for k in range(n):
                data.append(k+1)
            continue
        for j in range(1, n+1):
            new.append(sum(data[0:j]))
        data = new

    print(sum(data))
