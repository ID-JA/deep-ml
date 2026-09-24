def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	result = []

	for irow, row in enumerate(matrix):
		new_row = []
		for icol, col in enumerate(row):
			print()
			new_row.append(matrix[irow][icol] * scalar)
		result.append(new_row)

	return result
