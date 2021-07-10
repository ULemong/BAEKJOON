n = input()
a = n
count = 0

while True:
    if int(n) < 10: hap = str(n)
    else: hap = str(int(n[0]) + int(n[1]))

    if n[-1] == '0': n = hap[-1]
    else: n = n[-1] + hap[-1]

    count += 1

    if n == a: break

print(count)