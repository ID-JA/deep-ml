def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    mat_det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    if mat_det != 0:
        
        return [
            [matrix[1][1]/mat_det, -matrix[0][1]/mat_det],
            [-matrix[1][0]/mat_det, matrix[0][0]/mat_det]
        ]
        # num_rows = len(matrix)
        # num_cols = len(matrix[0])
        # mat_inv = []

        # for irow in range(num_rows):
        #     new_row = []
        #     for icol in range(num_cols):
        #         if irow == icol :
        #             new_row.insert(0, matrix[irow][icol  - 1] * -1)
        #         else:
        #             new_row.insert(0, matrix[irow][icol  - 1])

        #     print(new_row)
                    
        # print([matrix[i -1][i] for i in range(len(matrix))])
        

        # for icol in range(num_cols - 1, -1, -1):
        #     new_row = []
        #     for irow in range(num_rows):
        #         if icol == irow : 
        #             print(matrix[icol -1][icol] * -1)
        #         else:
        #             print(matrix[irow][icol])

        
        # return [ [ round(-item * (1/mat_det), 2) for item in row] for row in matrix]

        return []
    else:
        return None