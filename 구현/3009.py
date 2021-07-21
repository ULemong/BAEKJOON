a, b, result = [], [], []

for _ in range(3):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)

for i in a:
    if a.count(i) == 1:
        result.append(i)

for i in b:
    if b.count(i) == 1:
        result.append(i)

print(' '.join(map(str,result)))