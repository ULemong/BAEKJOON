n = int(input())
new_s = ''
count = 0

for i in range(n):
    s = input()

    for j in range(len(s)-1):
        if s[j] != s[j+1]:
            new_s += s[j]
    new_s += s[-1]

    for k in new_s:
        if new_s.count(k) > 1:
            break
        if k == new_s[-1]:
            count += 1
    new_s = ''

print(count)