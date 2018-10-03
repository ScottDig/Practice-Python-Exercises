
def GuessingGame():
    '''
    Guess a random number between 1 and 9 
    '''
    import random 

    NumGen = random.randint(1,9)
    NumGuess = int(input('Guess a number between 1 and 9: '))

    correct = 0
    wrong = 0

    ExitGame = 'no'

    while ExitGame.upper() != 'EXIT':
        if NumGuess == NumGen:
            print('You are correct!')
            correct += 1
        elif NumGuess < NumGen:
            print('You guessed too low')
            wrong += 1
        else:
            print('You guessed too high')
            wrong += 1
        ExitGame = input("Type EXIT to end the game: ")

    print('You guessed {} correctly out of {} total tries.'.format(correct, wrong))


GuessingGame()
