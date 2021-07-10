li = [(int(input())) % 42 for _ in range(10)]
li.sort()

count = 0

for i in range(9):
    if li[i] == li[i+1]: count += 1

print(int(len(li)) - count)