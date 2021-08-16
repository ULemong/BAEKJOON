N, M = map(int, input().split())
data = list(map(int, input().split()))
sum_list = []

for i in range(N):
    for j in range(1, N):
        if j <= i:
            continue
        for k in range(2, N):
            if k <= j:
                continue
            if data[i] + data[j] + data[k] <= M:
                sum_list.append(data[i] + data[j] + data[k])

print(max(sum_list))
