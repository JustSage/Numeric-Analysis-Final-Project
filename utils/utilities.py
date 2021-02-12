import numpy as np

def dominantify(mat, res):
    """ Makes the matrix diagonally dominant, if possible.
    :param mat:         The matrix.
    :param res:         The b component of Ax=b
    :return:            True if it succeeded, false otherwise.
    """
    row_max = [-1 for i in range(len(mat))]
    column_max = [False for i in range(len(mat))]
    for i in range(len(mat)):
        # get the absolute values of the row
        row = tuple(abs(mat[i][j]) for j in range(len(mat[i])))
        # find the maximum member of the row
        max_v = max(row)
        # find the sum of the rest
        rest_sum = sum(row) - max_v
        # check that the maximum dominates the row
        if max_v < rest_sum:
            return False

        # get the index the max is at
        index = np.where(row == max_v)[0][0]
        # mark the column the value is at and return false if it already has one
        if column_max[index]:
            return False
        column_max[index] = True
        # mark where the max of the current row is located
        row_max[i] = index

    # copy the matrix and b
    temp = np.array(mat)
    temp_res = np.array(res)

    for i in range(len(mat)):
        # place the i'th row in the row where the max will be on the pivot
        mat[row_max[i]] = np.array(temp[i])
        # adjust the b array accordingly
        res[row_max[i]] = temp_res[i]

    return True

def check_epsilon(xr,xr_1,tol):
    """
    Check_epsilon will check if the absolute value for each variable
    in solution substracted from the next solution is lower than the given
    epsilon, it will return false.
    """
    for x in range(0, len(xr)):
        if abs(xr_1[x] - xr[x]) < tol:
            return False
    return True