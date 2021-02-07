import numpy as np
from methods.dominant_matrix import dominantify


def jacobi(A, b, x_init, epsilon=1e-10, max_iterations=500):
    if not dominantify(A, b):
        return None
    # print the dominant matrix and results
    print("dominant matrix:\n", A)
    print("dominant matrix results:", b)

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
    A = np.array([
        [-1., -2., 5.],
        [4., -1., 1.],
        [1., 6., 2.]
    ])
    b = np.array([2., 4., 9.])

    # you can choose any starting vector
    x_init = np.zeros(len(b))
    x = jacobi(A, b, x_init)

    if x is not None:
        print("x:", x)
        print("computed b:", np.dot(A, x))
        print("real b:", b)
    else:
        print("failed")
