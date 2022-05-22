import random
movies = ['anadam', 'drishyam', 'vikram vedha', 'chanakya', 'race', 'chess', 'hero panti', 'rakshaan']
def play() :
    p1name = input("input player 1 name")
    p2name = input("input player 1 name")
    pp1 = 0
    pp2 = 0
    turn = 0
    willing = True
    while willing :
        if turn % 2 == 0 :
            print(p1name, 'its your turn')
            picked_movie = random.choice(movies)
            qn = create_question(picked)
            print qn
            not_said = True
            while not_said:
                letter = input("Your letter")
                if is_present(letter, picked_movie) :
                    modified_qn = unlock(modified_qn, picked_movie_ch)
                    print(modified_qn)
                    d = input("press 1 to guess or 2 to unlock another character : ")
                    if d == 1 :
                        ans = input('Your answer : ')
                        if ans == picked_movie :
                            pp1 += 1
                            print('correct')
                            not_said = False
                            print(p1name, 'your score : ', pp1)
                        else :
                            print('worng answer. try again !')
                else :
                    print(letter, 'not found')
            c = input('press 1 to continue or 0 to quit')
        else :
            turn += 1
play()
