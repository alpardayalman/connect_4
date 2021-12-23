def make_board():
  board = [[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']]
  return board


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

my_board = make_board()
select_space(my_board, 0, 'X')
select_space(my_board, 5, "W")
select_space(my_board, 1, 'X')
select_space(my_board, 5, 'O')
select_space(my_board, 5, 'O')
select_space(my_board, 5, 'O')
select_space(my_board, 5, 'O')
select_space(my_board, 5, 'O')
select_space(my_board, 5, 'O')
select_space(my_board, 5, 'O')
print_board(my_board)
