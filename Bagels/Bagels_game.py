x="""Bagels, a deductive logic game
I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say: That means:
    Pico One digit is correct but in the wrong position.
    Fermi One digit is correct and in the right position.
    Bagels No digit is correct.
I have thought up a number.
You have 10 guesses to get it."""
random_number:str
#######################
import random
import os
import time
#######################

def clear_screen()->None:
    """Clear terminal by calling this function"""
    os.system("cls" if os.name == "nt" else "clear")

def randy()->None:
   global random_number
   random_integer = random.randint(0, 999)
   random_number = f"{random_integer:0>3}"
        

def right_guess(number)->bool:
    """checks if user guess is right"""
    return random_number == number
     
def bagels(number)->bool:#works
    """checks if bagels and returns True if bagels else False"""
    count=0
    for i in range(0,3):
        for j in range(0,3):
            count += random_number[i] == number[j]
    if count==0:
        print("Bagels")
        return True
    return False
def game_end()->bool:
    """game over! logic"""
    z=input("Do you want to play again? (yes or no)")
    if z == "yes":
        main()
    elif z=="no":
        clear_screen()
        print("Thanks for playing!")
        return True

def fp(number)->None:
    """Prints the fermi pico logic"""
    fermi_count=0
    pico_count=0
    for i in range(0,3):
        if random_number[i]==number[i]:
            fermi_count=fermi_count+1
    for r in range(0,3):
        for s in range(0,3):
            if random_number[r]==number[s]:
                pico_count=pico_count+1
    if fermi_count == 2:
        pico_count=0
        print("fermifermi")
    elif fermi_count == 1:
        pico_count=pico_count-1
        print("fermi","pico"*pico_count)
    else:
        print("pico"*pico_count)
        
def main()->None:
    """Main game function"""
    clear_screen()
    time.sleep(2)#added a small delay because clear_screen was messing with the print(x) line
    v=0
    print(x)
    while True:
        random_number=randy()
        for v in range(1,11):
            number=input(f"Guess #{v}:")
            number=f"{number:0>3}"
            if right_guess(number):
                print("You guessed it")
                if game_end():
                    break
            else:
                if v == 10:
                    print("Game over! You are out of chances")
                    if game_end():
                        break
                else:
                    if bagels(number):
                        continue
                    fp(number)
                    continue
        break
main()








            

            
        
    


    
                





    
