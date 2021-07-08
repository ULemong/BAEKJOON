n = int(input())
hap = []
for i in range(n):
    A, B = map(int, input().split())
    hap.append(A + B)
for i in hap:
    print(i)
