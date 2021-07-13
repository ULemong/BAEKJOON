n = int(input())

if n < 100:
    print(n)
else:
    count = 0
    for i in range(100, n+1):
        new_i = str(i)
        if (int(new_i[0]) - int(new_i[1])) == (int(new_i[1]) - int(new_i[2])):
            count += 1
    print(count + 99)