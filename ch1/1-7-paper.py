def set_zeros(matrix):
	for i, row in enumerate(matrix):
		for j, element in enumerate(row):
			if element == 0:
				# change row to 0's
				for k in row:
					k = 0
				# change col to 0's
				for row1 in matrix:
					row1[j] = 0
