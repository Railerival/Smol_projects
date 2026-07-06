import random
import os
import time
import sys

wallet = 5000
string = "💎🍀🎁✨💰"
winning = True
ban = False

def machine_break_print():
    """prints the machine break dialogue"""
    print("OHHHH NOOOOOO!!!! the machine broke......")
    time.sleep(2)
    print("a staff came running.....")
    time.sleep(2)
    print("what happened sir....")

def jackpot_print()->None:
    """prints the jackpot messages"""
    print("YOU JUST HIT THE JACKPOTTTTTT!!!!!")
    time.sleep(3)

def kick_print():
    """too much money kick print"""
    print("You were kicked out because you won too much")
    print("I guess the house always wins.....")

def wallet_print(wallet) -> None:
    """prints the wallet"""
    print(f"[wallet:{wallet}$]")

def clear_screen() -> None:
    """Clear terminal by calling this function"""
    os.system("cls" if os.name == "nt" else "clear")

def game_quit() -> None:
    """4 second delay,clear screen and quits"""
    time.sleep(4)
    clear_screen()
    sys.exit()
    

def main(wallet,ban):
    time.sleep(2)
    clear_screen()
    if wallet == 0:
        
        print("you are broke! GAME OVER!!")
        game_quit()

    if ban and wallet >= 100000:

        print("you were falsely charged for cheating and got JAILED for life!!!")
        print("GAMEBLING IS BAD")
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
        time.sleep(3)
        clear_screen()
        main(wallet,ban)
    
    if bet > wallet:

        print("You can't gamble the $MONEY$ you don't have! ;(")
        main(wallet,ban)

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

        if x == y == z == "💎":

            jackpot_print()
            kick_print()
            break

        elif x == y == z and x in "🍀🎁✨💰":

            wallet += bet
            print(f"You won {bet}$!!")
            question = input("do you wanna play again(y/n):").lower()
            if question == "y":

                continue
            else:

                print("thanks for playing")
                break
        else:

            print("you won NOTHING!!")
            wallet -= bet
            time.sleep(2)
            question = input("do you wanna play again(y/n):").lower()

            if question == "y":
                
                continue

            else:

                print(f"thanks for playing, you have {wallet}$ in your wallet")
                break
    else:

        print("that aint the lever!!")
        x = random.randrange(0,50)
        wallet -= bet
        
        if x in (25, 35, 45, 15 , 5):

            clear_screen()
            print("ohh u just pressed some weird button and the machine gave u 1000$")
            wallet += 1000

        elif x in (0, 10, 20, 30, 40):

            machine_break_print()
            time.sleep(5)
            clear_screen()

            if ban == True:
                print("""Your disguise was caught and you were instantly KICKED!!! out "
                and got JAILED for life
                guess you dont mess with the HOUSE""")
                
            else:
                time.sleep(1)
                question = input("did u break the machine?(y/n):").lower()
                if question == "y":

                    print("""Nice! atleast you are not lying about it.
                    You were KICKED OUT!! because u didnt have enough money to pay
                    u have 0$ in wallet""")
                    wallet = 0
                    break

                elif question == "n":

                    ban == True
                    print("""LIARRR!!!
                    You were KICKED OUT!! because u didnt have enough money
                    and you are now BANNED!!!!!!! from the casino to pay
                    and now u have 0$ in wallet""") 
                    wallet = 0
                    break

                else:

                    print("""They didnt listen to your explanation you were KICKED OUT!!
                    and you are now BANNED!!!!!!! from the casino to pay
                    and now u have 0$ in wallet""")
                    ban = True
                    wallet = 0
                    break

        elif x == 7:

            clear_screen()
            print("The machine started working by itself.....")
            jackpot_print()
            kick_print()
            ban = True
            break
        time.sleep(2)
        continue

time.sleep(4)
clear_screen()