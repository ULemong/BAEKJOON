n = int(input())
p = list(map(int, input().split()))
p.sort()
hap = 0
a = []
for i in range(n):
    hap = hap+p[i]
    a.append(hap)
result = sum(a)
print(result)
