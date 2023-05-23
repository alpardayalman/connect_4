# Connect Four Game

This is a simple implementation of the Connect Four game in Python. The game is played on a 7x6 grid, where two players take turns dropping their respective pieces (X or O) into a column of their choice. The goal is to be the first to connect four of their own pieces horizontally, vertically, or diagonally.

## Functions

### `print_board(board)`

This function takes a 2D list `board` representing the current state of the game and prints it in a visually appealing format. It displays the column numbers as the header and the board with the pieces.

### `move_is_valid(board, move)`

This function checks if a move is valid in the current state of the game. It takes the `board` and the selected `move` (column number) as inputs. The function returns `True` if the move is valid (the column exists and is not full) and `False` otherwise.

### `select_space(board, column, player)`

This function selects a space on the board for a player's piece. It takes the `board`, the selected `column`, and the `player` (X or O) as inputs. The function checks if the move is valid and places the player's piece at the bottom of the selected column. It returns `True` if the piece is successfully placed and `False` otherwise.

### `available_moves(board)`

This function returns a list of available moves (column numbers) in the current state of the game. It checks all columns and appends the valid moves to the list.

### `has_won(board, symbol)`

This function checks if a player with a specific `symbol` (X or O) has won the game. It checks for four consecutive symbols in horizontal, vertical, and diagonal directions. If a winning condition is found, the function returns `True`, otherwise `False`.

### `game_is_over(board)`

This function checks if the game is over. It returns `True` if either player has won the game or if there are no available moves left (a tie), and `False` otherwise.

### `play_game()`

This function is the main function that starts and controls the Connect Four game. It creates an empty board, alternates turns between players (X and O), and prompts the players for their moves. It checks for a winner after each move and displays the final result.

## How to Play

To play the Connect Four game, run the `play_game()` function. You will be prompted to select a column number to place your piece. The valid column numbers will be displayed as options. Enter your move and continue until the game ends. The game will display the board after each move and announce the winner or a tie at the end.

Have fun playing Connect Four!

