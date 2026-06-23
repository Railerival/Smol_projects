import random 
import os 
import time

class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} of {self.suit}'
    
    def __repr__(self):
        return f"{self.rank},{self.suit}"

class Deck:

    SUITS = ("♣", "♦", "♥", "♠")
    RANKS = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

    def __init__(self):
        self.cards = self.card_creation()

    def card_creation(self):
        cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                cards.append(card)
        return cards

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Hand:

    def __init__(self):
        self.card_hand = []
    def add_card(self,deck):
        self.card_hand.append(deck.deal())
    def rem_card(self):
        self.card_hand.pop()
    def empty_hand(self):
        self.card_hand = []
    def check_card(self,card):
        for i in self.card_hand:
            if card in self.card_hand:
                print("yes! u have the card")
            else:
                print("no that card aint in your hand")
    def card_count(self):
        print("no.of cards:",str(len(self.card_hand)))
         

def Clear_screen() -> None:
    
    """Clear terminal by calling this function"""
    os.system("cls" if os.name == "nt" else "clear")

def Decision():
    """nothing here"""
def Display(hand):
    """gg"""
    


def Main():
    """gg"""
    time.sleep(2)
    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()
    for i in range(2):
        player_hand.add_card(deck)
        dealer_hand.add_card(deck)
    print("(╯°□°)╯︵ ┻━┻ Dealer cards")
    Display(dealer_hand)
    print("┬─┬ノ( º _ ºノ) player cards")
    Display(player_hand)
    Decision()
    
    


    

if __name__ == "__main__":
    Main()