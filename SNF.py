from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form
m = Matrix([[12, 6, 4], [3, 9, 6], [2, 16, 14]])
print(smith_normal_form(m, domain=ZZ))