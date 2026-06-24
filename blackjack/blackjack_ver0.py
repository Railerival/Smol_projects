import random
import os
import time


deck=[{'A':'+---+\n|♥  |\n| A |\n|  ♥|\n+---+',
       '2':'+---+\n|♥  |\n| 2 |\n|  ♥|\n+---+',
       '3':'+---+\n|♥  |\n| 3 |\n|  ♥|\n+---+',
       '4':'+---+\n|♥  |\n| 4 |\n|  ♥|\n+---+',
       '5':'+---+\n|♥  |\n| 5 |\n|  ♥|\n+---+'
    ,'6':'+---+\n|♥  |\n| 6 |\n|  ♥|\n+---+'
    ,'7':'+---+\n|♥  |\n| 7 |\n|  ♥|\n+---+'
    ,'8':'+---+\n|♥  |\n| 8 |\n|  ♥|\n+---+'
    ,'9':'+---+\n|♥  |\n| 9 |\n|  ♥|\n+---+'
    ,'10':'+----+\n|♥  |\n| 10 |\n|  ♥|\n+----+'
    ,'10':'+---+\n|♥  |\n| J |\n|  ♥|\n+---+'
    ,'10':'+---+\n|♥  |\n| Q |\n|  ♥|\n+---+'
    ,'10':'+---+\n|♥  |\n| K |\n|  ♥|\n+---+'}
    ,{'A':'+---+\n|♦  |\n| A |\n|  ♦|\n+---+'
    ,'2':'+---+\n|♦  |\n| 2 |\n|  ♦|\n+---+'
    ,'3':'+---+\n|♦  |\n| 3 |\n|  ♦|\n+---+'
    ,'4':'+---+\n|♦  |\n| 4 |\n|  ♦|\n+---+'
    ,'5':'+---+\n|♦  |\n| 5 |\n|  ♦|\n+---+'
    ,'6':'+---+\n|♦  |\n| 6 |\n|  ♦|\n+---+'
    ,'7':'+---+\n|♦  |\n| 7 |\n|  ♦|\n+---+'
    ,'8':'+---+\n|♦  |\n| 8 |\n|  ♦|\n+---+'
    ,'9':'+---+\n|♦  |\n| 9 |\n|  ♦|\n+---+'
    ,'10':'+----+\n|♦  |\n| 10 |\n|  ♦|\n+----+'
    ,'10':'+---+\n|♦  |\n| J |\n|  ♦|\n+---+'
    ,'10':'+---+\n|♦  |\n| Q |\n|  ♦|\n+---+'
    ,'10':'+---+\n|♦  |\n| K |\n|  ♦|\n+---+'}
    ,{'A':'+---+\n|♠  |\n| A |\n|  ♠|\n+---+'
    ,'2':'+---+\n|♠  |\n| 2 |\n|  ♠|\n+---+'
    ,'3':'+---+\n|♠  |\n| 3 |\n|  ♠|\n+---+'
    ,'4':'+---+\n|♠  |\n| 4 |\n|  ♠|\n+---+'
    ,'5':'+---+\n|♠  |\n| 5 |\n|  ♠|\n+---+'
    ,'6':'+---+\n|♠  |\n| 6 |\n|  ♠|\n+---+'
    ,'7':'+---+\n|♠  |\n| 7 |\n|  ♠|\n+---+'
    ,'8':'+---+\n|♠  |\n| 8 |\n|  ♠|\n+---+'
    ,'9':'+---+\n|♠  |\n| 9 |\n|  ♠|\n+---+'
    ,'10':'+----+\n|♠  |\n| 10 |\n|  ♠|\n+----+'
    ,'10':'+---+\n|♠  |\n| J |\n|  ♠|\n+---+'
    ,'10':'+---+\n|♠  |\n| Q |\n|  ♠|\n+---+'
    ,'10':'+---+\n|♠  |\n| K |\n|  ♠|\n+---+'}
    ,{'A':'+---+\n|♣  |\n| A |\n|  ♣|\n+---+'
    ,'2':'+---+\n|♣  |\n| 2 |\n|  ♣|\n+---+'
    ,'3':'+---+\n|♣  |\n| 3 |\n|  ♣|\n+---+'
    ,'4':'+---+\n|♣  |\n| 4 |\n|  ♣|\n+---+'
    ,'5':'+---+\n|♣  |\n| 5 |\n|  ♣|\n+---+'
    ,'6':'+---+\n|♣  |\n| 6 |\n|  ♣|\n+---+'
    ,'7':'+---+\n|♣  |\n| 7 |\n|  ♣|\n+---+'
    ,'8':'+---+\n|♣  |\n| 8 |\n|  ♣|\n+---+'
    ,'9':'+---+\n|♣  |\n| 9 |\n|  ♣|\n+---+'
    ,'10':'+----+\n|♣  |\n| 10 |\n|  ♣|\n+----+'
    ,'10':'+---+\n|♣  |\n| J |\n|  ♣|\n+---+'
    ,'10':'+---+\n|♣  |\n| Q |\n|  ♣|\n+---+'
    ,'10':'+---+\n|♣  |\n| K |\n|  ♣|\n+---+'}]
