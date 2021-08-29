def gcd(a, b):
    return gcd(b, a % b) if b else a
def lcm(a, b):
    return a * b // gcd(a, b)

for i in range(int(input())):
    a, b = map(int, input().split())
    print(lcm(a, b))