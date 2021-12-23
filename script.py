board = [[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']]



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
