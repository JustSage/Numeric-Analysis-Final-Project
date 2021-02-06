import numpy as np
from dominant_matrix import dominantify

ITERATION_LIMIT = 1000

# initialize the matrix
A = np.array([[-2., 1., 0.5], [1., -2., -0.5], [0., 1., 2.]])
# initialize the RHS vector
b = np.array([4., -4., 0])


def gauss_seidel(A, b):
    print("System of equations:")
    for i in range(A.shape[0]):
        row = ["{0:3g}*x{1}".format(A[i, j], j + 1) for j in range(A.shape[1])]
        print("[{0}] = [{1:3g}]".format(" + ".join(row), b[i]))

    x = np.zeros_like(b)
    for it_count in range(1, ITERATION_LIMIT):
        x_new = np.zeros_like(x)
        print("Iteration {0}: {1}".format(it_count, x))
        for i in range(A.shape[0]):
            s1 = np.dot(A[i, :i], x_new[:i])
            s2 = np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        if np.allclose(x, x_new, rtol=1e-8):
            break
        x = x_new
    return x


if __name__ == "__main__":
    A = np.array([[-1., -1., 2.], [2., -1., 1.], [2., -4., 1.]])
    b = np.array([1., 4., -2.])
    if dominantify(A, b):
        print(A)
        print(b)
        x = gauss_seidel(A, b)
        print("Solution: {0}".format(x))
        error = np.dot(A, x) - b
        print("Error: {0}".format(error))