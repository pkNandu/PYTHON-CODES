# The alphabets are enumerated as A = 0, B = 1, C = 2, … , Z = 25. Consider an encryption
#
# scheme where a character with value C i in the plaintext is replaced by another character
#
# with value C j using the formula C j = (C i + 5) % 26. After replacement, the resulting string is
#
# shuffled (permuted) at random to obtain the cipher text.
#
# Given a plain text and a possible cipher text, your task is to determine whether the cipher
#
# text can be formed from the plain text using the above mentioned scheme.
a = input()
b = input()
u = ''
for i in a:
    u += chr((ord(i) - ord('A') + 5)%26 + ord('A'))
if sorted(b) == sorted(u):
    print('yes')
else:
    print('no')