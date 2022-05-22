import string
import random
symbols = []
symbols = list(string.ascii_letters)
card1 = [0] * 5
card2 = [0] * 5
pos1 = random.randint(0, 5)
pos2 = random.randint(0, 5)
sameSymbol = random.choice(symbols)
symbols.remove(sameSymbol)
if pos1 == pos2:
    card2[pos1] = sameSymbol
    card1[pos1] = sameSymbol
else:
    card1[pos1] == sameSymbol
    card2[pos2] == sameSymbol
    card1[pos2] = random.choice(symbols)
    symbols.remove(card1[pos2])
    card2[pos1] = random.choice(symbols)
    symbols.remove(card2[pos1])
i=0
while i<5 :
    if i != pos1 and i != pos2:
        card1[i] = random.choice(symbols)
        symbols.remove(card1[i])
        card2[i] = random.choice(symbols)
        symbols.remove(card2[i])
    i += 1
print(card1,'\n',card2)