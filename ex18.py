# cows and bulls

def cows_n_bulls():
    import random

    print('Welcome to the game of Cows and Bulls')
    solution = str(random.randint(0, 9999)).zfill(4)
    guess_num = 0
    cows = 0

    while cows != 4:
        guess = input('Guess a 4 digit number between 0000 and 9999: ')
        cows = 0
        bulls = 0
        guess_num += 1
        while len(guess) != 4 or type(int(guess)) != int:
            guess = input('Error: Guess a 4 digit number between 0000 and 9999: ')

        for index in range(len(guess)):
            if guess[index] == solution[index]:
                cows += 1
            elif guess[index] in solution:
                bulls += 1

        print('Cows: {}\nBulls: {}\nGuesses: {}'.format(cows, bulls, guess_num))
    return

cows_n_bulls()



# solution = str(random.randint(0,9999)).zfill(4)
