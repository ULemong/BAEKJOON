data_list = []

for _ in range(int(input())):
    data = input().split()
    data_list.append((int(data[0]), data[1]))

data_list.sort(key=lambda x: x[0])

for i in data_list:
    print(i[0], i[1])