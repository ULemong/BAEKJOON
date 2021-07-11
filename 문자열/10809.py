s = input()
alpha = ord('a')

for i in range(0, 26):
    if chr(alpha+i) in s:
        print(s.index(chr(alpha+i)), end=' ')
    else:
        print(-1, end=' ')