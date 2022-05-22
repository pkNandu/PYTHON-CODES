#to reverse a given integer
def reverse(x):
    if x>=0:
        x=str(x)
        x=x[::-1]
        x=int(x)
        return x
    else:
        x=x*-1
        x=str(x)
        x=x[::-1]
        x=int(x)
        x=x*-1
        return x
x=int(input())
print(reverse(x))