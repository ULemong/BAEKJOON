n = int(input())
a, i = 1, 1
count = 2

while True:
    if n == 1:
        print(count-1)
        break
    elif a + 1 <= n <= a + (6 * i):
        print(count)
        break
    else:
        a = a + (6 * i)
        i += 1
        count += 1