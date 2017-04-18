ans = list('EVAPORATE')
bracket = list('_'*len(ans))
print('Welcome to Hangman!')
print(' '.join(bracket) + '\n')
lst = list()
while True:
    guess = input('Guess your letter: ').upper()
    if guess not in lst: lst.append(guess)
    else: print('You have guessed it.')
    if guess not in ans:
        print('Incorrect!\n')
    else:
        position = [i for i, j in enumerate(ans) if j == guess]
        for k in position:
            bracket[k] = guess
        print(' '.join(bracket) + '\n')
        if '_' not in bracket:
            print('Congrats!\n')
            break
