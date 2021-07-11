n = int(input())

count = 0
c = []

for i in range(n):
    result = input()
    a = result.split('X')
    new = ' '.join(a).split()

    for j in new:
        for k in range(len(j)):
            count += 1
            c.append(count)
        count = 0

    print(sum(c))
    c = []