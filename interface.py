from RPS import RPS
from Snake import start_game
from TTT import start_tic_tac_toe
from Breakout import start_breakout

def interface():
    nick = input("Enter your nickname: ")
    print(f"Hi, {nick}!")
    print("Choose your option:")
    print("1. Rock, Paper, Scissors")
    print("2. Snake")
    print("3. Tic-Tac-Toe")
    print("4. Breakout")

    choice = input("Select the game you want to play (1, 2, 3 or 4): ")

    if choice == '1':
        print("Starting Rock, Paper, Scissors...")
        RPS()
    elif choice == '2':
        print("Starting Snake...")
        start_game()
    elif choice == '3':
        print("Starting Tic-Tac-Toe...")
        start_tic_tac_toe()
    elif choice == '4':
        print("Starting Breakout...")
        start_breakout()
    else:
        print("Invalid choice")
        interface()

interface()
