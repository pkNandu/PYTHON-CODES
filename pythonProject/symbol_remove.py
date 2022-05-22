# input : "Wow!!! It's a beautiful morning"
# output : Wow Its a beautiful morning
s = input()
m = []
for i in s:
    if i.isalpha():
        m.append(i)
    elif i == ' ':
        m.append(i)
s = ''.join(m)
print(s)


