'''
print("Rock")
print("Paper")
print("Scissors")

player1 = input("Player 1. Make Your Move ")
player2 = input("Player 2. Make Your Move ")

if player1 == 'Rock' and player2 == 'Paper':
    print("Player 1 wins")

elif player1 == 'Rock' and player2 == 'Scissors':
    print("Player 2 wins")

elif player1 == 'Scissors' and player2 == 'Paper':
    print("Player 2 wins")

elif player1 == 'Paper' and player2 == 'Rock':
    print("Player 1 wins")

elif player1 == 'Rock' and player2 == 'Scissors':
    print("Player 2 wins")

else:
    print("something went wrong")
'''

import datetime
x = datetime.datetime.now()
print(x)