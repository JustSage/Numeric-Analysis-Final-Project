import numpy as np
from methods.dominant_matrix import dominantify

ITERATION_LIMIT = 1000
epsilon = 1e-8

# initialize the matrix
A = np.array([[-2., 1., 0.5], [1., -2., -0.5], [0., 1., 2.]])
# initialize the RHS vector
b = np.array([4., -4., 0])


def gauss_seidel(mat, res, x=None):
    if not dominantify(mat, res):
        return None
    # initial guess, if not given, set to 0 vector.
    if x is None:
        x = np.zeros_like(res)
    print("System of equations:")
    for i in range(mat.shape[0]):
        row = ["{0:3g}*x{1}".format(mat[i, j], j + 1) for j in range(mat.shape[1])]
        print("[{0}] = [{1:3g}]".format(" + ".join(row), res[i]))

    for it_count in range(1, ITERATION_LIMIT):
        x_new = np.zeros_like(x)
        print("Iteration {0}: {1}".format(it_count, x))
        for i in range(mat.shape[0]):
            s1 = np.dot(mat[i, :i], x_new[:i])
            s2 = np.dot(mat[i, i + 1:], x[i + 1:])
            x_new[i] = (res[i] - s1 - s2) / mat[i, i]
        if np.allclose(x, x_new, rtol=epsilon):
            break
        x = x_new
    return x


if __name__ == "__main__":
    A = np.array([[-1., -1., 2.], [2., -1., 1.], [2., -4., 1.]])
    b = np.array([1., 4., -2.])
    x = gauss_seidel(A, b)

    if x is not None:
        print("x:", x)
        print("computed b:", np.dot(A, x))
        print("real b:", b)
    else:
        print("Not eligible")
