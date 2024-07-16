import random


def generate_bodmas_problem():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    num3 = random.randint(1, 100)
    num4 = random.randint(1, 100)

    operator1 = random.choice(['*', '/'])
    operator2 = random.choice(['+', '-'])

    # Ensure that division operations are valid
    if operator1 == '/':
        num3 = random.randint(1, 1000)  # Avoid division by zero
    if operator2 == '-' and num2 < num3:
        num2, num3 = num3, num2  # Ensure num2 >= num3 to avoid negative results

    problem = f"{num1} {operator1} ({num2} {operator2} {num3}) {operator1} {num4}"

    # Evaluate the expression to get the solution
    solution = eval(problem)

    return f"{problem} =", solution


# Generate 50 BODMAS problems
problems = [generate_bodmas_problem() for _ in range(25)]

# Print the generated problems
for i, (problem, _) in enumerate(problems, start=1):
    print(f"{i}. {problem}")

# Optional: Print the solutions for the problems
for i, (_, solution) in enumerate(problems, start=1):
    print(f"{i}. Solution: {solution}")
