def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	if len(a[0]) != len(b):
		return -1
	results = []
	for row in a:
		sum_row = 0
		for pos, col in enumerate(row):
			sum_row += col*b[pos]
		results.append(sum_row)

	return  results
