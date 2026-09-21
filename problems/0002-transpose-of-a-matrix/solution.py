def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    transpo_mat = []
    # for irow, row in enumerate(a):
    #     for icol, col in enumerate(row):
    #         print("irow", irow)
    #         print("icol", icol)
    #         print(a[irow][icol])
    #         break
    
    # irow = 0
    # icol = 0 
    # for row in a:
    #     for col in row:
    #         print(a[irow][icol])
    #         break
    #     irow+=1
    #     if irow == len(a):
    #         icol+=1

    # for irow, row in enumerate(a):
    #     for item_col in row:
    #         transpo_mat.append([item_col])
        
    # print(transpo_mat)
    num_rows = len(a)
    num_cols = len(a[0])


    for col in range(num_cols):
        transpo_mat.append([])
        for row in range(num_rows):
            transpo_mat[col].append(a[row][col])
    return transpo_mat