def print_board(board):
    for i in range(3):
        print(f" {board[i * 3]} | {board[i * 3 + 1]} | {board[i * 3 + 2]} ")
        if i < 2:
            print("-----------")


def check_winner(board):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != " ":
            return board[i]

    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != " ":
            return board[i]

    # Check diagonals
    if board[0] == board[4] == board[8] != " ":
        return board[0]
    if board[2] == board[4] == board[6] != " ":
        return board[2]

    return None


def is_board_full(board):
    return " " not in board


def tic_tac_toe():
    board = [" "] * 9
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print("Positions are numbered from 1 to 9 as shown:")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    print("\nLet's begin!\n")

    while True:
        print_board(board)
        position = input(f"Player {current_player}, enter position (1-9): ")

        try:
            position = int(position) - 1  # Convert to 0-based index
            if position < 0 or position > 8:
                print("Please enter a number between 1 and 9.")
                continue

            if board[position] != " ":
                print("That position is already taken!")
                continue

            board[position] = current_player

            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break

            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break

            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("Please enter a valid number between 1 and 9.")


if __name__ == "__main__":
    tic_tac_toe()


