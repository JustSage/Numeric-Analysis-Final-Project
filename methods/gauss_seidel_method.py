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

    for iterations in range(ITERATION_LIMIT):
        print("Iteration {0}: guess = {1}".format(iterations, x))
        x_new = np.array(x)
        for j in range(x.shape[0]):
            temp = 0
            for i in range(x.shape[0]):
                if i != j:
                    temp += mat[j][i] * x_new[i]
            x_new[j] = (res[j] - temp) / mat[j][j]
        if np.allclose(x, x_new, rtol=epsilon):
            print("Total iterations: {0}\nFinal result: {1}".format(iterations, x_new))
            return x_new
        x = x_new
    return None


if __name__ == "__main__":
    A = np.array([[-1., -1., 2.], [2., -1., 1.], [2., -4., 1.]])
    b = np.array([1., 4., -2.])
    x = gauss_seidel(A, b)

    if x is not None:
        print("x:", x)
        print("computed b: A*x = ", np.dot(A, x))
        print("real b: b = ", b)
    else:
        print("Not eligible")
