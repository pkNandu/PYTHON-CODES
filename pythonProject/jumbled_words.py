from numpy import random

def choose():
    words = ["hello", "computer", "condition", "science", "dragon"]
    pick = random.choice(words)
    return pick


def jumble(word):
    jumble = "".join(random.sample(word, len(word)))
    return jumble


def thank(p1n, p2n, p1, p2):
    print(p1n, " Your score is : ", p1)
    print(p2n, " Your score is : ", p2)
    print("Thanks for playing")


def play():
    p1name = input("Enter player 1 name : ")
    p2name = input("Enter player 2 name : ")
    pt1 = 0
    pt2 = 0
    turn = 0
    while 1:
        picked_word = choose()
        qn = jumble(picked_word)
        print(qn)
        # player1
        if turn % 2 == 0:
            print(p1name, ' Your turn')
            ans = input("What is on your mind : ")
            if ans == picked_word:
                pt1 += 1
                print("Your Score is : ", pt1)
            else:
                print('Better luck next time, I thought the word ', picked_word)
            c = input("Press 1 to continue and 0 to quit : ")
            if c == 0:
                thank(p1name, p2name, pt1, pt2)
                break
        # player1
        else:
            print(p1name, ' Your turn')
            ans = input("What is on your mind : ")
            if ans == picked_word:
                pt2 += 1
                print("Your Score is : ", pt2)
            else:
                print('Better luck next time, I thought the word ', picked_word)
            c = input("Press 1 to continue and 0 to quit : ")
            if c == 0:
                thank(p1name, p2name, pt1, pt2)
                break
play()

