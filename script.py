
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


def computer_turn(b):
    print("Computer's turn")
    print_board(b)

    row, col = best_move(b)
    make_move(b, row, col, 'O')

def evaluate(b):
    if has_won(b, 'O'):
        return +1
    elif has_won(b, 'X'):
        return -1
    else:
        return 0

def simulate(b, depth, is_maximizing):
    score = evaluate(b)

    if score == 1 or score == -1 or not get_empty_cells(b):
        return score

    if is_maximizing:
        best_score = -float('inf')
        for (i, j) in get_empty_cells(b):
            b[i][j] = 'O'
            value = simulate(b, depth + 1, False)
            b[i][j] = ' '
            best_score = max(best_score, value)
        return best_score
    else:
        best_score = float('inf')
        for (i, j) in get_empty_cells(b):
            b[i][j] = 'X'
            value = simulate(b, depth + 1, True)
            b[i][j] = ' '
            best_score = min(best_score, value)
        return best_score

def best_move(b):
    best_score = -float('inf')
    move = None
    for (i, j) in get_empty_cells(b):
        b[i][j] = 'O'
        score = simulate(b, 0, False)
        b[i][j] = ' '
        if score > best_score:
            best_score = score
            move = (i, j)
    return move

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
        computer_turn(board)
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
print_board(board)