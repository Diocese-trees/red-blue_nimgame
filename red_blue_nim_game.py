import argparse
import math

# Welcome message
def welcome_message():
    print("Welcome to the Red-Blue Nim Game!")
    print("Get ready for a thrilling game of strategy!\n")

# Function to check if the game is over
def check_game_over(red, blue):
    return red == 0 and blue == 0  # Game over when both piles are empty

# Function to announce the winner
def announce_winner(current_player, version):
    if version == 'standard':
        if current_player == 'human':
            print("\nGame over! You win! Congratulations!")
        else:
            print("\nGame over! The computer wins! Better luck next time!")
    elif version == 'misere':
        if current_player == 'human':
            print("\nGame over! The computer wins in misère mode! Better luck next time!")
        else:
            print("\nGame over! You win in misère mode! Congratulations!")

# Function to calculate the score at the end of the game
def calculate_score(red, blue):
    return red * 2 + blue * 3  # 2 points for red marbles, 3 points for blue marbles

# Validating user input for moves
def validate_move(pile, num_marbles, red, blue):
    if pile == 'red' and 0 < num_marbles <= red:
        return True
    elif pile == 'blue' and 0 < num_marbles <= blue:
        return True
    return False

# Human player's move
def human_move(red, blue):
    while True:
        pile = input("Which pile? (red/blue): ").lower()
        if pile not in ['red', 'blue']:
            print("Invalid choice. Try again.")
            continue

        try:
            num_marbles = int(input(f"How many marbles do you want to take from {pile}? "))
            if validate_move(pile, num_marbles, red, blue):
                return pile, num_marbles
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter a valid number.")

# Apply move to the game state
def apply_move(red, blue, move):
    pile, num_marbles = move
    if pile == 'red':
        red -= num_marbles
    else:
        blue -= num_marbles
    return red, blue

# MinMax with Alpha Beta Pruning and Depth-Limited Search
def minmax_ab(red, blue, depth, alpha, beta, is_maximizing, version):
    if check_game_over(red, blue) or depth == 0:
        return evaluate_score(red, blue, version, is_maximizing)

    if is_maximizing:
        max_eval = float('-inf')
        for move in get_possible_moves(red, blue):
            new_red, new_blue = apply_move(red, blue, move)
            eval = minmax_ab(new_red, new_blue, depth - 1, alpha, beta, False, version)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_possible_moves(red, blue):
            new_red, new_blue = apply_move(red, blue, move)
            eval = minmax_ab(new_red, new_blue, depth - 1, alpha, beta, True, version)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Generate possible moves
def get_possible_moves(red, blue):
    moves = []
    if red >= 1: moves.append(('red', 1))
    if blue >= 1: moves.append(('blue', 1))
    if red >= 2: moves.append(('red', 2))
    if blue >= 2: moves.append(('blue', 2))
    return moves

# Evaluate score (heuristic for non-terminal states)
def evaluate_score(red, blue, version, is_maximizing):
    if version == 'standard':
        if check_game_over(red, blue):
            return -math.inf if is_maximizing else math.inf
    elif version == 'misere':
        if check_game_over(red, blue):
            return math.inf if is_maximizing else -math.inf
    return red * 2 + blue * 3

# AI move using MinMax and Alpha Beta Pruning
def computer_move(red, blue, depth, version):
    best_move = None
    best_score = float('-inf')
    for move in get_possible_moves(red, blue):
        new_red, new_blue = apply_move(red, blue, move)
        score = minmax_ab(new_red, new_blue, depth - 1, float('-inf'), float('inf'), False, version)
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

# Main function to run the game
def nim_game():
    welcome_message()

    parser = argparse.ArgumentParser(description="Red-Blue Nim Game")
    parser.add_argument('num_red', type=int, help='Number of red marbles')
    parser.add_argument('num_blue', type=int, help='Number of blue marbles')
    parser.add_argument('--version', choices=['standard', 'misere'], default='standard', help='Game version')
    parser.add_argument('--first-player', choices=['human', 'computer'], default='computer', help='Who plays first')
    parser.add_argument('--depth', type=int, default=5, help='Depth of AI search (optional, default=5)')
    args = parser.parse_args()

    red_marbles = args.num_red
    blue_marbles = args.num_blue
    current_player = args.first_player
    game_over = False

    # Main game loop
    while not game_over:
        print(f"\nRed Marbles: {red_marbles}, Blue Marbles: {blue_marbles}")
        
        if current_player == 'human':
            move = human_move(red_marbles, blue_marbles)
        else:
            print("Computer is thinking...")
            move = computer_move(red_marbles, blue_marbles, args.depth, args.version)
            if move is not None:
                print(f"Computer takes {move[1]} from {move[0]} pile.")
            else:
                print("No valid moves available for the computer.")
                break  # Exit or handle the situation when no valid move is found

        red_marbles, blue_marbles = apply_move(red_marbles, blue_marbles, move)

        if check_game_over(red_marbles, blue_marbles):
            game_over = True
            announce_winner(current_player, args.version)
        else:
            current_player = 'computer' if current_player == 'human' else 'human'

# Entry point
if __name__ == "__main__":
    nim_game()
