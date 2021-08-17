for _ in range(int(input())):
    data = []
    count = 0
    N, M = map(int, input().split())
    importent = list(map(int, input().split()))
    while count <= len(importent):
        count += 1

        if importent[M] == N:
            break
        N -= 1



        if importent[M] == max(importent):
            count += 1
            break
        else:


