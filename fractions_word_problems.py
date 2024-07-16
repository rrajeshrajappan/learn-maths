import random

def generate_fraction_word_problem():
    problem_type = random.choice([
        "spending",
        "proportion",
        "selling",
        "plane_journey",
        "painting",
        "animal_shelter",
        "taco_recipe",
        "cupcake_icing",
        "lawn_mowing"
    ])

    if problem_type == "spending":
        fraction = f"{random.randint(1, 9)}/9"
        remaining_fraction = f"{9 - eval(fraction)} / 9"
        problem = f"Pragya spent {fraction} of her allowance on food and shopping. What fraction of her allowance had she left?"
        answer = remaining_fraction

    elif problem_type == "proportion":
        girls_fraction = random.randint(1, 4)
        total_children = random.randint(10, 50)
        girls_count = (girls_fraction * total_children) // 5
        problem = f"{girls_fraction}/5 of a group of children were girls. If there were {girls_count} girls, how many children were there in the group?"
        answer = total_children

    elif problem_type == "selling":
        teddy_bears = random.randint(50, 200)
        sold_fraction = random.randint(1, 3)
        sold_count = (teddy_bears * sold_fraction) // 3
        problem = f"Tarika had {teddy_bears} teddy bears in his toy store. He sold {sold_fraction}/3 of them at $12 each. How much did he receive?"
        answer = sold_count * 12

    elif problem_type == "plane_journey":
        expected_time = random.randint(1, 10) * 0.1
        actual_time = expected_time + (1 / 5)
        problem = f"Rajesh thought that a plane journey would take {expected_time} hour but the actual journey took {actual_time} hour longer. How long did the actual journey take?"
        answer = actual_time

    elif problem_type == "painting":
        portrait_time = random.randint(2, 10) / 3
        scenery_time = portrait_time + (1 / 3)
        problem = f"Sarala took {portrait_time} hour to paint a portrait. This was 1/3 hour shorter than the time she took to paint scenery. How long did she take to paint scenery?"
        answer = scenery_time

    elif problem_type == "animal_shelter":
        cats_fraction = f"{random.randint(1, 5)}/6"
        male_cats_fraction = f"{random.randint(1, 2)}/2"
        male_fraction = eval(cats_fraction) * eval(male_cats_fraction)
        problem = f"At the animal shelter {cats_fraction} of the animals are cats. Of the cats {male_cats_fraction} are male. What fraction of the animals at the shelter are male cats?"
        answer = male_fraction

    elif problem_type == "taco_recipe":
        tacos = random.randint(1, 10)
        cheese_per_taco = f"2/3"
        cheese_needed = tacos * eval(cheese_per_taco)
        problem = f"A taco recipe called for {cheese_per_taco} cup of cheese per taco. If Andrew wanted to make {tacos} tacos, how much cheese would he need?"
        answer = cheese_needed

    elif problem_type == "cupcake_icing":
        cupcakes = random.randint(10, 50)
        mint_icing_fraction = f"1/5"
        chocolate_icing_fraction = f"1/2"
        mint_icing_count = cupcakes * eval(mint_icing_fraction)
        remaining_cupcakes = cupcakes - mint_icing_count
        chocolate_icing_count = remaining_cupcakes * eval(chocolate_icing_fraction)
        vanilla_icing_count = remaining_cupcakes - chocolate_icing_count
        problem = f"Ethan is icing {cupcakes} cupcakes. He spreads mint icing on {mint_icing_count} of the cupcakes and chocolate on {chocolate_icing_count} of the remaining cupcakes. The rest will get vanilla frosting. How many cupcakes have vanilla frosting?"
        answer = vanilla_icing_count

    elif problem_type == "lawn_mowing":
        total_money = random.randint(30, 100)
        saved_fraction = f"1/4"
        money_after_saving = total_money * eval(saved_fraction)
        remaining_money = total_money - money_after_saving
        sister_fraction = f"1/2"
        money_to_sister = remaining_money * eval(sister_fraction)
        remaining_money = remaining_money - money_to_sister
        problem = f"Maddox puts {saved_fraction} of her lawn-mowing money in savings and uses {sister_fraction} of the remaining money to pay back her sister. If she has ${remaining_money} left, how much did she have at first?"
        answer = total_money

    return problem, answer
answers = []
# Generate 25 fraction word problems
for i in range(25):
    problem, answer = generate_fraction_word_problem()
    print(f"Problem {i+1}: {problem}")
    print()
    answers.append(answer)

for i, answer in enumerate (answers):
    print(f"{i+1}. {answer}")
