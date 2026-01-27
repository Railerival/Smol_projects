import random
import os
import time

SUITS = ("♣", "♦", "♥", "♠")
RANKS = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
deck = []
DECK = [(suit,rank) for suit in SUITS for rank in RANKS]

def sumsum(x) -> int:
    """Player sum logic"""
    sum_list = []
    ps = 0

    for i in x:
        rank = i[1]
        sum_list.append(rank)
    for i in sum_list:
        if i == "A":
            ps = ps + 11
        elif i == "J" or i == "Q" or i == "K":
            ps = ps + 10
        else:
            ps = ps + int(i)

    s = ace(sum_list)
    while ps >= 21 and s > 0:
        ps -= 10
        s -= 1
    return ps

def draw(deck_copy) -> tuple:
    """DRAWS A CARD"""
    card = random.choice(deck_copy)
    deck_copy.remove(card)
    return card

def clear_screen() -> None:
    """Clear terminal by calling this function"""
    os.system("cls" if os.name == "nt" else "clear")

def ace(x):
    sum = 0
    for i in x:
        if "A" in i:
            sum = sum + 1
    return sum

def first_deal(deck_copy,dealer_cards,player_cards) -> None:
    """First deal logic"""
    dealer_cards.append(("?","?"))
    dealer_cards.append(draw(deck_copy))
    player_cards.append(draw(deck_copy))
    player_cards.append(draw(deck_copy))

def cards_print(list,dealer_cards,player_cards) -> None:
    """Cards print logic"""
    suitlist1 = []
    suit_list2 = []
    rank_list = []
    length = len(list)
    if list == dealer_cards:
        print("(╯°□°)╯︵ ┻━┻ Dealer cards")
    elif list == player_cards:
        print("┬─┬ノ( º _ ºノ) player cards")
    for i in list:
        suit = i[0]
        rank = i[1]
        suitlist1.append(f"|{suit}  |")
        suit_list2.append(f"|  {suit}|")
        rank_list.append(f"| {rank:<2}|")
    print("+---+"*length)
    print("".join(suitlist1))
    print("".join(rank_list))
    print("".join(suit_list2))
    print("+---+"*length)

def hit(deck_copy,dealer_cards,player_cards) -> None:
    """Hit logic"""
    player_cards.append(draw(deck_copy))
    clear_screen()
    cards_print(dealer_cards,dealer_cards,player_cards)
    cards_print(player_cards,dealer_cards,player_cards)

    ps = sumsum(player_cards)
    if ps > 21:
        for c in "YOU BUST!":
            print(c, end="")
            time.sleep(0.1)
        print()
        playagain(deck_copy,dealer_cards,player_cards)
    elif ps == 21:
        for c in "YOU WIN!!!":
            print(c, end="")
            time.sleep(0.1)
        print()
        playagain(deck_copy,dealer_cards,player_cards)

    decision(deck_copy,dealer_cards,player_cards)

def stand(deck_copy,dealer_cards,player_cards) -> None:
    """Stand logic"""
    dealer_cards.pop(0)
    dealer_cards.append(draw(deck_copy))
    clear_screen()
    cards_print(dealer_cards,dealer_cards,player_cards)
    cards_print(player_cards,dealer_cards,player_cards)

    ds = sumsum(dealer_cards)
    ps = sumsum(player_cards)
    if ds > 21:
        for c in "DEALER BUSTED,YOU WIN!!!":
            print(c, end="")
            time.sleep(0.1)
        print()
        playagain(deck_copy,dealer_cards,player_cards)
    elif ds == 21:
        for c in "DEALER WINS!":
            print(c, end="")
            time.sleep(0.1)
        print()
        playagain(deck_copy,dealer_cards,player_cards)

    if ds <= 16 and ps > ds:
        dealer_hit(deck_copy,dealer_cards,player_cards)
    else:
        dealer_stand(deck_copy,dealer_cards,player_cards)

def dealer_hit(deck_copy,dealer_cards,player_cards) -> None:
    """Dealer hit logic"""
    dealer_cards.append(draw(deck_copy))
    clear_screen()
    cards_print(dealer_cards,dealer_cards,player_cards)
    cards_print(player_cards,dealer_cards,player_cards)

    ds = sumsum(dealer_cards)
    if ds > 21:
        for c in "DEALER BUSTED,YOU WIN!!!":
            print(c, end="")
            time.sleep(0.1)
        print()
        playagain(deck_copy,dealer_cards,player_cards)
    elif ds == 21:
        for c in "DEALER WINS!":
            print(c, end="")
            time.sleep(0.1)
        print()
        playagain(deck_copy,dealer_cards,player_cards)

    dealer_hit(deck_copy,dealer_cards,player_cards)

def dealer_stand(deck_copy,dealer_cards,player_cards) -> None:
    """Dealer stand logic"""
    ds = sumsum(dealer_cards)
    ps = sumsum(player_cards)
    clear_screen()
    cards_print(dealer_cards,dealer_cards,player_cards)
    cards_print(player_cards,dealer_cards,player_cards)

    if ps > ds:
        for c in "YOU WIN!!!":
            print(c, end="")
            time.sleep(0.1)
        print()
        playagain(deck_copy,dealer_cards,player_cards)
    elif ps < ds:
        for c in "DEALER WINS!":
            print(c, end="")
            time.sleep(0.1)
        print()
        playagain(deck_copy,dealer_cards,player_cards)
    elif ps == ds:
        for c in "DRAW!":
            print(c, end="")
            time.sleep(0.1)
        print()
        playagain(deck_copy,dealer_cards,player_cards)

def decision(deck_copy,dealer_cards,player_cards) -> None:
    """hit or stand decision logic"""

    decision = input("hit or stand(H/S):").lower()

    if decision == "h":
        hit(deck_copy,dealer_cards,player_cards)
    elif decision == "s":
        stand(deck_copy,dealer_cards,player_cards)
    else:
        print("wrong input")
        playagain(deck_copy,dealer_cards,player_cards)

def playagain(deck_copy,dealer_cards,player_cards)->None:
    dealer_cards.clear()
    player_cards.clear()
    deck_copy = []
    deck_copy = deck.copy()
    x=input("do you want to play again?(y)").lower()
    if x == 'y':
        main()
    else:
        quit() 


def main():
    dealer_cards = []
    player_cards = []
    deck_copy = DECK.copy()
    time.sleep(2)
    clear_screen()
    #first deal logic
    first_deal(deck_copy,dealer_cards,player_cards)
    cards_print(dealer_cards,dealer_cards,player_cards)
    cards_print(player_cards,dealer_cards,player_cards)

    ps = sumsum(player_cards)
    if ps > 21:
        for c in "YOU BUSTED!":
            print(c, end="")
            time.sleep(0.1)
        print()
        playagain(deck_copy,dealer_cards,player_cards)
    elif ps == 21:
        for c in "BLACKJACKKKK!!!":
            print(c, end="")
            time.sleep(0.1)
        print()
        playagain(deck_copy,dealer_cards,player_cards)

    decision(deck_copy,dealer_cards,player_cards)



if __name__ == "__main__":
    main()