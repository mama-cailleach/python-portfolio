import random

# Suits and ranks
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# ASCII art templates for suits
SUIT_SYMBOLS = {
    'Hearts': '♥',
    'Diamonds': '♦',
    'Clubs': '♣',
    'Spades': '♠'
}

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def ascii_art(self):
        # Simple ASCII art card
        lines = [
            "┌─────────┐",
            f"│{self.rank:<2}       │",
            "│         │",
            f"│    {SUIT_SYMBOLS[self.suit]}    │",
            "│         │",
            f"│       {self.rank:>2}│",
            "└─────────┘"
        ]
        return "\n".join(lines)

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in SUITS for rank in RANKS]
    
    def draw_card(self):
        return random.choice(self.cards)

class InvalidGuess(Exception):
    pass

class GuessTheCardGame:
    def __init__(self):
        self.deck = Deck()
        self.target_card = self.deck.draw_card()

    def get_guess(self):
        rank = input(f"Guess the card rank ({', '.join(RANKS)}): ").strip().upper()
        suit = input(f"Guess the suit ({', '.join(SUITS)}): ").strip().capitalize()
        if rank not in RANKS or suit not in SUITS:
            raise InvalidGuess("Invalid rank or suit entered.")
        return Card(rank, suit)

    def play(self):
        print("Welcome to the Magic Card Guessing Game!")
        print("Try to guess the card chosen by the computer.\n")
        attempts = 0
        while True:
            try:
                guess = self.get_guess()
                attempts += 1
                if guess == self.target_card:
                    print("\nAmazing! You guessed the card!\n")
                    print(self.target_card.ascii_art())
                    print(f"\nIt took you {attempts} attempt(s).")
                    break
                else:
                    print("Nope, that's not the card. Try again!\n")
            except InvalidGuess as e:
                print(f"Error: {e}\nPlease enter a valid rank and suit.\n")
            except KeyboardInterrupt:
                print("\nGame exited. The card was:")
                print(self.target_card.ascii_art())
                break

if __name__ == "__main__":
    GuessTheCardGame().play()
