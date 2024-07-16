import random

def generate_multiplication_problem():
    num1 = random.randint(1000, 9999)
    num2 = random.randint(11, 99)  # To ensure the second number is not too large for division
    return f"{num1} * {num2}"

def generate_division_problem():
    num1 = random.randint(1000, 9999)
    factors = [i for i in range(11, 99) if num1 % i == 0]  # Get factors of num1 for valid division
    if factors:
        num2 = random.choice(factors)
        return f"{num1} / {num2}"
    else:
        # If no factors found, try generating another division problem
        return generate_division_problem()

# Generate 25 multiplication and 25 division problems
problems = [generate_multiplication_problem() for _ in range(25)] + [generate_division_problem() for _ in range(25)]

# Shuffle the problems to mix multiplication and division
random.shuffle(problems)

# Print the generated problems
for i, problem in enumerate(problems, start=1):
    print(f"{i}. {problem}")
