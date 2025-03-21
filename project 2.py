import random
import time

OPERATORS = ["+","-","*","%"]
min_operand = 1
max_operand = 30
total_problem = 10

def generate():
    left = random.randint(min_operand,max_operand)
    right = random.randint(min_operand,max_operand)
    operator = random.choice(OPERATORS)
    problem = str(left)+ " " + operator+ " " + str(right)
    answer = eval(problem)
    return problem , answer

input("Press enter to start!")
print("-----------------------------------")

start_time = time.time()

for x in range(total_problem):
    problem , answer = generate()
    
    while True:
        your_answer = input("Ploblem No." + str(x + 1) + ": " + problem + " = ")
        if str(answer) == your_answer :
            print("You are correct! Next!")
            break
        else:
            print("You are wrong!Try agian!")
        
end_time = time.time()
total_time = end_time - start_time
print("-----------------------------------")
print("Nice work! You finished in",total_time,"seconds!")
