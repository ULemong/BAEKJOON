s = [input() for _ in range(int(input()))]

s = list(set(s))
s.sort(key=lambda x: (len(x),x))

print('\n'.join(s))