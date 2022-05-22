# Anagrams are the strings which are made up of the same set of letters.
s1 = input()
s2 = input()
l1 = []
l2 = []
for i in s1:
    if i.isalpha():
        l1.append(i.lower())
for i in s2:
    if i.isalpha():
        l2.append(i.lower())
l1.sort()
l2.sort()
if l1 == l2:
    print('Yes', end='')
else:
    print('No', end='')