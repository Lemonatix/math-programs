from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form
m = Matrix([[8, 2, 9,-2], [22, 2, 28, -8], [20, -6, 31, -12]])
print(smith_normal_form(m, domain=ZZ))