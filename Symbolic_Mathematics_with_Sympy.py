# Number of program 1
import sympy
from sympy import N, sqrt

# Calculate square root of 2 with 100 decimal places
square_root_2 = N(sqrt(2), 100)
print(square_root_2)

# PNumber of program 2
from sympy import Rational

# Add rational numbers
half = Rational(1, 2)
third = Rational(1, 3)
sum_result = half + third
print(sum_result)

# Number of program 3
import sympy as sym

# Expand a binomial expression
var_x, var_y = sym.symbols('x y')
binomial_expr = (var_x + var_y)**6
expanded_expr = sym.expand(binomial_expr)
print(expanded_expr)

# Number of program 4
import sympy
from sympy import Symbol, simplify, sin, cos

# Simplify a trigonometric expression
var_x = Symbol('x')
trig_expr = sin(var_x) / cos(var_x)
simplified_expr = simplify(trig_expr)
print(simplified_expr)

# Number of program 5
import sympy
from sympy import Symbol, solveset, sin

# Solve an equation involving a trigonometric function
var_x = Symbol('x')
equation = (sin(var_x) - var_x) / (var_x**3)
solution_set = solveset(equation, var_x)
print(solution_set)

# Number of program 6
import sympy
from sympy import symbols, log, Derivative

# Calculate derivatives
var_x = symbols('x')
log_expr = log(var_x)
log_derivative = Derivative(log_expr, var_x)
log_derivative_value = log_derivative.doit()
print(f"Derivative of log(x) with respect to x: {log_derivative}")
print(f"Value of the derivative: {log_derivative_value}")

inverse_expr = 1 / var_x
inverse_derivative = Derivative(inverse_expr, var_x)
inverse_derivative_value = inverse_derivative.doit()
print(f"Derivative of 1/x with respect to x: {inverse_derivative}")
print(f"Value of the derivative: {inverse_derivative_value}")

sin_expr = sin(var_x)
sin_derivative = Derivative(sin_expr, var_x)
sin_derivative_value = sin_derivative.doit()
print(f"Derivative of sin(x) with respect to x: {sin_derivative}")
print(f"Value of the derivative: {sin_derivative_value}")

cos_expr = cos(var_x)
cos_derivative = Derivative(cos_expr, var_x)
cos_derivative_value = cos_derivative.doit()
print(f"Derivative of cos(x) with respect to x: {cos_derivative}")
print(f"Value of the derivative: {cos_derivative_value}")

# Number of program 7
import sympy
from sympy import symbols, Eq, solve

# Solve a system of equations
var_x, var_y = symbols('x y')
equation1 = Eq(var_x + var_y - 2, 0)
equation2 = Eq(2 * var_x + var_y, 0)
solution_dict = solve((equation1, equation2), (var_x, var_y))
print(f"x = {solution_dict[var_x]}")
print(f"y = {solution_dict[var_y]}")

# Number of program 8
import sympy
from sympy import symbols, integrate, sin, cos

# Perform integrations
var_x = symbols('x')
integrated_expr1 = integrate(var_x**2, var_x)
print(f"Integration of x^2: {integrated_expr1}")

integrated_expr2 = integrate(sin(var_x), var_x)
print(f"Integration of sin(x): {integrated_expr2}")

integrated_expr3 = integrate(cos(var_x), var_x)
print(f"Integration of cos(x): {integrated_expr3}")

# Number of program 9
import sympy as sym
from sympy import symbols, Function, Eq, dsolve

# Solve a differential equation
var_x = symbols('x')
function_f = Function('f')(var_x)
differential_equation = Eq(function_f.diff(var_x, var_x) + 9 * function_f, 1)
solution = dsolve(differential_equation, function_f)
print(solution)

# Number of program 10
import sympy as sym
from sympy import symbols, Matrix, linsolve

# Solve a linear system of equations
var_x, var_y, var_z = symbols('x y z')
coeff_matrix = Matrix(((3, 7, -12, 0), (4, -2, -5, 0)))
system = coefficient_matrix, constants = coeff_matrix[:, :-1], coeff_matrix[:, -1]
solution_set = linsolve(system, var_x, var_y, var_z)
print(solution_set)


#-----------------------------------------------------------------------------------------------------------------------------------------------------


# Answer: 1.414213562373095048801688724209698078569671875376948073176679737990732478462107038850387534327641573
#         5/6
#         x**6 + 6*x**5*y + 15*x**4*y**2 + 20*x**3*y**3 + 15*x**2*y**4 + 6*x*y**5 + y**6
#         tan(x)
#         Complement(ConditionSet(x, Eq(-x + sin(x), 0), Complexes), {0})
#         Derivative of log(x) with respect to x: Derivative(log(x), x)
#         Value of the derivative: 1/x
#         Derivative of 1/x with respect to x: Derivative(1/x, x)
#         Value of the derivative: -1/x**2
#         Derivative of sin(x) with respect to x: Derivative(sin(x), x)
#         Value of the derivative: cos(x)
#         Derivative of cos(x) with respect to x: Derivative(cos(x), x)
#         Value of the derivative: -sin(x)
#         x = -2
#         y = 4
#         Integration of x^2: x**3/3
#         Integration of sin(x): -cos(x)
#         Integration of cos(x): sin(x)
#         Eq(f(x), C1*sin(3*x) + C2*cos(3*x) + 1/9)
#         {(59*z/34, 33*z/34, z)}
