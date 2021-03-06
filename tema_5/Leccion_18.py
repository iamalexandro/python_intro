# -*- coding: utf-8 -*-
# Herramientas para computación científica
# Lección 18
# SymPy: Álgebra lineal

from sympy import *


def main():
    x = Symbol('x')
    y = Symbol('y')
    a = Matrix([[1, x], [y, 1]])

    print(a)
    print(a ** 2)

    b = Matrix([[1, x], [x, 1]])
    print(b.eigenvals())
    print(b.eigenvects())
    print(b.det_LU_decomposition())

if __name__ == '__main__':
    main()
