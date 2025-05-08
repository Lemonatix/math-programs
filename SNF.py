from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form
m = Matrix([[-1, 0, 0], [0, -1, 0], [0, 1, -1]]) # ET für Matrix([[-1, 0, 0], [0, -1, 0], [0, 1, -1]]) ist 1
print(smith_normal_form(m, domain=ZZ)) 