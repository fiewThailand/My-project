#let guess number untail you correct
import random

def guess(x):
    random_number = random.randint(1,x) #randiant(a,b)ใช้สุ่มตัวเลขระหว่างa,b
    guess = 0 
    while guess != random_number : # ถ้า guess ไม่เท่ากับ random_number จะให้ค่าจริง
        guess = int(input(f"Guess a number between 1 and {x}:"))
        if guess < random_number:
            print("Sorry , guess again.Too low")
            break
        elif guess > random_number :
            print("Sorry , guess again.Too high")
            break
        else :
            print(f"You are so lucky , {random_number} correct")

guess(10)