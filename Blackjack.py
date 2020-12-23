
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit

two_hearts = Card(suits[0],ranks[0])

class Deck:
    
    def __init__(self):
        # Only happens once upon creation of a new Deck
        self.all_cards = [] 
        for suit in suits:
            for rank in ranks:
                # This assumes the Card class has already been defined!
                self.all_cards.append(Card(suit,rank))
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()  

class Player:
    
    def __init__(self,name):
        self.name = name
        # A new player has no cards
        self.all_cards = [] 
        
    def remove_one(self):
        # Note we remove one card from the list of all_cards
        # We state 0 to remove from the "top" of the deck
        # We'll imagine index -1 as the bottom of the deck
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

def hand_value():
    result = 0
    for i in range(len(gambler.all_cards)):
        result += gambler.all_cards[i].value
    return result

def hit():
    gambler.add_cards(new_deck.deal_one())

def bet():
    global chips
    global pot
    amount = int(input(f"How much do you want to bet? Available chips: {chips}\n"))
    chips -= amount
    pot += amount

def decision():
    while True:
        another_card = input("Would you like another card? (yes/no)\n")
        if another_card.lower() == "yes":
            return True
        elif another_card.lower() == "no":
            return False
        else:
            print("Incorrect input!")
            
print("Welcome to BlackJack!")

dealer = Player("Dealer")
player_name = input("Whats your name?: ")
gambler = Player(player_name)

new_deck = Deck()
new_deck.shuffle()

chips = 500
pot = 0
# tomorrow
