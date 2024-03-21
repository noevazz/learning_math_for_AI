from sympy import symbols, Eq, solve

# Define the variable
x = symbols('x')

# Define la equation
equation = Eq(-3*x - 21, -2*x + 7)

# Solve the equation
solution = solve(equation, x)

print(f"The solution for {equation} is {solution}")
