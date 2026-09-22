import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	
	
	reshaped_matrix = []
	collen = len(a[0])
	rowlen = len(a)
	if collen * rowlen != new_shape[0] * new_shape[1]:
		return []

	

	# i did my own implmentation of reshaping matrix

	# for irow in range(rowlen):
	# 	for icol in range(0, collen, new_shape[1]):
	# 		new_row = a[irow][icol:icol + new_shape[1]]
	# 		reshaped_matrix.append(new_row)
		

	# or using numpy 
	return np.array(a).reshape(new_shape).tolist()
	# return reshaped_matrix