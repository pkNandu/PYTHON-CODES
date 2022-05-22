l = [int(x) for x in input().split(' ')]
k = int(input())
s = set(l)
for i in s:
    if (l.count(i) == k):
        print(k, end="")
        break