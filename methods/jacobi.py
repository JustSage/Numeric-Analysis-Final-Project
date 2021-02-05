
def jacobi_method(matrix, result, variables):
    """
    Jacobi iterative method will iterate over each row in the matrix
    and will calculate it's variables to provide a new solution.

    Will not use the next solution therefore may cause additional iterations.

    matrix - assuming diagonally dominant.
    result - the result colum of the matrix (b)
    variables - the variable column (x)
    """
    size = len(matrix)
    new_vars = []  # will append the new solutions to it.
    for col in range(0, size):
        holder = result[col]
        for row in range(0, size):
            if col != row:  # if not diagonal index
                holder -= matrix[col][row] * variables[row]
                # calculating variables x**(val=0,1,2,3,...)
        new_vars.append(holder / matrix[col][col])
    # not updating yr+1/zr+1 with xr+1 etc
    # divide by dominant diagonal
    return new_vars  # returns the updated values.