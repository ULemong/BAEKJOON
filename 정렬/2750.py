li = []

for i in range(int(input())):
    li.append(int(input()))

li.sort()
print('\n'.join(map(str, li)))