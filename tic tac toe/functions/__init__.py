def display_board(board):
    print('+-----------+')
    for k, v in board.items():
        if k in [1, 4, 7]:
            print('|', end='')
        print(f' {v} |', end='')
        if k in [3, 6, 9]:
            print()
    print('+-----------+')
    #  A função aceita um parâmetro contendo o status atual do tabuleiro
    #  e imprime no console.


def enter_move(board, move, mark):
    for k, v in board.items():
        if k is move and v == ' ':
            board.update({move: mark})
            return False
    return True
    # A função aceita o status atual do tabuleiro, pergunta ao usuário sobre sua movimentação,
    # verifica a entrada e atualiza o quadro de acordo com a decisão do usuário.


'''def make_list_of_free_fields(board):

     # A função navega no tabuleiro e constrói uma lista de todos os quadrados livres;
     # a lista consiste em tuplas, enquanto cada tupla é um par de números de linha e coluna.


def victory_for(board, sign):

     # A função analisa o estado da placa para verificar se
     # o jogador que usou 'O's ou 'X's ganhou o jogo


def draw_move(board):

     # A função desenha o movimento do computador e atualiza o tabuleiro.
'''