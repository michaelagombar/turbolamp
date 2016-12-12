import random
import sys

CARDS = ('1','2','3','4','5','6','7','8','9','10','10','10','10')
SUIT = ('S','H','C','D')
RANK = {'A':1, '2':2, '3': 3, '4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}

class Card:
    def __init__(self, suit, rank):
        if (suit in SUIT) and (rank in RANK):
            self.suit = suit #initializes suit
            self.rank = rank #initializes rank


    def __str__(self):
        return self.rank + self.suit #creates a card

    def get_suit(self):
            return self.suit #pulls suit

    def get_rank(self):
            return self.rank #pulls rank

class Hand:

    def __init__(self):
        self.card = [] #empty list to be appended

    def __str__(self):
        result =""
        for card in self.card: #iterates through self.cards
            result += " " + card.__str__() #prints result, essentially

        return "The hand is this: " + result

    def add_card(self, card):
        self.card.append(card) #adds card to empty



        #return value
    def get_value(self):
        value = 0
        contains_ace = False

        for card in self.card:
            rank = card.get_rank()
            value += RANK[rank]

            if(rank =='A'):
                contains_ace = True

        if(value < 11 and contains_ace):
            value += 10

        return value

class Deck:
    def __init__(self):
        self.card = []

        for suit in SUIT:
            for rank in RANK:
                self.card.append(Card(suit, rank)) #adds ALL instances of the cards

    def __str__(self):
        result = ""
        for card in self.card:
            result += " " + card.__str__() #returns a card

        return "Deck contains: " + result

    def shuffle(self):
        random.shuffle(self.card) #shuffles, simply

    def deal_card(self):
        return self.card.pop(0) #deals each card

def hit():

    def new_game_not():
        new_game = input(print("do you want to play again? y/n"))
        if new_game == 'y':
            deal()
        else:
            sys.exit()

    def show_player_hand():
        print("Player 1: %s" % player_hand)
        print("The value of player 1's hand is: %s" % player_hand.get_value())

    def show_dealer_hand():
        print("Dealer: %s" % dealer_hand)
        print("The value of dealer's hand is: %s" % dealer_hand.get_value())

    c = 'y'

    while dealer_hand.get_value() < 17:
        dealer_hand.add_card(deck.deal_card())
        if dealer_hand.get_value() > 21:
            print("You win! Dealer Busts!")
            show_dealer_hand()
            new_game_not()

    while c != 'q':

        c = input(print("Does Player 1  want to hit? y/n"))


        if c == 'y':
            player_hand.add_card(deck.deal_card())
            show_player_hand()

            if player_hand.get_value() > 21:
                print("BUST! You Lose man")
                new_game_not()
        elif c == 'n':
            show_player_hand()
            show_dealer_hand()
            if player_hand.get_value() > dealer_hand.get_value():
                print("YOU WIN!!!!!!")
                new_game_not()
            elif player_hand.get_value() == dealer_hand.get_value():
                print("It's a tie!")
                new_game_not()
            else:
                print("YOU LOSE!!!!")
                new_game_not()


def deal():

    global player_hand #allows these variables to be called in hit function
    global dealer_hand
    global deck

    deck = Deck() #initialize deck
    deck.shuffle() #shuffles the deck

    player_hand = Hand() #initializes players hand
    dealer_hand = Hand()

    player_hand.add_card(deck.deal_card()) #this adds two cards as the initial deal
    player_hand.add_card(deck.deal_card())

    dealer_hand.add_card(deck.deal_card()) #this adds two cards as the intial deal
    dealer_hand.add_card(deck.deal_card())

    print("Player 1: %s" % player_hand) #this simply prints out the car
    print("Player 1 value: %s" % player_hand.get_value())
    print("Dealer: %s" % dealer_hand)
    print("Dealer value: %s" % dealer_hand.get_value())

    hit()


print(deal())


