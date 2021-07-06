n = int(input())

rope_list = []
result = []
for _ in range(n):
    rope = int(input())
    rope_list.append(rope)

rope_list.sort(reverse = True)

for i in range(n):
    a = rope_list[i] * (i+1)
    result.append(a)

print(max(result))