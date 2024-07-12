import random

def RPS():
    choice=['Rock', 'Paper', 'Scissors']
    ai=random.choice(choice)

    player=input("choose: paper, rock, scissors: ").lower()
    print(f"I chose {ai}")

    if player==ai:
        print(f"Draw, you both chose {choice}")
    elif    (choice=="Rock" and ai=="scissors") or\
            (choice=="paper" and ai=="rock") or \
            (choice=="scissors" and ai=="paper"):
        print("Congratulations, you won")
    else:
        print("unfortunately you lost")