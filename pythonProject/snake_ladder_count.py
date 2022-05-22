# In the given configuration, 6:14 indicates a ladder and 22:7 indicates a snake
# input : 6:14, 11:28, 17:74, 22:7, 38:59, 49:12, 57:76, 61:54, 81:98, 88:4
# There are 4 snakes and 6 ladders.
s = input().split(',')
count_s = 0
count_b = 0
for i in s:
    a, b = i.split(':')
    if int(a) > int(b):
        count_s += 1
    else:
        count_b += 1
print(count_s, ' ', count_b)
