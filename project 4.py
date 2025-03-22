import random

#ต้องเพิ่มว่าถ้าใส่ค่าอื่นที่ไม่ใช่ h l c มาบอกให้ใส่ใหม่เป็นพวกนี่

print("I will guess number in your mine")
input("Press enter to start!")
print("---------------------------------------------------------")

def computer_guess_your_number(x):
    low = 1
    high = x
    feedback = " "
    while feedback != "c": #ทำงานเมื่อ feedback ไม่เท่ากับ c ง่ายๆคือหยุดทำงานเมื่อถูก
        if low != high : 
            guess = random.randint(low,high)
        
        feedback = input(f"Is {guess} too high (h) too low (l) or correct (c)?")
        
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        else :
            print("---------------------------------------------------------")
            print(f"Yay! The computer guessed your number {guess} corretly")
    
computer_guess_your_number(10)

