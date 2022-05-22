#number palindrome or not
def palindrome(x):
    x=str(x)
    y=x[::-1]
    if(x==y):
        print("Palindrome")
    else:
        print("Not a Palindrome")
x=int(input())
palindrome(x)