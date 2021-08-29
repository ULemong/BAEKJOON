import sys
n = int(input())
data = list(map(int, sys.stdin.readline().split()))

data2 = list(sorted(set(data)))
dic = {value: index for index, value in enumerate(data2)}

for i in data:
    print(dic[i], end= " ")