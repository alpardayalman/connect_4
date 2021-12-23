def print_board(board):
	header = ' '
	for num in range(1, len(board) + 1):
	    header += ' '+ str(num) +'  '
	print(header)
	print('+---' * (len(board)) + '+')

	for row in range(len(board[0])):
	    print('|   ' * (len(board) +1))

	    row_with_items = ''
	    for col in range(len(board)):
	        row_with_items += ('| '+str(board[col][row])) + ' '
	    print(row_with_items + '|')

	    print('|   ' * (len(board) +1))

	    print('+---' * (len(board)) + '+')

def move_is_valid(board, move):
	# The column doesn't exist
    if move < 1 or move > (len(board)):
        return False

    # The column is full
    if board[move-1][0] != ' ':
        return False

    return True

def select_space(board, column, player):
	# Check to see if the move is valid
    if not move_is_valid(board, column):
        print("Trying to place an " + player + " in column " + str(column))
        print("Make sure to pick a column between 1 and " + str(len(board)) + " that is not full")
        print()
        return False

    # Check to make sure the symbol is either an X or O
    if player != "X" and player != "O":
        print("Trying to place an " + player + " in column " + str(column))
        print("Make sure to use either an 'X' or an 'O' as your piece")
        print()
        return False

    # Places a piece at the bottom of the selected column
    for y in range(len(board[0])-1, -1, -1):
        if board[column-1][y] == ' ':
            board[column-1][y] = player
            print("Placed an " + player + " in column " + str(column))
            print()
            return True
    return False

def available_moves(board):
    # Returns the columns that are open
    moves = []
    for i in range(1, len(board)+1):
        if move_is_valid(board, i):
            moves.append(i)
    return moves

def has_won(board, symbol):
    # check horizontal spaces
    for y in range(len(board[0])):
        for x in range(len(board) - 3):
            if board[x][y] == symbol and board[x+1][y] == symbol and board[x+2][y] == symbol and board[x+3][y] == symbol:
                return True

    # check vertical spaces
    for x in range(len(board)):
        for y in range(len(board[0]) - 3):
            if board[x][y] == symbol and board[x][y+1] == symbol and board[x][y+2] == symbol and board[x][y+3] == symbol:
                return True

    # check / diagonal spaces
    for x in range(len(board) - 3):
        for y in range(3, len(board[0])):
            if board[x][y] == symbol and board[x+1][y-1] == symbol and board[x+2][y-2] == symbol and board[x+3][y-3] == symbol:
                return True

    # check \ diagonal spaces
    for x in range(len(board) - 3):
        for y in range(len(board[0]) - 3):
            if board[x][y] == symbol and board[x+1][y+1] == symbol and board[x+2][y+2] == symbol and board[x+3][y+3] == symbol:
                return True

    return False

def game_is_over(board):
  # Returns True if either player has won the game or if there are no open columns
  return has_won(board, "X") or has_won(board, "O") or len(available_moves(board)) == 0

def play_game():
    # Creating an empty board
    my_board = []
    for col in range(7):
        my_board.append([' '] * 6)

    # Starting the game with X going first    
    turn = "X"
    winner = False
    while(not game_is_over(my_board)):

        print_board(my_board)
        move = 0
        available = available_moves(my_board)
        # Continuing to ask for a valid move until the user gives one
        while (move not in available):
            move = int(input("It is " + turn + "'s turn. Please select a column. Your optionns are " + str(available)))
        select_space(my_board, move, turn)
        # Checking to see if this move wins the game for the player. If so, exiting the loop
        if has_won(my_board, turn):
            print(turn + " has won!")
            print_board(my_board)
            winner = True
            break

        # Switching the players turn
        if turn == 'X':
            turn = "O"
        else:
            turn = 'X'
    # If we exit the loop and haven't determined a winner, that means it was a tie
    if not winner:
        print("It was a tie!")
        print_board(my_board)

play_game()
