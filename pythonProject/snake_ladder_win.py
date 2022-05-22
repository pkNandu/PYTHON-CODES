# this is a winning combination if the set of die rolls lead to a number equal to 100 or exceeds 100)
# First line of the input contains the board configuration in the form of mapping of snakes and ladders
# Second line of the input contains comma separated integers indicating the values obtained on rolling a die.
# input :
#6:14, 11:28, 17:74, 22:7, 38:59, 49:12, 57:76, 61:54, 81:98, 88:4
# 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6
s = input().split(',')
l = list(map(int, input().split(',')))
D = {}
count = 0
for i in s:
    t = i.split(':')
    D[int(t[0])] = int(t[1])
for val in l:
    count += val
    if count in D:
        count = D[count]
if count >= 0:
    print('Yes', end='')
else:
    print('No', end='')

