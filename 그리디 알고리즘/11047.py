n, k = map(int, input().split())
coin_list = []

for i in range(n):
    coin = int(input())
    coin_list.append(coin)

coin_list.reverse()
result = 0

for i in coin_list:
    result += k//i
    k %= i

print(result)