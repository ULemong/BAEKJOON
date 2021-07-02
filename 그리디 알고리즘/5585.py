n = 1000-int(input())
coin_list = [500, 100, 50, 10, 5, 1]
a = 0

for coin in coin_list:
    a = a + n//coin
    n = n%coin
print(a)
