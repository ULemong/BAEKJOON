T = int(input())

coin_list = [25, 10, 5, 1]
c = []

for i in range(T):
    c.append(int(input()))

for i in range(T):
    C = c[i]
    for coin in coin_list:
        result = C // coin
        C %= coin
        print(result, end=" ")
    print()