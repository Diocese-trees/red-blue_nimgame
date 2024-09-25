# red-blue_nimgame
Red-Blue Nim is a two-player strategy game in which players take turns removing marbles from red and blue piles. These are the settings: Standard-the player who takes the last marble wins; Misere-the player who takes the last marble loses. Moves are determined through the MinMax algorithm to optimize moves and adjust difficulty.


Red-Blue Nim Game

## Overview
The **Red-Blue Nim Game** is an interactive two-player strategy game in which a player plays against his opponent by removing marbles from two piles, one red and one blue. The game contains two modes of gameplay: **Standard** and **Misere**, each with active strategic challenges to be engaged in.
## Key Features
- **Human vs. AI**: Engage in playing against an intelligent AI opponent.
MinMax Algorithm: It makes use of the **MinMax** algorithm for computing the moves to make it difficult.
 Alpha-Beta Pruning: It enables the decisions made by the AI by pruning a branch that is unnecessary for processing.
 Depth-Limited AI: Depending on a person, it can change to limit AI strength.
Game Modes:
 Standard Mode: In this mode, a player who took the last marble wins a game.
• **Misere Mode**: The player drawing the last marble is the loser.
 
## How to Play
1. There are initially set numbers of red and blue marbles.
2. Players remove one marble from either the red or the blue pile.
3. The game ends when one of the piles has been cleared.
4. Scores are determined by the remaining marbles:
-2 points for each red marble.
   -3 points for each blue marble.

## Running the Game
1. Clone the repository.
    ```bash
    git clone https://github.com/yourusername/red-blue-nim-game.git
    ```
2. Change into the directory.
    ```bash
    cd red-blue-nim-game
    ```
3. Run the game with Python.
    ```bash
python "red blue nim game.py" <num_red> <num_blue> --version <version> --first-player <player> --depth <depth>
    ```
    Example:
    ```bash
    python "red blue nim game.py" 5 3 --version standard --first-player human --depth 5
    ```

### Arguments:
- `<num_red>`: Number of red marbles.
- `<num_blue>`: Number of blue marbles.
- `--version`: Game version, either `standard` or `misere` (default: `standard`).
--first-player: Choose who makes the first move - human or computer. Default is computer.
--depth: AI search depth, MinMax algorithm. Default is 5.

## Technologies Used
- **Python**: Main programming language.
- **MinMax Algorithm**: To realize AI decisions.
- **Alpha-Beta Pruning**: For optimization of the AI computations.

## Future Scope
- More game play.
- A graphical interface for better user interaction.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
