'''
Sudoku Solver

'''

from sets import Set



def find_empty_cell(sudoku):
'''
Find an empty cell

'''
	
	for row in range(9):
		for col in range(9):
			if sudoku[row][col] is None or sudoku[row][col] < 1 or sudoku[row][col] > 9:
				return (row, col)

	return (None, None)



def get_valid_options(sudoku, row, col):
'''
Get all possible valid options for empty cell

'''

	invalid_x = Set([])
	
	for i in range(9):
		if sudoku[row][i] is not None:
			invalid_x.update([sudoku[row][i]])
		if sudoku[i][col] is not None:
			invalid_x.update([sudoku[i][col]])

	box_row = row - (row % 3)
	box_col = col - (col % 3)

	for i in range(box_row, box_row + 3):
		for j in range(box_col, box_col + 3):
			if sudoku[i][j] is not None:
				invalid_x.update([sudoku[i][j]])

	return Set(range(1,10)) - invalid_x



def solve_sudoku(sudoku):
'''
Recursive function that solves empty cells

'''

	row, col = find_empty_cell(sudoku)

	if row is None and col is None:
		return True

	valid_options = get_valid_options(sudoku, row, col)
	
	for x in valid_options:
		sudoku[row][col] = x
		if solve_sudoku(sudoku):
			return True
		sudoku[row][col] = None

	return False



if __name__ == '__main__':

	sudoku = [
				[None, None, 2, None, None, 5, 9, None, None],
				[4, None, None, None, None, 9, None, None, 8],
				[7, None, None, None, None, 2, 1, 6, None],
				[None, None, 1, None, None, 4, 2, None, None],
				[None, 3, None, None, None, None, None, 4, None],
				[None, None, 9, 6, None, None, 5, None, None],
				[None, 2, 5, 9, None, None, None, None, 1],
				[3, None, None, 5, None, None, None, None, 2],
				[None, None, 4, 8, None, None, 3, None, None]
			 ]

	if solve_sudoku(sudoku):
		for x in range(9):
			print sudoku[x]

	else:
		print "No Solution found"