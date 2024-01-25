def display_board(board):
    print('+-----------+')
    for k, v in board.items():
        if k in [1, 4, 7]:
            print('|', end='')
        print(f' {v} |', end='')
        if k in [3, 6, 9]:
            print()
    print('+-----------+')


def enter_move(board, move, mark):
    for k, v in board.items():
        if k is move and v == ' ':
            board.update({move: mark})
            return False
    return True


def victory_for(board, player):
    vitorias = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    mark = player
    jogadas = []
    for k, v in board.items():
        if v == mark:
            jogadas.append(k)
    jogadas.sort()
    print(jogadas)
    consec = 0
    for c in vitorias:
        for i in c:
            for v in jogadas:
                if v == i:
                    consec += 1
                if consec >= 3:
                    return player
        consec = 0
    else:
        return ''
