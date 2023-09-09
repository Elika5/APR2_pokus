import random

def generate_math_problem():
    # Generujeme náhodné čísla pro úlohu
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    
    # Vybrání náhodné matematické operace
    operator = random.choice(['+', '-', '*', '/'])
    
    # Generování textového popisu úlohy
    if operator == '+':
        problem = f"{num1} + {num2} = ?"
        answer = num1 + num2
    elif operator == '-':
        problem = f"{num1} - {num2} = ?"
        answer = num1 - num2
    elif operator == '*':
        problem = f"{num1} * {num2} = ?"
        answer = num1 * num2
    else:
        # Zabránění dělení nulou a zaokrouhlení výsledku
        answer = round(num1 / num2, 2)
        problem = f"{num1} / {num2} = ?"

    return problem, answer

def create_problem_file(problems):
    with open("math_problems.txt", "w") as file:
        for problem, answer in problems.items():
            file.write(f"{problem} Odpověď: {answer}\n")
    print("Úlohy byly uloženy do souboru 'math_problems.txt'.")

def solve_problems(problems):
    correct_answers = 0
    for problem in problems:
        print(problem)
        user_answer = input("Zadejte odpověď: ")
        try:
            user_answer = float(user_answer)
            if user_answer == problems[problem]:
                print("Správně!")
                correct_answers += 1
            else:
                print("Nesprávně.")
        except ValueError:
            print("Neplatný vstup, očekáváme číslo.")
    
    return correct_answers

def main():
    num_problems = int(input("Kolik úloh chcete vygenerovat? "))
    
    problems = {}
    
    for _ in range(num_problems):
        problem, answer = generate_math_problem()
        problems[problem] = answer
    
    print("\nVygenerované úlohy:")
    
    choice = input("Chcete řešit úlohy? (ano/ne) ").lower()
    
    if choice == 'ano':
        correct_answers = solve_problems(problems)
        print(f"\nVyřešili jste {correct_answers} z {num_problems} úloh správně.")
    else:
        create_problem_file(problems)

if __name__ == "__main__":
    main()
