import random 
import os 
import sys
import time

def clear_screen() -> None:
    """Clear terminal by calling this function"""
    os.system("cls" if os.name == "nt" else "clear")

def sum_hand(hand) -> int:
    """returns sum of cards in a hand"""
    sum_ranks = 0
    for card in hand:
        rank = card.rank
        if rank == "A":
            sum_ranks = sum_ranks + 11
        elif rank in "JQK":
            sum_ranks = sum_ranks + 10
        else:
            sum_ranks = sum_ranks + int(rank)
    return sum_ranks

def cards_print(hand, reversed) -> None:
    """printing cards in a hand"""
    suitlist1 = []
    suit_list2 = []
    rank_list = []
    length = len(hand)
    print_block = "+---+"*length
    if reversed:
        suitlist1.append(f"|?  |")
        suit_list2.append(f"|  ?|")
        rank_list.append(f"| ? |")
        print(print_block)
        print("|?  |"*length)
        print("| ? |"*length)
        print("|  ?|"*length)
        print(print_block)
    else:
        for card in hand:
            suitlist1.append(f"|{card.suit}  |")
            suit_list2.append(f"|  {card.suit}|")
            rank_list.append(f"| {card.rank:<2}|")
        print(print_block)
        print("".join(suitlist1))
        print("".join(rank_list))
        print("".join(suit_list2))
        print(print_block)

class Card:

    def __init__(self, rank, suit) -> None:
        """holds the cards attributes"""
        self.rank = rank
        self.suit = suit

    def __str__(self) -> str:
        """returns the str version of the object"""
        return f'{self.rank} of {self.suit}'
    
    def __repr__(self) -> str:
        """returns the display of the object for the developer"""
        return f"Card({self.rank},{self.suit})"
    
    def __eq__(self,other) -> bool:
        """checks if 2 card objects are equal"""
        return (self.card, other.suite) == (other.card, other.suite)

class Deck:

    SUITS = ("♣", "♦", "♥", "♠")
    RANKS = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

    def __init__(self) -> None:
        """calls the card_creation method to create the deck"""
        self.deck= self.card_creation()

    def card_creation(self) -> Card:
        """creates the deck"""
        self.cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self.cards.append(card)
        return self.cards

    def shuffle(self) -> None:
        """shuffles the deck"""
        random.shuffle(self.cards)

    def deal(self) -> Card:
        """deals a card from the deck"""
        self.shuffle()
        return self.cards.pop()

class Hand:

    def __init__(self) -> None:
        """has the attribute that is hand of cards"""
        self.card_hand = []

    def add_card(self,card) -> None:
        """adds a new card to the hand"""
        self.card_hand.append(card)

    def rem_card(self,card) -> Card:
        """removes cards from the hand and returns it"""
        index = self.card_hand.index(card)
        card = self.card_hand.pop(index)
        return card
    
    def empty_hand(self) -> None:
        """empties the hand"""
        self.card_hand.clear()

    def check_card(self,card) -> None:
        """checks if a certain card is in hand"""
        for _ in self.card_hand:
            if card in self.card_hand:
                print("yes! u have the card")
            else:
                print("no that card aint in your hand")

    def card_count(self) -> None:
        """prints the card count in the hand"""
        print("no.of cards:"+str(len(self.card_hand)))

