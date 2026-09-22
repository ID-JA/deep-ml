import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	
	reshaped_matrix = []
	collen = len(a[0])
	rowlen = len(a)
	if collen * rowlen != new_shape[0] * new_shape[1]:
		return []

	
	# for irow in range(rowlen):
	# 	for icol in range(collen):
	# 		for jcol in range(icol+2, collen, 2):
	# 			print(f"{icol}:{jcol}")
	# 			print(a[irow][icol:jcol])

	for irow in range(rowlen):
		for icol in range(0, collen, new_shape[1]):
			new_row = a[irow][icol:icol + new_shape[1]]
			reshaped_matrix.append(new_row)
			# print(icol)
			# print(a[irow][:icol])
		

	# print(a[0][0:[new_shape[1]]])
	return reshaped_matrix