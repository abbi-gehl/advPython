# Abigail Gehlbach Lab 02 Go Fish
import random


class Card:
    # Card class creates a card object which has a suit and value
    # str and eq functions are overrided to simplify functionality of the program
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return self.value > other.value

    def __str__(self):
        return f'{str(self.value)} of {self.suit}'


class Deck:
    def __init__(self):
        self.deck = self.generate_deck()

    def generate_deck(self):
        suit = ["Hearts", "Diamonds", "Spades", "Clubs"]
        value = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        return [Card(i, j) for i in suit for j in value]

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def pop_deck(self):
        return self.deck.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.num_books = 0

    def __str__(self):
        hand_str = f"{self.name}'s hand:\n"
        for card in self.hand:
            hand_str += f'{str(card)}\n'
        return hand_str

    def remove_card(self, card):
        self.hand.remove(card)

    def draw_card(self, deck):
        if len(deck.deck) < 1:
            print("Deck is out of cards, you lose your turn.")
            return
        self.hand.append(deck.pop_deck())

    def play_book(self, book):
        for match in book:
            self.hand.remove(match)
        self.num_books += 1

    def steal_card(self, player_from, val, deck):
        stolen_cards = []
        for card in player_from.hand:
            if card.value == val:
                stolen_cards.append(card)
        for card in stolen_cards:
            player_from.hand.remove(card)

        if len(stolen_cards) > 0:
            self.hand.extend(stolen_cards)
            print(f"Stole {len(stolen_cards)} from {player_from.name}. {self.name} can play again.")
            return True
        else:
            print("Go fish!")
            self.draw_card(deck)
            return False

    def check_books(self):
        self.hand.sort()
        counter = 0
        cards_to_remove = []
        temp_rank = None
        for card in self.hand:
            if card.value == temp_rank:
                cards_to_remove.append(card)
                counter += 1
                if counter == 4:
                    print(f"{self.name} played a book of {temp_rank}s")
                    self.play_book(cards_to_remove)
                    counter = 0
                    cards_to_remove = []
            else:
                temp_rank = card.value
                counter = 1
                cards_to_remove = [card]


class GameHelper:
    def __init__(self, players):
        self.players = players

    def deal_cards(self, deck):
        for i in range(0, 5):
            for player in self.players:
                player.draw_card(deck)

    # returns true if 13 (all possible) books are played
    def check_played_books(self):
        total_books = sum(player.num_books for player in self.players)
        if total_books == 13:
            return True
        return False

    def find_winner(self):
        max_books = max(player.num_books for player in self.players)
        winners = [player.name for player in self.players if player.num_books == max_books]
        if len(winners) == 1:
            print(f"{winners[0]} won this round of Go Fish!")
        else:
            print(f"It's a tie! Winners: {', '.join(winners)}")

    # method overloading to exclude a player from printing
    def print_players_exclude(self, player_exclude):
        # enumerate from w3 schools docs
        # https://www.w3schools.com/python/ref_func_enumerate.asp
        for index, player in enumerate(self.players):
            if player_exclude.name != player.name:
                print(f'({index+1}) {player.name}')

    # method overloading to print all players
    def print_players(self):
        # enumerate from w3 schools docs
        # https://www.w3schools.com/python/ref_func_enumerate.asp
        for index, player in enumerate(self.players):
            print(f'({index+1}) {player.name}')

    # method for a player to take their turn
    def turn(self, player, deck):
        valid_card_values = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']

        if len(player.hand) == 0:
            print(f"{player.name}, you ran out of cards, go fish.")
            player.draw_card(deck)
        if len(player.hand) == 0:
            return

        while True:
            user_in = input(f'would you like to do {player.name}:\n'
                            f'(1) ask for a card\n'
                            f'(2) check cards\n'
                            f'input: ')
            if user_in == '1':
                self.print_players_exclude(player)
                while True:
                    steal_from = input("Please enter a player to steal from: ")
                    try:
                        steal_from = int(steal_from) - 1
                        if 0 <= steal_from < len(self.players) and self.players[steal_from] != player:
                            break  # Valid input, exit the loop
                        else:
                            print("Invalid input. Please enter a valid player number.")
                    except ValueError:
                        print("Invalid input. Please enter a valid player number.")

                while True:
                    steal_value = input("Please enter a card value to steal from (2-10, J, Q, K, A): ")
                    if steal_value in valid_card_values:
                        break  # Valid input, exit the loop
                    else:
                        print("Invalid card value. Please enter a valid value (2-10, J, Q, K, A).")

                success = player.steal_card(self.players[steal_from], steal_value, deck)
                player.check_books()
                if not success:
                    return  # End the turn if the player failed to steal a card
                else:
                    continue  # Allow the player to take another action

            elif user_in == '2':
                print(player)
            else:
                print("Invalid input, please enter a valid choice.")


def main():
    # game setup, do not use more than 10 players
    player1 = Player('Abbi G')
    player2 = Player('Clare M')
    player3 = Player('Allannah J')
    player4 = Player('Amelia B')
    helper = GameHelper([player1, player2, player3, player4])

    a_deck = Deck()
    a_deck.shuffle_deck()

    helper.deal_cards(a_deck)

    # game loop:
    while True:
        for player in helper.players:
            helper.turn(player, a_deck)
            if helper.check_played_books():
                helper.find_winner()
                return


if __name__ == "__main__":
    main()
