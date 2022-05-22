# Input:
#
# 5
# Output:
#
# 1
# 121
# 12321
# 1234321
# 123454321
k = int(input())
for i in range(1,k+1):
    for j in range(1,i):
        print(j, end=" ")
    print(i, end=" ")
    for j in range(1,i):
        print(i-j, end=" ")
    print()