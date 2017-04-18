def who(token):
    if token == 'x':
        return('Player1')
    elif token == 'o':
        return('Player2')

def win(board):
    # Line
    for i in range(3):
        row = set([board[i][0], board[i][1], board[i][2]])
        column = set([board[0][i], board[1][i], board[2][i]])
        if len(row) == 1 and board[i][0] != ' ':
            return('The winner is %s!' %(who(board[i][0])))
        elif len(column) == 1 and board[0][i] != ' ':
            return('The winner is %s!' %(who(board[0][i])))

    # Diagonal
    if board[0][0] == board[1][1] == board[2][2] and board[1][1] != ' ':
        return('The winner is %s!' %(who(board[1][1])))
    elif board[0][2] == board[1][1] == board[2][0] and board[1][1] != ' ':
        return('The winner is %s!' %(who(board[1][1])))

    else:
        return(0)

def play(player, token):
    player = input('%s where does your token go? [Row Column] ' %(player))
    while True:
        place = [i-1 for i in list(map(int, player.split()))]
        if board[place[0]][place[1]] == ' ':
            board[place[0]][place[1]] = token
            for element in board:
                print(element)
            break
        else:
            print("This space is occupied. Please chose another one.")
            player = input('Where again? ')

board = [[' ', ' ', ' '] for i in range(3)]
player1 = 'Player1'
player2 = 'Player2'
token1 = 'x'
token2 = 'o'
while True:
    play(player1, token1)
    win(board)
    if win(board) != 0:
        print(win(board))
        break
    play(player2, token2)
    win(board)
    if win(board) != 0:
        print(win(board))
        break
