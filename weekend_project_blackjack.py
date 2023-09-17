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
    def bust(self):
        player_bust = self.deck.check_bust_player()
        if player_bust == 1:
            return 'Bust'
    def win_con(self):
        if sum(self.deck.player_cards_value) > sum(self.deck.dealer_cards_value) and sum(self.deck.player_cards_value) <= 21:
            return f'You won with a total of {sum(self.deck.player_cards_value)} while the dealer only had {sum(self.deck.dealer_cards_value)}'
        elif sum(self.deck.player_cards_value) < sum(self.deck.dealer_cards_value) and sum(self.deck.player_cards_value) <= 21:
            return f'You lost with a total of {sum(self.deck.player_cards_value)} while the dealer had {sum(self.deck.dealer_cards_value)}'
    def driver(self):
        print('Welcome to Black Jack')
        while True:
            u_choice = input('Would you like to play? [yes] or [no]: ').lower()
            if u_choice == 'no':
                print('Thanks for stopping by the Black Jack table!')
                break
            elif u_choice == 'yes':
                print('The dealer shuffles the cards.')
                delt = self.deal()
                if delt == 1:
                    print(f'You won a Blackjack with a {self.deck.player_cards[0][0]} of {self.deck.player_cards[0][1]} and a {self.deck.player_cards[1][0]} of {self.deck.player_cards[1][1]}\nThe dealer showed a {self.deck.dealer_cards[0][0]} of {self.deck.dealer_cards[0][1]}')
                    continue
                elif delt == 2:
                    print(f'You were dealt a {self.deck.player_cards[0][0]} of {self.deck.player_cards[0][1]} and a {self.deck.player_cards[1][0]} of {self.deck.player_cards[1][1]}\nThe dealer shows a {self.deck.dealer_cards[0][0]} of {self.deck.dealer_cards[0][1]}')
                u_choice_2 = input('Would you like to [hit] or [stand]?: ').lower()
                if u_choice_2 == 'stand':
                    print(self.win_con())
                elif u_choice_2 == 'hit':
                    hit = self.deck.hit()
                    if hit == 'Bust':
                        continue
                    elif hit == 'Satisfied':
                        print(self.win_con())
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
    def hit(self):
        while True:    
            self.player_card = [random.choice(self.ranks),random.choice(self.suits)]
            self.player_cards.append(self.player_card)
            self.player_cards_value.append(self.values[self.player_card[0]])
            print(f'You drew a {self.player_card[0]} of {self.player_card[1]}')
            print('You currently have')
            for card in self.player_cards:
                print(f'{card[0]} of {card[1]}')
            flag = self.check_bust_player()
            if flag == False:
                print('You hit and busted. You Lose...')
                return 'Bust'
            u_d = input('Do you want to hit again? [yes] or [no]: ').lower()
            if u_d == 'no':
                return 'Satisfied'

    def stand(self):
        pass
        
    def check_bust_player(self):
        player_count = 0
        for num in self.player_cards_value:
            player_count += num
        if player_count > 21:
            return False
        else:
            return True
        
        

Porter = BlackJack()
Porter.driver()