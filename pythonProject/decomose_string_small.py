s = input()
l = input()
m = []
for i in l:
    if i.isalpha():
        m.append(i.lower())
l = ''.join(m)
if(set(s) == set(l) and len(s) == len(l)):
    print('Yes', end='')
else:
    print('No',end='')