dealer_cards=['+---+\n|░░░|\n|░░░|\n|░░░|\n+---+']
player_cards=[]
dealer_numbers=[]
player_numbers=[]
deck_copy = deck.copy()


def clear_screen()->None:
    """Clear terminal by calling this function"""
    os.system("cls" if os.name == "nt" else "clear")
def first_deal()->None:
    """deals the first hand"""
    #dealer logic
    drawn=draw()
    dealer_card_number=drawn[0]
    dealer_card=drawn[1]
    dealer_numbers.append(dealer_card_number)
    dealer_cards.append(dealer_card)
    #player logic
    for i in range(0,2):
        drawn=draw()
        player_card_number=drawn[0]
        player_card=drawn[1]
        player_numbers.append(player_card_number)
        player_cards.append(player_card)
def draw():
    """it draws a random card"""
    
    random_type = random.choice(deck_copy)
    random_key = random.choice(list(random_type))
    random_card = random_type[random_key]
    for ind,element in enumerate(deck_copy):
        if element == random_type:
            ff=ind
            break
    
    del deck_copy[ff][random_key]
    return random_key,random_card
def dealer_hit()->None:
    dealer_sum=0
    drawn=draw()
    dealer_card_number=drawn[0]
    dealer_card=drawn[1]
    dealer_numbers.append(dealer_card_number)
    dealer_cards.append(dealer_card)
    for i in dealer_numbers:
        if i =='A':
            i = 11
            dealer_sum=dealer_sum+i
        else:
            dealer_sum=dealer_sum+int(i)
    if dealer_sum != 21:
        if dealer_sum > 21:
            print("you win")
            playagain()
    elif dealer_sum == 21:
        print("dealer wins")
        playagain()
    dealer_hit() 
def dealer_stand()->None:
    dealer_sum=0
    player_sum=0
    for i in player_numbers:
        if i =='A':
            i = 11
            player_sum = player_sum + i
        else:
            player_sum = player_sum + int(i)
    for i in dealer_numbers:
        if i =='A':
            i = 11
            dealer_sum = dealer_sum + i
        else:
            dealer_sum = dealer_sum + int(i)
    if player_sum>dealer_sum:
        print("you win")
        playagain()
    else:
        print("dealer wins")
        playagain()
def hit()->None:
    """hit logic"""
    player_sum=0
    drawn = draw()
    player_card_number=drawn[0]
    player_card=drawn[1]
    player_numbers.append(player_card_number)
    player_cards.append(player_card)
    clear_screen()
    print(dealer_cards)
    print(player_cards)
    for i in player_numbers:
        if i =='A':
            i = 11
            player_sum = player_sum + i
        else:
            player_sum = player_sum + int(i)
    if not player_sum == 21:
        if player_sum > 21:
            print("you bust")
            playagain()
    elif player_sum == 21:
        print("you win")
        playagain()
    decision()
def stand()->None:
    """stand logic"""
    dealer_sum=0
    drawn=draw()
    player_card_number=drawn[0]
    player_card=drawn[1]
    dealer_cards.pop(0)
    dealer_cards.append(player_card)
    dealer_numbers.append(player_card_number)
    clear_screen()
    print(dealer_cards)
    print(player_cards)
    for i in dealer_numbers:
        if i =='A':
            i = 11
            dealer_sum=dealer_sum+i
        else:
            dealer_sum=dealer_sum+int(i)
    if not dealer_sum == 21:
        if dealer_sum > 21:
            print("you win")
            playagain()
    elif dealer_sum == 21:
        print("dealer wins")
        playagain()
    if dealer_sum>=16:
        dealer_hit()
    else:
        dealer_stand()
def decision()->None:#checked
    """hit or stand decision logic"""
    decision=input("hit or stand(H/S):").lower()
    if decision=='h':
        hit()
    elif decision=='s':
        stand()
    else:
        print("wrong input")
        playagain()
def playagain()->None:
    global dealer_cards
    global player_cards
    global dealer_numbers
    global player_numbers
    global deck_copy
    dealer_cards=['+---+\n|░░░|\n|░░░|\n|░░░|\n+---+']
    player_cards=[]
    dealer_numbers=[]
    player_numbers=[]
    deck_copy = deck.copy()
    x=input("do you want to play again?")
    if x == 'y':
        main()
    else:
        quit()
def main()->None:#checked
    time.sleep(2)
    clear_screen()
    player_sum=0
    #first deal logic
    first_deal()
    print(dealer_cards)
    print(player_cards)
    for i in player_numbers:
        if i =='A':
            i = 11
            player_sum = player_sum + i
        else:
            player_sum = player_sum + int(i)
    if not player_sum == 21:
        if player_sum > 21:
            print("you busted")
            playagain()
    elif player_sum == 21:
        print("you win")
        playagain()
    decision()

main()
    
#some issues that can be fixed:
#1)Ace can be 11 and 1
#2)global usage in playagain function
#3)visual part of cards is a list which needs to be fixed