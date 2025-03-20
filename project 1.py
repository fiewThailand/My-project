import random

def roll():
    roll = random.randint(1,6)
    return roll

while True: # while True : จะรันไปเรื่อยๆจนกว่าจะมีคำสั่ง break
    players = input("Enter the number of players (2-4):") #ให้คนเล่นบอกจำนวนคนเล่น
    if players.isdigit(): #เช็คว่าที่คนเล่นบอกมาว่าเป็นตัวเลขไหม ถ้าใช่รันต่อ
        players = int(players) #แปลงข้อมูลเป็นตัวเลข
        if 2 <= players <= 4: #ถ้าตัวเลขตรงตามเงื่อนไข ถ้าใช่รันต่อ
            break
        else: 
            print("Must be between 2 - 4 players.") 
    else: #ถ้าไม่ใช่บอกให้ลองใหม่
        print("Invalid,try again")

max_score = 50
players_scores = [0 for _ in range(players)] # สร้างลำดับคะแนนตามจำนวนผู้เล่นโดยใส่คะแนน 0

while max(players_scores) <= max_score : #จะทำงานจนกว่าจะมากกว่าหรือเท่ากับ 50
    for players_index in range(players): #สำหรับตัวแปร players_index จะสร้างระยะตามจำนวนตัวแปร players
        print("\nPlayer number",players_index + 1,"turn has just started!") #\n คือ ขึ้นบรรทัดใหม่ 
        print("Your total score is:",players_scores[players_index]) #บอกคะแนนที่อ้างอิงลำดับผู้เล่นจากplayers_index #รู้ได้ไงว่าต้องระบุของคนไหน?
        current_score = 0 #สร้างตัวแปรใหม่มาเก็บค่าคะแนน

        while True :
            just_roll = input("Would you like to roll (y)?") #สร้างตัวแปรใหม่มาเก็บข้อมูลอินพุด
            if just_roll != "y":
                break
            value = roll()
            if value == 1:
                print("You rolled 1! Turn done!")
                break
        
    break