s = input()
Croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in Croatian:
    if i in s:
        s = s.replace(i,' ')

print(len(s))