from functions import *
from random import randint

j2 = j1 = True
victory = ''
tabuleiro = {1: ' ', 2: ' ', 3: ' ',
             4: ' ', 5: ' ', 6: ' ',
             7: ' ', 8: ' ', 9: ' '}
display_board(tabuleiro)
while True:
    while j1:
        j2 = True
        try:
            j = int(input('diga o numero da jogada:'))
        except ValueError:
            j = 0
        j1 = enter_move(tabuleiro, j, 'O')
    display_board(tabuleiro)
    victory = victory_for(tabuleiro, 'O')
    if victory != '':
        break
    while j2:
        j1 = True
        j = randint(1, 9)
        j2 = enter_move(tabuleiro, j, 'X')
    display_board(tabuleiro)
    victory = victory_for(tabuleiro, 'X')
    if victory != '':
        break
print(f'{victory} ganhou')
