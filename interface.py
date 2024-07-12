from RPS import RPS
from Snake import start_game

def interface():
    nick = input("Enter your nickname: ")
    print(f"Hi, {nick}!")
    print("Choose your option:")
    print("1. Rock, Paper, Scissors")
    print("2. Snake")

    choice = input("Select the game you want to play (1 or 2): ")

    if choice == '1':
        print("Starting Rock, Paper, Scissors...")
        RPS()
    elif choice == '2':
        print("Starting Snake...")
        start_game()
    else:
        print("Invalid choice. Please select 1 or 2.")
        interface()
