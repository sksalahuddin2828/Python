# Program 1:
import sympy
from sympy import N, sqrt

# Calculate square root of 2 with 100 decimal places
result = N(sqrt(2), 100)
print(result)

# Program 2:
from sympy import Rational

# Add rational numbers
a = Rational(1, 2)
b = Rational(1, 3)
sum_result = a + b
print(sum_result)

# Program 3:
import sympy as sym

# Expand a binomial expression
x, y = sym.symbols('x y')
expression = (x + y)**6
expanded_expr = sym.expand(expression)
print(expanded_expr)

# Program 4:
import sympy
from sympy import Symbol, simplify, sin, cos

# Simplify a trigonometric expression
x = Symbol('x')
trig_expr = sin(x) / cos(x)
simplified_expr = simplify(trig_expr)
print(simplified_expr)

# Program 5:
import sympy
from sympy import Symbol, solveset, sin

# Solve an equation involving a trigonometric function
x = Symbol('x')
equation = (sin(x) - x) / (x**3)
solution_set = solveset(equation, x)
print(solution_set)

# Program 6:
import sympy
from sympy import symbols, log, Derivative

# Calculate derivatives
x = symbols('x')
expr1 = log(x)
expr1_diff = Derivative(expr1, x)
expr1_derivative = expr1_diff.doit()
print(f"Derivative of expression with respect to x: {expr1_diff}")
print(f"Value of the derivative: {expr1_derivative}")

expr2 = 1 / x
expr2_diff = Derivative(expr2, x)
expr2_derivative = expr2_diff.doit()
print(f"Derivative of expression with respect to x: {expr2_diff}")
print(f"Value of the derivative: {expr2_derivative}")

expr3 = sin(x)
expr3_diff = Derivative(expr3, x)
expr3_derivative = expr3_diff.doit()
print(f"Derivative of expression with respect to x: {expr3_diff}")
print(f"Value of the derivative: {expr3_derivative}")

expr4 = cos(x)
expr4_diff = Derivative(expr4, x)
expr4_derivative = expr4_diff.doit()
print(f"Derivative of expression with respect to x: {expr4_diff}")
print(f"Value of the derivative: {expr4_derivative}")

# Program 7:
import sympy
from sympy import symbols, Eq, solve

# Solve a system of equations
x, y = symbols('x y')
eq1 = Eq(x + y - 2, 0)
eq2 = Eq(2 * x + y, 0)
solution_dict = solve((eq1, eq2), (x, y))
print(f"x = {solution_dict[x]}")
print(f"y = {solution_dict[y]}")

# Program 8:
import sympy
from sympy import symbols, integrate, sin, cos

# Perform integrations
x = symbols('x')
integrated_expr1 = integrate(x**2, x)
print(f"Integration of x^2: {integrated_expr1}")

integrated_expr2 = integrate(sin(x), x)
print(f"Integration of sin(x): {integrated_expr2}")

integrated_expr3 = integrate(cos(x), x)
print(f"Integration of cos(x): {integrated_expr3}")

# Program 9:
import sympy as sym
from sympy import symbols, Function, Eq, dsolve

# Solve a differential equation
x = symbols('x')
f = Function('f')(x)
equation = Eq(f.diff(x, x) + 9 * f, 1)
solution = dsolve(equation, f)
print(solution)

# Program 10:
import sympy as sym
from sympy import symbols, Matrix, linsolve

# Solve a linear system of equations
x, y, z = symbols('x y z')
M = Matrix(((3, 7, -12, 0), (4, -2, -5, 0)))
system = A, b = M[:, :-1], M[:, -1]
solution_set = linsolve(system, x, y, z)
print(solution_set)
