k = int(input())
m = []
for i in range(k):
    a = list(map(int, input().split()))
    m.append(a)
for i in range(k):
    for j in range(k-i-1):
        m[i][k-j-1] = 0
for i in range(k):
    for j in range(k):
        print(m[i][j], end=' ')
    print()