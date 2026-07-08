import time
import os
import sys
import random

class Game:
    def __init__(self):
        self.wallet = 5000
        self.string = "💎🍀🎁✨💰"
        self.ban = False
        self.playing = True
        self.main()
        
    def main(self) -> None:
        """main function"""
        while self.playing:
            time.sleep(2)
            clear_screen()
            if self.wallet == 0:
                print("you are broke! GAME OVER!!")
                clear_and_exit()
            if self.ban and self.wallet >= 100000:
                print("you were falsely charged for cheating and got JAILED for life!!!")
                print("GAMEBLING IS BAD!!")
                clear_and_exit()
            if self.ban:
                print("""You changed your appearance and entered the casino again""")
            if self.wallet >= 100000:
                kick_print()
                clear_and_exit()

            wallet_print(self.wallet)
            print()
            print()
            try:
                bet = int(input("Enter the bet:"))
            except ValueError:
                print("that aint money u gotta type numbers!!")
                playing = self.play_again()
                if playing:
                    continue
                else:
                    clear_and_exit()
            
            if bet > self.wallet:
                print("You can't gamble the $MONEY$ you don't have! ;(")
                playing = self.play_again()
                if playing:
                    continue
                else:
                    clear_and_exit()
        
            lever = input("Type l to move the lever and start the game:").lower()

            clear_screen()
            wallet_print((self.wallet)-bet)
            print()
            print()

            x = random.choice(self.string)
            y = random.choice(self.string)
            z = random.choice(self.string)

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
                self.slots(x, y, z, bet)
                if self.playing:
                    continue
                else:
                    clear_and_exit()
            
            else:
                print("that aint the lever!!")
                x = random.randrange(0,50)
                self.wallet -= bet
                self.lever_events(x, self.wallet, self.ban)#here
                if self.playing:
                    continue
                else:
                    clear_and_exit()


    def slots(self, x, y, z, bet) -> None:
        """slots check and prize"""
        if x == y == z == "💎":

            jackpot_print_and_delay()
            kick_print()
            self.playing = self.play_again()

        elif x == y == z and x in "🍀🎁✨💰":

            self.wallet += bet
            print(f"You won {bet}$!!")
            self.playing = self.play_again()

        else:

            print("you won NOTHING!!")
            self.wallet -= bet
            time.sleep(2)
            self.playing = self.play_again()


    def lever_events(self, x, wallet, ban) ->None:
        """lever events"""
        time.sleep(2)
        if x in (25, 35, 45, 15 , 5):
            print("ohh u just pressed some weird button and the machine gave u 1000$")
            wallet += 1000
            self.playing = True

        elif x in (0, 10, 20, 30, 40):

            machine_break_print()
            time.sleep(2)
            if ban == True:
                
                print("""Your disguise was instantly caught and you were KICKED!!! out "
and got JAILED for life
guess you dont mess with the HOUSE""")
                self.playing = False
                
            else:

                question = input("did u break the machine?(y/n):").lower()
                if question == "y":
                    print("""Nice! atleast you are not lying about it.
were KICKED OUT!! because u didnt have enough money to play
u have 0$ in wallet
GAMER OVER!!""")
                    wallet = 0
                    self.playing = False

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
                    self.playing = False

        elif x == 7:

            print("The machine started working by itself.....")
            jackpot_print_and_delay()
            kick_print()
            ban = True
            self.playing = False
        

    def play_again(self) -> None:
        """plays the slot game again"""
        question = input("do you wanna play again(y/n):").lower()
        if question == "y":
            return True
        else:
            clear_and_exit()

def clear_screen() -> None:
    """Clear terminal by calling this function"""
    os.system("cls" if os.name == "nt" else "clear")

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

def clear_and_exit() -> None:
    """quits"""
    time.sleep(3.5)
    clear_screen()
    sys.exit()

def kick_print() -> None:
    """too much money kick print"""
    print("You were kicked out because you won too much")
    print("I guess the house always wins.....")

def wallet_print(wallet) -> None:
    """prints the wallet"""
    print(f"[wallet:{wallet}$]")


if __name__ == "__main__":
    game = Game()
