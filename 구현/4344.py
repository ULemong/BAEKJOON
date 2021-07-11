C = int(input())

for i in range(C):
    count = 0
    grade = list(map(int, input().split()))

    n = grade[0]
    del(grade[0])
    avg = sum(grade) / n

    for j in grade:
        if j > avg:
            count += 1

    print('%.3f%%' % (count/n*100))