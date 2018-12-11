import random

from random import randint

resume = None

while resume != 'n':

    # Get human player moves
    print("Let's play rock paper scissors!  So.... Rock, Paper, or Scissors?\n")

    humanPlay = input()
    humanPlay = humanPlay.lower()
    
    computerPlay = random.randint(1,3)

    # Computer player move conversion from int to str
    if computerPlay == 1:
        computerPlay = 'rock'
    if computerPlay == 2:
        computerPlay = 'paper'
    if computerPlay == 3:
        computerPlay = 'scissors'

    # Determine who wins
    
    if humanPlay == computerPlay:
        print("\nIt's a tie!\n ")
        resume = input('Do you want to play again? (y/n) ' )

    # Human enters something other than rock, paper, or scissors.
    elif humanPlay != 'rock' or 'paper' or 'scissors':
        print('\nSomething went wrong......please choose rock, paper, or scissors')
        print("Let's try again\n")
        continue
        
    # Continue statement skips any more steps inside this loop
        
    elif humanPlay == 'rock':
        
        if computerPlay == 'paper':
            print('\nYou lose!\n')
        elif computerPlay == 'scissors':
            print('\nYou win!\n')

    elif humanPlay == 'paper':
        
        if computerPlay == 'scissors':
            print('\n You lose!\n')
        elif computerPlay == 'rock':
            print('\n You win!\n')

    elif humanPlay == 'scissors':
        
        if computerPlay == 'rock':
            print('\nYou lose!\n')
        elif computerPlay == 'paper':
            print('\nYou win!\n')

    # Restart the loop
    resume = input('Do you want to play again? (y/n) ' )

