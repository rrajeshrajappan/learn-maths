import random

def generate_square_root_problem():
    problem_type = random.choice(["square", "square_root"])

    if problem_type == "square":
        number = random.randint(1, 20)
        problem = f"What is the square of {number}?"
        answer = number ** 2

    elif problem_type == "square_root":
        number = random.randint(1, 100)
        problem = f"What is the square root of {number}?"
        answer = round(number ** 0.5, 2)

    return problem, answer

# Generate 25 square and square root problems
for i in range(25):
    problem, answer = generate_square_root_problem()
    print(f"Problem {i+1}: {problem}")
    print("Answer:", answer)
    print()
