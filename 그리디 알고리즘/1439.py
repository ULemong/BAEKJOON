s = input()
new_s = []

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        new_s.append(s[i])
new_s.append(s[-1])

zero = new_s.count('0')
one = new_s.count('1')

if zero < one:
    print(zero)
else:
    print(one)