number = []
self_number = []

for i in range(1, 10001):
    sum = 0
    for j in str(i):
        sum += int(j)
    number.append(sum + i)

for i in range(1, 10001):
    if i not in number:
        self_number.append(i)

print('\n'.join(map(str, self_number)))