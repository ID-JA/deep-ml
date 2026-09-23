def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

	means = []

	# rows = len(matrix)
	# cols = len(matrix[0])

	# if mode == "column":
	# 	for i in range(cols):
	# 		res_sum = 0
	# 		for j in range(rows):
	# 			res_sum += matrix[j][i]
	# 		means.append(res_sum/rows)
	# elif mode == "row":
	# 	for i in range(rows):
	# 		res_sum = 0
	# 		for j in range(cols):
	# 			res_sum += matrix[i][j]
	# 		means.append(res_sum/cols)

	if mode == "row":
		return [sum(row)/len(row) for row in matrix] 
	elif mode == "column":
		return [sum(col)/len(col) for col in zip(*matrix)]

	return means