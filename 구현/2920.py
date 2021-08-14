import sys
n = list(map(int, sys.stdin.readline().split()))

ascending, descending = True, True

for i in range(1, 8):
    if n[i-1] < n[i]:
        descending = False
    else:
        ascending = False

if ascending:
    print('ascending')
elif descending:
    print('descending')
else:
    print('mixed')