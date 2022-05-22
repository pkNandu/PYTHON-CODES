# A Zero-One or a Binary matrix is a matrix in which all the elements are either 0 or 1.
r, c = map(int, input().split())
flag = 0
val = [0, 1]
m = []
for i in range(r):
    a  = list(map(int, input().split()))
    for item in a:
        if item not in val:
            flag = 1
    m.append(a)
if flag == 1:
    print('No', end='')
else:
    print('Yes', end='')