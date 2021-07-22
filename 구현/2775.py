k = 2
n = 3
a = []
new = []

for i in range(k):
    if i == 0:
        for k in range(n):
            a.append(k+1)
        continue
    for j in range(1, n+1):
        new.append(sum(a[0:j]))
    a = new
    new = []
    print(a)

print(sum(a))