class Game:

    def __init__(self)->None:
        """has game_number = 0 attribute which represents the first game"""
        self.game_number = 0

    def play(self) -> None:
        """main function"""
        if self.game_number != 0:
            question = input("Do you want to play the game again?(y/n):")
            if question != "y" or self.game_number > 100: #game_number controls recursion and asks the question
                clear_screen()
                sys.exit()
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.game_number += 1
        time.sleep(2)
        clear_screen()
        for i in range(0,2):
            card = self.deck.deal()
            self.player_hand.add_card(card)
            card = self.deck.deal()
            self.dealer_hand.add_card(card)
        print("(╯°□°)╯︵ ┻━┻ Dealer cards")
        cards_print(self.dealer_hand.card_hand,reversed = 1)
        print("┬─┬ノ( º _ ºノ) player cards")
        cards_print(self.player_hand.card_hand,reversed = 0)
        player_sum = sum_hand(self.player_hand.card_hand)
        if player_sum > 21:
            for letter in "YOU BUSTED!":
                print(letter, end="" ,flush = True)
                time.sleep(0.1)
            print()
            self.play()
        elif player_sum == 21:
            for letter in "BLACKJACKKKK!!!":
                print(letter, end="" ,flush = True)
                time.sleep(0.1)
            print()
            self.play()
        self.decision()

    def decision(self) -> None:
        """hit or stand decision logic"""
        decision = input("hit or stand(H/S):").lower()
        if decision == "h":
            self.hit()
        elif decision == "s":
            self.stand()
        else:
            print("you can only do hit or stand, Game Over!!")
            self.play()

    def hit(self) -> None:
        """Hit logic"""
        card = self.deck.deal()
        self.player_hand.card_hand.append(card)
        self.table_print()
        player_sum = sum_hand(self.player_hand.card_hand)
        if player_sum > 21:
            for letter in "YOU BUST!":
                print(letter, end="" ,flush = True)
                time.sleep(0.1)
            print()
            self.play()
        elif player_sum == 21:
            for letter in "YOU WIN!!!":
                print(letter, end="" ,flush = True)
                time.sleep(0.1)
            print()
            self.play()
        self.decision()

    def stand(self) -> None:
        """Stand logic"""
        self.table_print()
        dealer_sum = sum_hand(self.dealer_hand.card_hand)
        player_sum = sum_hand(self.player_hand.card_hand)
        if dealer_sum > 21:
            for c in "DEALER BUSTED,YOU WIN!!!":
                print(c, end="" ,flush = True)
                time.sleep(0.1)
            print()
            self.play()
        elif dealer_sum == 21:
            for c in "DEALER WINS!":
                print(c, end="" ,flush = True)
                time.sleep(0.1)
            print()
            self.play()

        if dealer_sum <= 16 and player_sum > dealer_sum:
            self.dealer_hit()
        else:
            self.dealer_stand()

    def dealer_hit(self) -> None:
        """Dealer hit logic"""
        card = self.deck.deal()
        self.dealer_hand.card_hand.append(card)
        self.table_print()
        dealer_sum = sum_hand(self.dealer_hand.card_hand)
        if dealer_sum > 21:
            for letter in "DEALER BUSTED,YOU WIN!!!":
                print(letter, end="" ,flush = True)
                time.sleep(0.1)
            print()
            self.play()
        elif dealer_sum == 21:
            for letter in "DEALER WINS!":
                print(letter, end="" ,flush = True)
                time.sleep(0.1)
            print()
            self.play()

        self.dealer_hit()

    def dealer_stand(self) -> None:
        """Dealer stand logic"""
        dealer_sum = sum_hand(self.dealer_hand.card_hand)
        player_sum = sum_hand(self.player_hand.card_hand)
        self.table_print()
        if player_sum > dealer_sum:
            for letter in "YOU WIN!!!":
                print(letter, end="" ,flush = True)
                time.sleep(0.1)
            print()
            self.play()
        elif player_sum < dealer_sum:
            for letter in "DEALER WINS!":
                print(letter, end="" ,flush = True)
                time.sleep(0.1)
            print()
            self.play()
        elif player_sum == dealer_sum:
            for letter in "DRAW!":
                print(letter, end="" ,flush = True)
                time.sleep(0.1)
            print()
            self.play()
    def table_print(self) -> None:
        """clears the terminal and prints the game table"""
        clear_screen()
        print("(╯°□°)╯︵ ┻━┻ Dealer cards")
        cards_print(self.dealer_hand.card_hand,reversed = 0)
        print("┬─┬ノ( º _ ºノ) player cards")
        cards_print(self.player_hand.card_hand,reversed = 0)


if __name__ == "__main__":
    game = Game()
    game.play()