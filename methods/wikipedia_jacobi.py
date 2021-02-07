import numpy as np
from methods.dominant_matrix import dominantify


def jacobi(A, b, x_init=None, epsilon=1e-10, max_iterations=500):
    if not dominantify(A, b):
        return None
    if x_init is None:
        x_init = np.zeros(len(b))
    print("System of equations:")
    for i in range(A.shape[0]):
        row = ["{0:3g}*x{1}".format(A[i, j], j + 1) for j in range(A.shape[1])]
        print("[{0}] = [{1:3g}]".format(" + ".join(row), b[i]))

    D = np.diag(np.diag(A))
    LU = A - D
    x = x_init
    D_inv = np.diag(1 / np.diag(D))
    for i in range(max_iterations):
        # print the current x for this iteration
        print('iteration {0} starting guess:'.format(i), x)
        x_new = np.dot(D_inv, b - np.dot(LU, x))
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

    # you can choose any starting vector
    x = jacobi(A, b)

    if x is not None:
        print("x:", x)
        print("computed b:", np.dot(A, x))
        print("real b:", b)
    else:
        print("failed")
