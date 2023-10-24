import random

# Initializing Tic-Tac-Toe board
board = [' ' for _ in range(9)]

# Defining win combo
winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]


# Function to print board
def print_board(board):
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i + 1]} | {board[i + 2]}")
        if i < 6:
            print("-" * 9)


# Check if player won
def check_win(board, player):
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False


# Check if board is full (a tie)
def is_full(board):
    return ' ' not in board


# Function to make a move1
def make_move(board, position, player):
    if board[position] == ' ':
        board[position] = player


# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_win(board, 'O'):
        return -1
    if check_win(board, 'X'):
        return 1
    if is_full(board):
        return 0

    if is_maximizing:
        max_eval = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval


# AI player's move using Minimax with Alpha-Beta Pruning
def ai_move(board):
    best_move = -1
    best_eval = -float('inf')
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            eval = minimax(board, 0, False, -float('inf'), float('inf'))
            board[i] = ' '
            if eval > best_eval:
                best_eval = eval
                best_move = i
    return best_move


# Main game loop
while True:
    print_board(board)

    # Human player's move
    try:
        human_move = int(input("Enter your move (0-8): "))
        if board[human_move] != ' ':
            print("Invalid move. Try again.")
            continue
        make_move(board, human_move, 'O')
        if check_win(board, 'O'):
            print_board(board)
            print("You win!")
            break
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break
    except (ValueError, IndexError):
        print("Invalid input. Please enter a number between 0 and 8.")

    # AI player's move
    ai_best_move = ai_move(board)
    make_move(board, ai_best_move, 'X')
    if check_win(board, 'X'):
        print_board(board)
        print("AI wins!")
        break
    if is_full(board):
        print_board(board)
        print("It's a tie!")
        break
