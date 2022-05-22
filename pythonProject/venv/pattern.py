def printn(i):
    for k in range(i) :
        print(i, end = "")
def pattern(n, i) :
    if n == 0 :
        return
    printn(i)
    return pattern(n-1, i+1)
print(pattern(5,1))