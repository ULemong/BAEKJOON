T = input()
time = [300, 60, 10] #A ,B, C
a = []

if T[-1] != '0':
    print(-1)
else:
    T = int(T)

    for i in time:
        if i > T:
            a.append(0)
            continue
        else:
            result = T // i
            T = T % i
            a.append(result)

    print(" ".join(map(str, a)))