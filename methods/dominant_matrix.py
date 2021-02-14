import numpy as np


def dominantify(mat, res, second=False):
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
            if not second:
                # attempt to dominantify with columns instead
                mat_t = mat.transpose()
                filler = np.zeros(res.shape[0])
                flag = dominantify(mat_t, filler, True)
                if flag:
                    np.copyto(mat, mat_t.transpose())
                    return flag
            return False

        # get the index the max is at
        index = np.where(row == max_v)[0][0]
        # mark the column the value is at and return false if it already has one
        if column_max[index]:
            if not second:
                # attempt to dominantify with columns instead
                mat_t = mat.transpose()
                filler = np.zeros(res.shape[0])
                flag = dominantify(mat_t, filler, True)
                if flag:
                    np.copyto(mat, mat_t.transpose())
                    return flag
            return False
        column_max[index] = True
        # mark where the max of the current row is located
        row_max[i] = index

    # copy the matrix and b
    temp = np.array(mat)
    temp_res = np.array(res)

    for i in range(len(mat)):
        # place the ith row in the row where the max will be on the pivot
        mat[row_max[i]] = np.array(temp[i])
        # adjust the b array accordingly
        res[row_max[i]] = temp_res[i]

    return True


if __name__ == "__main__":
    mat = np.array([[1., 1., 3.], [4., 4., 1.], [2., 6., 1.]])
    res = np.array([1, 4, -2])
    dominantify(mat, res)
    print(mat)
    print(res)
