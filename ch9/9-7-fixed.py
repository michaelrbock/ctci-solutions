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
	return fill_r(canvas, row, col, new_color, canvas[row][col])

def fill_r(canvas, row, col, new, orig):
	if (row < 0 or row >= len(canvas) or
		col < 0 or col >= len(canvas[0])):
		return False

	if (canvas[row][col] == orig):
		canvas[row][col] = new
		fill_r(canvas, row - 1, col, new, orig) # up
		fill_r(canvas, row + 1, col, new, orig) # down
		fill_r(canvas, row, col - 1, new, orig) # left
		fill_r(canvas, row, col + 1, new, orig) # right
	return True
