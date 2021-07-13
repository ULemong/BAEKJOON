#풀이 1
s = input()
alpha = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
sum = 0

for i in s:
    for j in alpha:
        if i in j:
            sum += alpha.index(j) + 3
print(sum)


#풀이 2
s = input()
second = 0

for i in s:
    if ord(i) < ord('P'):
        a, s = 0, 3

        for j in range(2, 7):
            if ord('A') + a <= ord(i) <= ord('C') + a:
                second += s
                break
            else:
                a += 3
                s += 1
                continue
    else:
        if ord('P') <= ord(i) <= ord('S'): second += 8
        elif ord('T') <= ord(i) <= ord('V'): second += 9
        else: second += 10

print(second)