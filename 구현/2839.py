n = int(input())
bag = 0

while True:
    if n < 0:
        bag = -1
        break
    if n%5 == 0:
        bag += n//5
        break
    n -= 3
    bag += 1

print(bag)