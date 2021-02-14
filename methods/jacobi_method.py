import numpy as np
from methods.dominant_matrix import dominantify

ITERATION_LIMIT = 1000
epsilon = 1e-8


def jacobi(mat, res, x=None):
    if not dominantify(mat, res):
        return None
    if x is None:
        x = np.zeros(len(res))
    print("System of equations:")
    for i in range(mat.shape[0]):
        row = ["{0:3g}*x{1}".format(mat[i, j], j + 1) for j in range(mat.shape[1])]
        print("[{0}] = [{1:3g}]".format(" + ".join(row), res[i]))

    # The diagonal of the matrix
    diag = np.diag(np.diag(mat))
    # the matrix with 0 in the diagonal
    LU = mat - diag
    # the inverse of the
    D_inv = np.diag(1 / np.diag(diag))
    for i in range(ITERATION_LIMIT):
        # print the current x for this iteration
        print('iteration {0} starting guess:'.format(i), x)

        # # xr+1 = -Dinv(L+U)xr+Dinv*b
        x_new = np.dot(D_inv, res - np.dot(LU, x))

        # print the reworked x for this iteration
        print('iteration {0} new guess:'.format(i), x_new)
        if np.linalg.norm(x_new - x) < epsilon:
            return x_new
        x = x_new
    return x


if __name__ == "__main__":
    # problem data
    A = np.array([[0, 1., 2.], [-2., 1., 0.5], [1., -2., -0.5]])
    b = np.array([0., 4., -4.])
    x = jacobi(A, b)

    if x is not None:
        print("x:", x)
        print("computed b:", np.dot(A, x))
        print("real b:", b)
    else:
        print("failed")
