def who(token):
    if token == 'x':
        return('Player1')
    elif token == 'o':
        return('Player2')

def gameboard():
    board = [[' ---', ' ---', ' ---'],
             ['|   ', '|   ', '|   ', '|   '],
             [' ---', ' ---', ' ---'],
             ['|   ', '|   ', '|   ', '|   '],
             [' ---', ' ---', ' ---'],
             ['|   ', '|   ', '|   ', '|   '],
             [' ---', ' ---', ' ---']]
    return(board)

def print_gameboard(board):
    for line in board:
        print(''.join(line))

def play(board, player, token):
    player = input('%s [row col]: ' %(player))
    while True:
        row = int(player.split()[0])
        col = int(player.split()[1]) - 1
        trans_row = {1:1, 2:3, 3:5}
        if row in range(1, 4) and col in range(0, 3):
            if board[trans_row[row]][col] == '|   ':
                board[trans_row[row]][col] = '| %s ' %(token)
                print_gameboard(board)
                break
            else:
                print('This space is occupied.')
                player = input('Where again? ')
        else:
            print('Wrong input.')
            player = input('Where again? ')

def win(board):
    for i in range(1, 6, 2): # Row
        row = set([board[i][0], board[i][1], board[i][2]])
        if len(row) == 1 and board[i][0] != '|   ':
            return('The winner is %s!' %(who(board[i][0][2])))

    for j in range(3): # Column
        column = set([board[1][j], board[3][j], board[5][j]])
        if len(column) == 1 and board[1][j] != '|   ':
            return('The winner is %s!' %(who(board[1][j][2])))

    # Diagonal
    if board[1][0] == board[3][1] == board[5][2] and board[3][1] != '|   ':
        return('The winner is %s!' %(who(board[3][1][2])))
    elif board[1][2] == board[3][1] == board[5][0] and board[3][1] != '|   ':
        return('The winner is %s!' %(who(board[3][1][2])))

    else:
        return(0)



board = gameboard()
player1, token1 = 'Player1', 'x'
player2, token2 = 'Player2', 'o'

finish = False
while not finish:
    play(board, player1, token1)
    if win(board) == 0:
        play(board, player2, token2)
        finish = False
    else:
        print(win(board))
        finish = True
