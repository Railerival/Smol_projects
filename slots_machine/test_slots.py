import time
import os
winning = True
import sys

def clear_screen() -> None:
    """Clear terminal by calling this function"""
    os.system("cls" if os.name == "nt" else "clear")

def game_quit() -> None:
    """quits"""
    time.sleep(4)
    clear_screen()
    sys.exit()

def kick_print():
    """too much money kick print"""
    print("You were kicked out because you won too much")
    print("I guess the house always wins.....")

def wallet_print(wallet) -> None:
    """prints the wallet"""
    print(f"[wallet:{wallet}$]")

def play_again(wallet,ban):
    """plays the slot game again"""
    time.sleep(3)
    clear_screen()
    main(wallet,ban)

def main(wallet,ban):
    time.sleep(1)
    clear_screen()

    if wallet == 0:
        print("you are broke! GAME OVER!!")
        game_quit()
    if ban and wallet >= 100000:
        print("you were falsely charged for cheating and got JAILED for life!!!")
        print("GAMEBLING IS BAD!!")
        game_quit()
    if ban:
        print("""You changed your appearance and entered the casino again""")
    if wallet >= 100000:
        kick_print()
        game_quit()

    try:
        bet = int(input("Enter the bet:"))
    except ValueError:
        print("that aint money u gotta type numbers!!")
        play_again(wallet,ban)
    
    if bet > wallet:
        print("You can't gamble the $MONEY$ you don't have! ;(")
        play_again(wallet,ban)

    lever = input("Type l to move the lever and start the game:").lower()

    clear_screen()
    wallet_print(wallet-bet)
    print()
    print()

main(wallet=5000,ban = False)