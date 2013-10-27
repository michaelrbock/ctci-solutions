def set_zeros(matrix):
	zero_locations = []
	for i, row in enumerate(matrix):
		for j, element in enumerate(row):
			if element == 0:
				zero_locations.append((i, j)) # row, col
	for location in zero_locations:
		i, j = location
		# set row to zeros
		matrix[i] = [0] * len(matrix[0])
		# set col to zeros
		for row in matrix:
			row[j] = 0
