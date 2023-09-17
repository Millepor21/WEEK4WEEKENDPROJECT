import random

class BlackJack():

    def __init__(self):
        self.deck = DeckOfCards()

    def deal(self):
        self.deck.draw()
        if sum(self.deck.player_cards_value) == 21:
            return 1
        else:
            return 2
    def is_player_bust(self):
        player_bust = self.deck.check_bust_player()
        if player_bust == 1:
            return 'Bust'
        
    def is_dealer_bust(self):
        dealer_bust = self.deck.check_bust_dealer()
        if dealer_bust == 1:
            return 'Bust'

    def win_con(self):
        if sum(self.deck.player_cards_value) > sum(self.deck.dealer_cards_value) and sum(self.deck.player_cards_value) <= 21 and sum(self.deck.dealer_cards_value) <= 21:
            return print(f'You won with a total of {sum(self.deck.player_cards_value)} while the dealer only had {sum(self.deck.dealer_cards_value)}'), self.deck.print_hands()
        elif sum(self.deck.player_cards_value) < sum(self.deck.dealer_cards_value) and sum(self.deck.player_cards_value) <= 21 and sum(self.deck.dealer_cards_value) <= 21:
            return print(f'You lost with a total of {sum(self.deck.player_cards_value)} while the dealer had {sum(self.deck.dealer_cards_value)}'), self.deck.print_hands()
        elif sum(self.deck.player_cards_value) < sum(self.deck.dealer_cards_value) and sum(self.deck.player_cards_value) <= 21 and sum(self.deck.dealer_cards_value) > 21:
            return print(f'You won with a total of {sum(self.deck.player_cards_value)} because the dealer busted with {sum(self.deck.dealer_cards_value)}'), self.deck.print_hands()
        elif sum(self.deck.player_cards_value) > sum(self.deck.dealer_cards_value) and sum(self.deck.player_cards_value) > 21 and sum(self.deck.dealer_cards_value) <= 21:
            return print(f'The dealer won with a total of {sum(self.deck.dealer_cards_value)} because the player busted with {sum(self.deck.player_cards_value)}'), self.deck.print_hands()
        elif sum(self.deck.player_cards_value) == sum(self.deck.dealer_cards_value) and sum(self.deck.player_cards_value) <= 21:
            return print(f'You both tied with a total of {sum(self.deck.player_cards_value)}'), self.deck.print_hands()
        elif sum(self.deck.player_cards_value) == sum(self.deck.dealer_cards_value) and sum(self.deck.player_cards_value) > 21:
            return print(f'You both busted with a total of {sum(self.deck.player_cards_value)}'), self.deck.print_hands()
        
    def driver(self):
        print('Welcome to Black Jack')
        while True:
            u_choice = input('Would you like to play? [yes] or [no]: ').lower()
            if u_choice == 'no':
                print('Thanks for stopping by the Black Jack table!')
                break
            elif u_choice == 'yes':
                print('The dealer shuffles the cards.\n')
                delt = self.deal()
                if self.is_player_bust() == 'Bust':
                    self.win_con()
                    continue
                if self.is_dealer_bust == 'Bust':
                    self.win_con()
                    continue
                if delt == 1:
                    print(f'You won a Blackjack with a {self.deck.player_cards[0][0]} of {self.deck.player_cards[0][1]} and a {self.deck.player_cards[1][0]} of {self.deck.player_cards[1][1]}\nThe dealer showed a {self.deck.dealer_cards[0][0]} of {self.deck.dealer_cards[0][1]} and a {self.deck.dealer_cards[1][0]} of {self.deck.dealer_cards[1][1]}')
                    continue
                elif delt == 2:
                    print(f'You were dealt a {self.deck.player_cards[0][0]} of {self.deck.player_cards[0][1]} and a {self.deck.player_cards[1][0]} of {self.deck.player_cards[1][1]}\nThe dealer shows a {self.deck.dealer_cards[0][0]} of {self.deck.dealer_cards[0][1]}')
                u_choice_2 = input('Would you like to [hit] or [stand]?: ').lower()
                if u_choice_2 == 'stand':
                    self.win_con()
                elif u_choice_2 == 'hit':
                    hit = self.deck.hit()
                    if hit == 'Bust':
                        self.win_con()
                        continue
                    elif hit == 'Satisfied':
                        self.win_con()
            else:
                print('Please enter either "yes" or "no"')
                continue
class DeckOfCards:
    def __init__(self):
        self.suits = ['Hearts','Diamonds','Spades','Clubs']
        self.ranks = ['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']
        self.values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

    def draw(self):
        self.player_cards = []
        self.player_cards_value = []
        self.dealer_cards = []
        self.dealer_cards_value = []
        for i in range(2):
            self.player_card = [random.choice(self.ranks),random.choice(self.suits)]
            self.player_cards.append(self.player_card)
            self.player_cards_value.append(self.values[self.player_card[0]])
            self.dealer_card = [random.choice(self.ranks),random.choice(self.suits)]
            self.dealer_cards.append(self.dealer_card)
            self.dealer_cards_value.append(self.values[self.dealer_card[0]])
        if sum(self.dealer_cards_value) < 17:
            self.dealer_card = [random.choice(self.ranks),random.choice(self.suits)]
            self.dealer_cards.append(self.dealer_card)
            self.dealer_cards_value.append(self.values[self.dealer_card[0]])

    def hit(self):
        while True:    
            self.player_card = [random.choice(self.ranks),random.choice(self.suits)]
            self.player_cards.append(self.player_card)
            self.player_cards_value.append(self.values[self.player_card[0]])
            if sum(self.player_cards_value) > 21 and self.player_cards_value[-1] == 11:
                self.player_cards_value.pop(-1)
                self.player_cards_value.append(1) 
            print(f'You drew a {self.player_card[0]} of {self.player_card[1]}')
            print('You currently have')
            for card in self.player_cards:
                print(f'{card[0]} of {card[1]}')
            flag = self.check_bust_player()
            if flag == 1:
                return 'Bust'
            u_d = input('Do you want to hit again? [yes] or [no]: ').lower()
            if u_d == 'no':
                return 'Satisfied'
            
    def print_hands(self):
        print('\nYour Hand:')
        for player_card in self.player_cards:
            print(f'{player_card[0]} of {player_card[1]}')
        print('\nDealer\'s Hand:')
        for dealer_card in self.dealer_cards:
            print(f'{dealer_card[0]} of {dealer_card[1]}')

    def check_bust_player(self):
        if sum(self.player_cards_value) > 21:
            return 1
        else:
            return 0
        
    def check_bust_dealer(self):
        if sum(self.dealer_cards_value) > 21:
            return 1
        else:
            return 0

Porter = BlackJack()
Porter.driver()