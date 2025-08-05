
def print_board(board):
    print("  0 1 2")
    for i, row in enumerate(board):
        print(f"{i} " + " ".join(row))

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def make_move(board, row, col, player):
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    return False

def reset_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

