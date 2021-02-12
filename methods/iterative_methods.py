import numpy as np
import modules.modules as ui
import utils.utilities as utils
from . import guassian_seidel,jacobi


def linear_system_iterative_method(iterative_method, matrix, result, xr, epsilon):
    """
      linear_system_iterative_method is an iterative method used to solve a system of
      linear equations. Can be applied to any matrix with non-zero elements
      on the diagonals, convergence is only guarenteed if the matrix is either
      strictly diagonally dominant (D), or symmetric and positive definite.
      this function will check if the given matrix is diagonally dominant.
    """

    def check_epsilon(xr, xr_1,epsilon):
        """
        Check_epsilon will check if the absolute value for each variable
        in solution substracted from the next solution is lower than the given
        epsilon, it will return false.
        """
        for x in range(0, len(xr)):
            if abs(xr_1[x] - xr[x]) < epsilon:
                return False
        return True

    count = 0  # Iteration count
    table = ui.Table('count','x','y','z')
    condition = True  # Will have check_epsilon result

    while condition:
        xr_1 = iterative_method(matrix, result, xr)
        table.append_row(count,round(xr_1,5))
        # x_3float = list(map(lambda y: "{:.3f}".format(y), xr_1))
        # print(f"{count+1}\t{x_3float}")
        condition = check_epsilon(xr, xr_1, epsilon)
        xr = np.copy(xr_1)
        count += 1

    table.append_row(count, round(xr,5))
    table.show_table()

    # x_3float = list(map(lambda y: "{:.3f}".format(y), xr))
    # print(f"Final solution:{x_3float}")


def main():
    # Data Input (from class)
    epsilon = 0.0001  # tolerance
    x0 = np.array([0,0,0])

    matrix_29 = np.array([[0,1,2],[-2,1,0.5],[1,-2,-0.5]])
    matrix_29_result = np.array([0,4,-4])
    utils.dominantify(matrix_29, matrix_29_result)

    linear_system_iterative_method(jacobi, matrix_29, matrix_29_result, x0, epsilon)
    linear_system_iterative_method(guassian_seidel, matrix_29, matrix_29_result, x0, epsilon)

main()