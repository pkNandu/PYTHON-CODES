s = input()
l = []
for i in s:
    if i.isalpha():
        l.append(i.lower())
s = ''.join(l)
if s == s[::-1]:
    print("Yes", end='')
else:
    print('No', end='')
