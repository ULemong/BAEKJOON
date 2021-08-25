h, m = map(int, input().split())
time = int(input())

sum = m + time

if sum >= 60:
    h += sum // 60
    m = sum % 60
else:
    m = sum

if h >= 24:
    h = h-24

print(h, m)