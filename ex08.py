
player1 = input('Player 1, select Rock, Paper, or Scissors: ')
player2 = input('Player 2, select Rock, Paper, or Scissors: ')


def RockPaperScissors():
    if player1.upper() == player2.upper():
        print('Draw Game')
    elif player1.upper() == 'ROCK' and player2.upper() == 'SCISSORS':
        print('Player 1 wins')
    elif player1.upper() == 'PAPER' and player2.upper() == 'ROCK':
        print('Player 1 wins')
    elif player1.upper() == 'SCISSORS' and player2.upper() == 'PAPER':
        print('Player 1 wins')
    else:
        print('Player 2 wins')

    replay = input('Would you like to play again (Y/N)? ')

    if replay.upper() == 'Y':
        RockPaperScissors()
    else:
        print('Thank you for playing')

RockPaperScissors()