data_list = []

for _ in range(int(input())):
    x, y = map(int, input().split())
    data_list.append((x, y))

data_list = sorted(data_list)

for i in data_list:
    print(i[0], i[1])