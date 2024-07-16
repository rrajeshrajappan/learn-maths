import random


def generate_fraction_problem():
    num1 = random.randint(1, 10)  # numerator
    den1 = random.randint(2, 10)  # denominator, ensuring it's not 1
    num2 = random.randint(1, 10)
    den2 = random.randint(2, 10)

    operator = random.choice(['+', '-', '*', '/'])

    if operator == '+':
        result = (num1 * den2 + num2 * den1, den1 * den2)
    elif operator == '-':
        result = (num1 * den2 - num2 * den1, den1 * den2)
    elif operator == '*':
        result = (num1 * num2, den1 * den2)
    else:
        result = (num1 * den2, den1 * num2)

    return f"{num1}/{den1} {operator} {num2}/{den2} = ", result


# Generate 50 fraction problems
problems = [generate_fraction_problem() for _ in range(25)]

# Print the generated problems
for i, (problem, _) in enumerate(problems, start=1):
    print(f"{i}. {problem}")

# Optional: Print the solutions for the problems
for i, (_, solution) in enumerate(problems, start=1):
    print(f"{i}. Solution: {solution[0]}/{solution[1]}")
