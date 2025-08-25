import math

# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check if someone has won
def check_winner(board):
    # Check rows & columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    
    return None

# Function to check if moves left
def is_moves_left(board):
    for row in board:
        if " " in row:
            return True
    return False

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "X":
        return 1
    if winner == "O":
        return -1
    if not is_moves_left(board):
        return 0
    
    if is_maximizing:  # Maximizer = X
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = " "
        return best
    else:  # Minimizer = O
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = " "
        return best

# Find the best move for X
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                move_val = minimax(board, 0, False)
                board[i][j] = " "
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    
    return best_move

# --- Main Game Loop ---
if __name__ == "__main__":
    board = [[" " for _ in range(3)] for _ in range(3)]

    print("Tic Tac Toe - You (O) vs AI (X)")
    print_board(board)

    while True:
        # Human move
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))
        if board[row][col] != " ":
            print("Invalid move! Try again.")
            continue
        board[row][col] = "O"

        if check_winner(board) == "O":
            print_board(board)
            print("You win! 🎉")
            break
        if not is_moves_left(board):
            print_board(board)
            print("It's a draw! 🤝")
            break

        # AI move
        print("AI is making a move...")
        move = find_best_move(board)
        board[move[0]][move[1]] = "X"

        print_board(board)

        if check_winner(board) == "X":
            print("AI wins! 🤖")
            break
        if not is_moves_left(board):
            print("It's a draw! 🤝")
            break
