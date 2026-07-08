import time
import os
import sys
import random

wallet = 5000
string = "💎🍀🎁✨💰"
ban = False
game_number = [0]

def machine_break_print() -> None:
    """prints the machine break dialogue"""
    print("OHHHH NOOOOOO!!!! the machine broke......")
    time.sleep(2)
    print("a staff came running.....")
    time.sleep(2)
    print("what happened sir....")

def jackpot_print_and_delay()->None:
    """prints the jackpot messages"""
    print("YOU JUST HIT THE JACKPOTTTTTT!!!!!")
    time.sleep(3)

def clear_screen() -> None:
    """Clear terminal by calling this function"""
    os.system("cls" if os.name == "nt" else "clear")

def clear_and_exit() -> None:
    """quits"""
    time.sleep(1.5)
    clear_screen()
    sys.exit()

def kick_print() -> None:
    """too much money kick print"""
    print("You were kicked out because you won too much")
    print("I guess the house always wins.....")

def wallet_print(wallet) -> None:
    """prints the wallet"""
    print(f"[wallet:{wallet}$]")

def play_again(wallet, ban) -> None:
    """plays the slot game again"""
    question = input("do you wanna play again(y/n):").lower()
    if question == "y":
        main(wallet, ban)
    else:
        clear_and_exit()

def slots(x, y, z, wallet, bet) -> None:
    """slots check and prize"""
    if x == y == z == "💎":

        jackpot_print_and_delay()
        kick_print()
        play_again(wallet, ban)

    elif x == y == z and x in "🍀🎁✨💰":

        wallet += bet
        print(f"You won {bet}$!!")
        play_again(wallet, ban)

    else:

        print("you won NOTHING!!")
        wallet -= bet
        time.sleep(2)
        play_again(wallet, ban)

def lever_events(x, wallet, ban) ->None:
    """lever events"""
    time.sleep(2)
    if x in (25, 35, 45, 15 , 5):
        print("ohh u just pressed some weird button and the machine gave u 1000$")
        wallet += 1000

    elif x in (0, 10, 20, 30, 40):

        machine_break_print()
        time.sleep(2)
        if ban == True:
            
            print("""Your disguise was instantly caught and you were KICKED!!! out "
and got JAILED for life
guess you dont mess with the HOUSE""")
            clear_and_exit()
            
        else:

            question = input("did u break the machine?(y/n):").lower()
            if question == "y":
                print("""Nice! atleast you are not lying about it.
You were KICKED OUT!! because u didnt have enough money to play
u have 0$ in wallet
GAMER OVER!!""")
                wallet = 0
                clear_and_exit()

            elif question == "n":

                ban == True
                print("""LIARRR!!!
You were KICKED OUT!! because u didnt have enough money
and you are now BANNED!!!!!!! from the casino to play
u have 0$ in wallet
GAMER OVER!!""") 
                wallet = 0
                clear_and_exit()

            else:

                print("""They didnt listen to your explanation you were KICKED OUT!!
and you are now BANNED!!!!!!! from the casino to play
u have 0$ in wallet
GAMER OVER!!""") 
                ban = True
                wallet = 0
                clear_and_exit()

    elif x == 7:

        print("The machine started working by itself.....")
        jackpot_print_and_delay()
        kick_print()
        ban = True
        clear_and_exit()
    play_again(wallet, ban)

def main(wallet, ban) -> None:
    """main function"""
    game_number[0] += 1
    if game_number[0] > 100:
        print("You played too much, Now u are in year 2300")
        clear_and_exit()
    time.sleep(2)
    clear_screen()

    if wallet == 0:
        print("you are broke! GAME OVER!!")
        clear_and_exit()
    if ban and wallet >= 100000:
        print("you were falsely charged for cheating and got JAILED for life!!!")
        print("GAMEBLING IS BAD!!")
        clear_and_exit()
    if ban:
        print("""You changed your appearance and entered the casino again""")
    if wallet >= 100000:
        kick_print()
        clear_and_exit()

    wallet_print(wallet)
    print()
    print()
    try:
        bet = int(input("Enter the bet:"))
    except ValueError:
        print("that aint money u gotta type numbers!!")
        play_again(wallet, ban)
    
    if bet > wallet:
        print("You can't gamble the $MONEY$ you don't have! ;(")
        play_again(wallet, ban)

    lever = input("Type l to move the lever and start the game:").lower()

    clear_screen()
    wallet_print(wallet-bet)
    print()
    print()

    x = random.choice(string)
    y = random.choice(string)
    z = random.choice(string)

    if lever == "l":

        slot_machine = f"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⣀⣤⣴⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣤⣀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⢸⣿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⣿⡇⠀⠀⣤⣄⠀⠀
        ⠀⠀⠀⠀⠀⠀⢸⣿⠀⢸⣿⣿⡇⢸⣿⣿⡇⢸⣿⣿⡇⠀⣿⡇⠀⠀⠛⠛⠀⠀
        ⠀⠀⠀⠀⠀⠀⢸⣿⠀ {x}  {y}  {z}  ⣿⡇⠀⠀⣷⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⢸⣿⠀⢸⣿⣿⡇⢸⣿⣿⡇⢸⣿⣿⡇⠀⣿⡇⠀⣾⡇⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⢸⣿⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣿⡇⠀⣿⡿⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠙⠃⠀⠀⠀
        ⠀⠀⠀⠀⢀⣴⣿⠟⠛⠛⢻⡿⠛⠛⠛⢻⣿⣿⡟⠋⠉⠉⠛⢿⣦⡀⠀⠀⠀⠀
        ⠀⠀⠀⢰⣿⣿⣥⣤⣤⣤⣾⣧⣤⣤⣤⣿⣿⣿⣷⣦⣤⣤⣶⣿⣿⣿⡆⠀⠀⠀
        ⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
        ⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
        ⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀"""

        print(slot_machine)
        print()
        print()
        slots(x, y, z, wallet, bet)
    
    else:
        print("that aint the lever!!")
        x = random.randrange(0,50)
        wallet -= bet
        lever_events(x, wallet, ban)

if __name__ == "__main__":
    main(wallet, ban)
