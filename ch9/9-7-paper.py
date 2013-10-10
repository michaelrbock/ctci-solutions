"""
Canvas:
2-D Array Representation: [[A, B], [C, D], [E, F], [G, H]] is 4x2
    0   1
  ---------
0 | A | B |  -
1 | C | D |   | rows
2 | E | F |   |
3 | G | H |  -
  ---------
  |_______|
    cols
Where A-H are colors as strings
"""

def fill(canvas, row, col, new_color):
	fill_r(canvas, row, col, new_color, canvas[row][col])

def fill_r(canvas, row, col, new, orig):
	canvas[row][col] = new # change color
	# check for all four directions
	min = 0
	max_row = len(canvas)
	max_col = len(canvas[0])
	# up
	if row - 1 >= min and canvas[row-1][col] == orig:
		fill_r(canvas, row - 1, col, new, orig)
	# right
	if col + 1 <= max_col and canvas[row][col+1] == orig:
		fill_r(canvas, row, col + 1, new, orig)
	# down
	if row + 1 <= max_row and canvas[row+1][col] == orig:
		fill_r(canvas, row + 1, col, new, orig)
	# left
	if col - 1 >= min and canvas[row][col-1] == orig:
		fill_r(canvas, row, col - 1, new, orig)
