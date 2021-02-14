import numpy as np
from methods.dominant_matrix import dominantify

ITERATION_LIMIT = 1000
epsilon = 1e-8


def jacobi(mat, res, x=None):
    if not dominantify(mat, res):
        return None
    # initial guess, if not given, set to 0 vector.
    if x is None:
        x = np.zeros_like(res)
    print("System of equations:")
    for i in range(mat.shape[0]):
        row = ["{0:3g}*x{1}".format(mat[i, j], j + 1) for j in range(mat.shape[1])]
        print("[{0}] = [{1:3g}]".format(" + ".join(row), res[i]))

    for iterations in range(ITERATION_LIMIT):
        print("Iteration {0}: guess = {1}".format(iterations, x))
        x_new = np.array(x)
        for j in range(x.shape[0]):
            temp = 0
            for i in range(x.shape[0]):
                if i != j:
                    temp += mat[j][i] * x[i]
            x_new[j] = (res[j] - temp) / mat[j][j]
        if np.allclose(x, x_new, rtol=epsilon):
            print("Total iterations: {0}\nFinal result: {1}".format(iterations, x_new))
            return x_new
        x = x_new
    return None


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
