#Given a list of binary numbers (0s and 1s), determine the number of possible arrangements of distinct binary sequences using given 0s and 1s.
def factorial(n):
    fact = 1
    if(n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)
l = [int(x) for x in input().split(' ')]
zeros_count = l.count(0)
ones_count = l.count(1)
num_arrangements = factorial(len(l)) // (factorial(zeros_count) * factorial(ones_count))
print(num_arrangements, end='')