import random

# create the suit array
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
# create the rank array
ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
# create a values dictionary to easily test to see if ranks are face or not
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
                
def main():
    # print intro statements
    print("Welcome to The Kenzo!")
    print("This is version one of my interpretation of a game played by my friends and I, I've googled around and this may exist under another name, so if anyone finds it let me know.")
    print("In the real-life version of The Kenzo, a pyramid of between 5 and 10 levels is made out of cards placed face-down on the playing surface.")
    print("The player will then turn over a card on the first row, and if the card is a number card the player advances.")
    print("If, however, the card is a face card, then the player must cover over all cards they've overturned on each row they have made it past with cards from the shuffled deck, and start again from the beginning.")
    print("The aim of the game is to make it to the top of the pyramid as quickly as possible.")
    print("The rules are simple, a player wins if they make it to the top of the pyramid, and loses if they run out of cards in the deck, enjoy!")
    
    on = True

    while on:
        # create classes
        deck = Deck()
        deck.shuffle()
        player = input("Input your name: ")

        # create the pyramid and fill the arrays with relevant numbers for each row
        pyramid = [[], [], [], [], [], [] ,[]]
        numb_cards, row_index = 8, 0
        while numb_cards > 0:
            numb_cards -= 1
            for i in range(numb_cards):
                pyramid[row_index].append(deck.deal_card())
            row_index += 1

        # set the game counters pre-game
        game_on = True    
        round = 0
        cards = 7
        active_cards = []
        # now initiate game_on
        while game_on:
            # ask the player which card they want to choose
            while True:
                # for all rounds bar the last
                if round != 6:
                    try:
                        choice = int(input(f"{player}, Please choose a card between 1 and {cards}: "))
                        if choice > 0 and choice <= cards:
                            break
                    except ValueError:
                        print("Please enter an integer")
                # if the penultimate round
                elif round == 6:
                    try:
                        choice = int(input(f"{player}, Please choose the final card (enter 1) "))
                        if choice == 1:
                            break
                    except ValueError:
                        print("Please enter the number 1 for your final card")
            # convert the players choice to the relevant index
            choice -= 1
            # index into the pyramid and get the card they chose
            chosen_card = pyramid[round][choice]
            # append the current card to the active cards array
            active_cards.append(chosen_card)
            # print the current active cards
            print(f"Active Cards: ")
            for card in active_cards:
                print(card)
            # check to see whethere the card is a face card or number card
            if chosen_card.value > 10:
                # need to discard the current chosen card and any before it if we are further into the game
                # first replace the card in the pyramid rows
                for i in range(len(pyramid)):
                    for j in range(len(pyramid[i])):
                        if pyramid[i][j] in active_cards:
                            try:
                                pyramid[i][j] = deck.deal_card()
                            except IndexError:
                                print("You ran out of cards!")
                                game_on = False   
                # then remove the card from the active cards list, and add to the discard pile
                for card in active_cards:
                    active_cards.remove(card)
                # set round back to start
                round = 0
                # set cards back to start
                cards = 7
            # if the card is a number card
            elif chosen_card.value <= 10:
                # increase round
                round += 1
                # decrease cards
                cards -= 1
            # winning condition
            if round >= 7:
                print("Congratulations! You have won The Kenzo!")
                game_on = False
            # losing condition
            elif not deck.all_cards:
                print("Unlucky! You ran out of cards and have lost The Kenzo")
                game_on = False
        # check if the user wants to play again
        answer = play()
        if answer == 'y':
            on = True   
        elif answer == 'n':
            print("Thanks for playing!")
            on = False

class Card:
    # when a card is instantiated, we want a suit and rank to be provided, the value will be automatically assigned via a dictionary
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    # create a string method for easy understanding for a user
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    # create a deck of 52 unique cards
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(rank, suit))
    # enable shuffling of the deck
    def shuffle(self):
        random.shuffle(self.all_cards)
    # enable dealing of a card from the deck
    def deal_card(self):
        return self.all_cards.pop()

# define the play function, which asks if someone wants to play again
def play():
    while True:
        try:
            play_again = input("Do you want to play again? Enter Y/N ").lower()
            if play_again in ['y', 'n']:
                return play_again
        except ValueError:
            print("Please input Y or N")
            continue

if __name__ == "__main__":
    main()