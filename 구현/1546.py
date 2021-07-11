n = int(input())
grade = list(map(int, input().split()))
M = max(grade)

new = []

for i in grade:
    new.append(i / M * 100)

print(sum(new) / n)