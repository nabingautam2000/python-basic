# A simple list to represent the 3x3 board
board = [" " for _ in range(9)]

def print_board():
    """Prints the tic-tac-toe board to the console."""
    row1 = f"| {board[0]} | {board[1]} | {board[2]} |"
    row2 = f"| {board[3]} | {board[4]} | {board[5]} |"
    row3 = f"| {board[6]} | {board[7]} | {board[8]} |"
    print("\n" + "+---+---+---+" + "\n" + row1 + "\n" + "+---+---+---+" + "\n" + row2 + "\n" + "+---+---+---+" + "\n" + row3 + "\n" + "+---+---+---+" + "\n")

def check_winner(player):
    """Checks if the given player has won."""
    # Check rows, columns, and diagonals
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_board_full():
    """Checks if the board is full (a tie)."""
    return " " not in board

def main_game():
    """The main function to run the game."""
    current_player = "X"
    game_over = False

    while not game_over:
        print_board()
        try:
            move = int(input(f"Player '{current_player}', enter your move (1-9): "))
            
            # Check if input is valid (1-9 and spot is empty)
            if move >= 1 and move <= 9 and board[move - 1] == " ":
                board[move - 1] = current_player
                
                # Check for winner
                if check_winner(current_player):
                    print_board()
                    print(f"🎉 Congratulations! Player '{current_player}' wins!")
                    game_over = True
                # Check for a tie
                elif is_board_full():
                    print_board()
                    print("🤝 It's a tie!")
                    game_over = True
                # Switch players
                else:
                    current_player = "O" if current_player == "X" else "X"
            else:
                print("⚠️ Invalid move. Please choose an empty spot from 1 to 9.")

        except ValueError:
            print("❌ Invalid input. Please enter a number between 1 and 9.")

# Start the game
if __name__ == "__main__":
    main_game()