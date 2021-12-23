# Representing the board as a 2D list with 7 rows and 6 columns. The board is actually represented sideways - when we print the board there's 7 columns and 6 rows. Encoding the board sideways will make adding a piece to a column much easier.
board = [[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']]

# Placing some pieces on the board so we can verify we know how to place pieces in certain locations
board[0][5] = 'X'
board[5][5] = 'O'

# Creating and printing the the header of the board - numbers to let the user know which column is what
header = ' '
for num in range(1, len(board) + 1):
    header += ' '+ str(num) +'  '
print(header)
print('+---' * (len(board)) + '+')

# Printing each row of the board
for row in range(len(board[0])):
    print('|   ' * (len(board) +1))

    row_with_items = ''
    for col in range(len(board)):
        row_with_items += ('| '+str(board[col][row])) + ' '
    print(row_with_items + '|')

    print('|   ' * (len(board) +1))

    print('+---' * (len(board)) + '+')
