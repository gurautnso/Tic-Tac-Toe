from functions import *
from random import randint
from time import sleep

victory = j2 = j1 = True
tabuleiro = {1: ' ', 2: ' ', 3: ' ',
             4: ' ', 5: ' ', 6: ' ',
             7: ' ', 8: ' ', 9: ' '}
display_board(tabuleiro)
while victory:
    while j1:
        j2 = True
        j = int(input('diga o numero da jogada:'))
        j1 = enter_move(tabuleiro, j, 'O')
        display_board(tabuleiro)
    while j2:
        j1 = True
        j = randint(1, 9)
        j2 = enter_move(tabuleiro, j, 'X')
        display_board(tabuleiro)
        sleep(5)
