A, B = input().split()
result = str(max(int(A[::-1]), int(B[::-1])))
print(result)