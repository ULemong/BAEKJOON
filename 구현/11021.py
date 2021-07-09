import sys

n = int(input())

for i in range(n):
    A, B = map(int, sys.stdin.readline().split())
    print('Case #%d: %d' % (i+1, A+B))