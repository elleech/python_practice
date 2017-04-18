def pic_hangman(bkt, msg, wrong):
    head = rhand = lhand = body = rleg = lleg = ' '
    if msg == 'Good luck.':
        pic = '''
        _____
        |    |    Welcome to Hangman
        |    %s
        |   %s%s%s   %s
        |    %s
        |   %s %s   %s
        |
        -----
        ''' %(head, rhand, body, lhand, bkt, body, rleg, lleg, msg)
    elif wrong > -1:
        if wrong == 1:
            head = 'O'
        elif wrong == 2:
            head = 'O'; body = '|'
        elif wrong == 3:
            head = 'O'; body = '|'; rhand = '/'
        elif wrong == 4:
            head = 'O'; body = '|'; rhand = '/'; lhand = '\\'
        elif wrong == 5:
            head = 'O'; body = '|'; rhand = '/'; lhand = '\\'; rleg = '/'
        elif wrong == 6:
            head = 'O'; body = '|'; rhand = '/'; lhand = '\\'; rleg = '/'; lleg = '\\'
        pic = '''
        _____
        |    |    Welcome to Hangman
        |    %s
        |   %s%s%s   %s
        |    %s
        |   %s %s   %s
        |
        -----
        ''' %(head, rhand, body, lhand, bkt, body, rleg, lleg, msg)
    return(pic)

def pick_word():
    import random
    file = 'sowpods.txt'
    with open(file, 'r') as f: words = list(f)
    return(random.choice(words).strip())

def play_hangman(word):
    word = list(pick_word())
    guessed = list()
    bracket = list('_'*len(word))
    bkt = ' '.join(bracket)
    wrong = 0
    print(pic_hangman(str(len(word)) + ' words.', 'Good luck.', wrong))
    while wrong <= 6:
        ans = input('Guess a letter: ').upper()
        if ans not in guessed:
            guessed.append(ans)
            if ans in word:
                position = [i for i , j in enumerate(word) if j == ans]
                for k in position:
                    bracket[k] = ans
                    bkt = ' '.join(bracket)
                if '_' not in bracket:
                    print(pic_hangman(bkt, 'Congrats!', wrong))
                    break
                else:
                    print(pic_hangman(bkt, 'Nice!', wrong))
            else:
                wrong += 1
                if wrong == 6:
                    print(pic_hangman(bkt, 'Game over! Answer: %s' %(''.join(word)), wrong))
                    break
                print(pic_hangman(bkt, 'Incorrect!', wrong))
        else:
            wrong += 1
            if wrong == 6:
                print(pic_hangman(bkt, 'Game over! Answer: %s' %(''.join(word)), wrong))
                break
            else:
                print(pic_hangman(bkt, 'Already guessed.', wrong))

while True:
    play_hangman(pick_word())
    again = input('Play again? Y/N ').upper()
    if again == 'Y': True
    else: break
