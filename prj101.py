import random 

up = 0
cp = 0
while True:
    ch = random.choice(['rock', 'paper','scissors'])
    us = input("Your Move: ")

    if us == 'q':
        break

    if us.lower() != ch:
        if (us.lower() == 'rock' and ch == 'paper') or (us.lower() == 'scissors' and ch == 'rock') or (us.lower() == 'paper' and ch == 'scissors'):
            print(f"Computer's Move: {ch}")
            cp += 1
        else:
            print(f"Computer's Move: {ch}")
            up += 1
    else:
        print(f"""Computer's Move: {ch}
No Points.""")      
    
    print(f"""User Points: {up}
Computer Points: {cp}""")
    print("*" * 50)
    if cp == 5:
        print("Computer Wins")
        break
    elif up == 5:
        print("User Wins")
        break