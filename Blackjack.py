
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

def hand_value(player):
    result = 0
    for i in range(len(player.all_cards)):
        result += player.all_cards[i].value
    return result

def hit(player):
    player.add_cards(new_deck.deal_one())

chips = 500
pot = 0
def bet():
    global chips
    global pot
    while True:
        amount = int(input(f"How much do you want to bet? Available chips: {chips}\n"))
        if amount <= chips:
            chips -= amount
            break
        else:
            print("You do not have enough chips!")
    pot += amount

def decision():
    while True:
        if hand_value(gambler) <= 21:
            another_card = input("Would you like another card? (yes/no)\n")
            if another_card.lower() == "yes":
                hit(gambler)
                print(gambler.all_cards[-1])
                print(f"Hand value: {hand_value(gambler)}")
            elif another_card.lower() == "no":
                return False
            else:
                print("Incorrect input!")
        else:
            return True

def dealer_turn():
    dealer.all_cards = []
    for i in range(2):
        dealer.add_cards(new_deck.deal_one())
    while hand_value(dealer) < 17:
        hit(dealer)
    return hand_value(dealer)

def game_eval():
    if hand_value(dealer) <= 21 and hand_value(gambler) <= 21:
        if hand_value(dealer) > hand_value(gambler):
            return 0
        elif hand_value(dealer) < hand_value(gambler):
            return 1
        else:
            return 2
    elif hand_value(gambler) > 21:
        return 0
    else:
        return 1

def commentator(arg):
    global pot
    global chips
    print("-"*7+"RESULT"+"-"*7)
    if arg == 0:
        print(f"Dealer's hand value: {hand_value(dealer)}\nYour hand value: {hand_value(gambler)}\n{dealer.name} wins.\nChips removed from pot: {pot}")
        pot = 0
    if arg == 1:
        print(f"Dealer's hand value: {hand_value(dealer)}\nYour hand value: {hand_value(gambler)}\n{gambler.name} wins!\nChips won: {pot*2}")
        chips += pot*2
        pot = 0
    if arg == 2:
        print(f"Dealer's hand value: {hand_value(dealer)}.\nYour hand value: {hand_value(gambler)}.\nDraw.\nChips returned to you: {pot}")
        chips += pot
        pot = 0

def hand_print(player):
    print("-"*10+"HAND"+"-"*10)
    print("Cards:")
    for i in player.all_cards:
        print(i)
    print(f"Hand value: {hand_value(player)}")

print("Welcome to BlackJack!")

dealer = Player("Dealer")
player_name = input("Whats your name?: ")
gambler = Player(player_name)

new_deck = Deck()
new_deck.shuffle()

game_on = True

while game_on == True:
    gambler.all_cards = []
    print("-"*10+"BET"+"-"*10)
    bet()
    print(f"Pot: {pot}")
    for i in range(2):
        gambler.add_cards(new_deck.deal_one())

    hand_print(gambler)
    over21 = decision()

    if over21 == False:
        print("-"*7+"DEALER TURN"+"-"*6)
        dealer_turn()
        hand_print(dealer)

        commentator(game_eval())
    else:
        print("-"*7+"RESULT"+"-"*7)
        print(f"Your hand value: {hand_value(gambler)}\n{dealer.name} wins.\nChips removed from pot: {pot}")
        pot = 0
    
    print("-"*7+"GAME ON?"+"-"*7)
    print(f"Available chips: {chips}")
    game_off = input("Press 1 if you wish to continue gambling.\nPress 2 if you wish to cash out.\n")
    if game_off == "2":
        game_on = False
print(f"Here's your imaginary {chips} chips. Buy yourself something nice!")