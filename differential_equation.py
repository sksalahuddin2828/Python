import sympy as sp

# Define the variable and function
x = sp.symbols('x')
y = sp.Function('y')(x)

# Define the differential equation
differential_eq = sp.Eq(y.diff(x), 2 * y)

# Solve the differential equation with the initial condition y(0) = 0
solution = sp.dsolve(differential_eq, ics={y.subs(x, 0): 0})

# Display the solution
print("Solution of the differential equation:")
print(solution)


# Answer: Solution of the differential equation:
#         Eq(y(x), 0)
