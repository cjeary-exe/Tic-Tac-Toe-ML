
def print_board(b):
    print("  1 2 3")
    for i, row in enumerate(b):
        print(f"{i + 1} " + " ".join(row))

def get_empty_cells(b):
    return [(i, j) for i in range(3) for j in range(3) if b[i][j] == ' ']

def make_move(b, row, col, player):
    if b[row][col] == ' ':
        b[row][col] = player
        return True
    return False

def reset_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def can_player_win(b, player):
    for row in b:
        if row.count(player) == 2 and row.count(' ') == 1:
            return True

    for col in range(3):
        col_vals = [b[row][col] for row in range(3)]
        if col_vals.count(player) == 2 and col_vals.count(' ') == 1:
            return True

    diag1 = [b[i][i] for i in range(3)]
    if diag1.count(player) == 2 and diag1.count(' ') == 1:
        return True

    diag2 = [b[i][2 - i] for i in range(3)]
    if diag2.count(player) == 2 and diag2.count(' ') == 1:
        return True

    return False

def has_won(b, player):
    for row in b:
        if row.count(player) == 3:
            return True

    for col in range(3):
        col_vals = [b[row][col] for row in range(3)]
        if col_vals.count(player) == 3:
            return True

    diag1 = [b[i][i] for i in range(3)]
    if diag1.count(player) == 3:
        return True

    diag2 = [b[i][2 - i] for i in range(3)]
    if diag2.count(player) == 3:
        return True

    return False

def find_winning_move(b, player):
    for i, row in enumerate(b):
        if row.count(player) == 2 and row.count(' ') == 1:
            return i, row.index(' ')

    for col in range(3):
        col_vals = [b[row][col] for row in range(3)]
        if col_vals.count(player) == 2 and col_vals.count(' ') == 1:
            return col_vals.index(' '), col

    diag1 = [b[i][i] for i in range(3)]
    if diag1.count(player) == 2 and diag1.count(' ') == 1:
        idx = diag1.index(' ')
        return idx, idx

    diag2 = [b[i][2 - i] for i in range(3)]
    if diag2.count(player) == 2 and diag2.count(' ') == 1:
        idx = diag2.index(' ')
        return idx, 2 - idx

    return None

def player_turn():
    while True:
        print_board(board)
        print("Your turn\n")
        try:
            playerInput1 = int(input("What row? "))
            playerInput2 = int(input("What column? "))
        except ValueError:
            print("Invalid input. Enter numbers 1–3.")
            continue

        if not (1 <= playerInput1 <= 3 and 1 <= playerInput2 <= 3):
            print("Input out of bounds")
            continue

        p1 = playerInput1 - 1
        p2 = playerInput2 - 1

        if make_move(board, p1, p2, 'X'):
            break
        else:
            print("Cell already taken. Try again.")


def computer_turn():
    print("Computer's turn")

    print_board(board)

    if can_player_win(board, 'O'):
        winningMove = find_winning_move(board, 'O')
        if winningMove is not None:
            make_move(board, winningMove[0], winningMove[1], 'O')
    elif can_player_win(board, 'O'):
        winningMove = find_winning_move(board, 'X')
        if winningMove is not None:
            make_move(board, winningMove[0], winningMove[1], 'O')
    else:
        if board[1][1] == ' ':
            make_move(board, 1, 1, 'O')
        elif board[0][0] == ' ':
            make_move(board, 0, 0, 'O')
        elif board[0][2] == ' ':
            make_move(board, 0, 2, 'O')
        elif board[2][0] == ' ':
            make_move(board, 2, 0, 'O')
        elif board[2][2] == ' ':
            make_move(board, 2, 2, 'O')



gameOver = False
board = reset_board()
turn = 0 #Starts with player
winner = None

print_board(board)

while not gameOver:
    if turn == 0:
        player_turn()
        turn = 1
    else:
        computer_turn()
        turn = 0

    if has_won(board, 'X'):
        gameOver = True
        winner = "Player Wins!"
    elif has_won(board, 'O'):
        gameOver = True
        winner = "Computer Wins!"
    elif not get_empty_cells(board):
        gameOver = True
        winner = "Draw"


print(winner)