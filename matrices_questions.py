from methods.gauss_seidel_method import gauss_seidel
from methods.jacobi_method import jacobi
import numpy as np


matrix1 = np.array([[10., 8., 1.], [4., 10., -5.], [5., 1., 10.]])
matrix2 = np.array([[0, 1., 2.], [-2., 1., 0.5], [1., -2., -0.5]])

result1 = np.array([-7., 2., 1.5])
result2 = np.array([0., 4., -4.])

print("\nquestion 20\n")
x1_gauss = gauss_seidel(matrix1, result1)
print()
x1_jacobi = jacobi(matrix1, result1)
print("\ngauss seidel solution:", x1_gauss)
print("jacobi solution:", x1_jacobi, "\n")

print("\nquestion 29\n")
x2_gauss = gauss_seidel(matrix2, result2)
print()
x2_jacobi = jacobi(matrix2, result2)
print("\ngauss seidel solution:", x2_gauss)
print("jacobi solution:", x2_jacobi)
