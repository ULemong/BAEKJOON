import math

for _ in range(int(input())):
    H, W, N = map(int, input().split())

    XX = math.ceil(N / H)
    YY = N - (H*(XX - 1))

    if XX > 9: print(str(YY) + str(XX))
    else: print(str(YY) + '0' + str(XX))