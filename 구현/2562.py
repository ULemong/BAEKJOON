li = []

for _ in range(9):
    li.append(int(input()))

print(max(li))
print(int(li.index(max(li)))+1)