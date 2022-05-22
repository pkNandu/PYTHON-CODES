l = int(input())
m = []
for i in range(l):
    s = list(map(int, input().split()))
    m.append(s)
f = 0
for i in range(l):
    for j in range(l):
        if m[i][j] != m[j][i]:
            f = 1
            break
if(f):
    print('No', end='')
else:
    print('Yes',end='')