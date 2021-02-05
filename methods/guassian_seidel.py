def guassian_seidel_method(matrix, result, variables):
    """
    Guassian-seidel iterative method will iterate over each row in the matrix
    and will calculate it's variables to provide a new solution.
    It will use the next solution of any non 0 variable from that row.

    Will deliver the result with less iterations than Jacobi iterative method.

    matrix - assuming diagonally dominant.
    result - the result colum of the matrix (b)
    variables - the variable column (x)
    """

    size = len(matrix)
    var = list(variables)
    for col in range(0, size):
        holder = result[col]
        for row in range(0, size):
            if col != row:  # if not diagonal index
                holder -= matrix[col,row] * var[row]
                # calculating variables x**(val=0,1,2,3,...)
        var[col] = holder / matrix[col,col]
        # updating yr+1/zr+1 with xr+1 etc
        # divide by dominant diagonal
    return var  # returns the updated values.
    ##