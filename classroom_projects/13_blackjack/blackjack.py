#######################
# Blackjack Card Game
# badDoggy | 11/17/2026
#######################


# ##########  Imports  ##############
import subprocess
import os
import random
from logo import logo


# #########  Functions  ##############
def clear_screen():
    """Clears the screen and displays the logo art."""
    command = "cls" if os.name == "nt" else "clear"
    subprocess.run(command, shell=True, check=False)
    print(logo)


def initial_setup():
    """Resets game data for initial start or replay and returns their initial values.
    \nDeals the first 2 cards for each player"""

    dealer_hand = []
    player_hand = []
    game_over = False

    for _ in range(2):
        dealer_hand.append(deal_card())
        player_hand.append(deal_card())

    return dealer_hand, player_hand, game_over


def deal_card():
    """Pulls a single random card from the deck.
    \nReturns the card by dictionary "key" name.
    \nMust assign this card to a player when calling the function.
    \n  eg. player_hand.append(deal_card())"""

    card = random.choice(list(cards))
    return card


def card_totals(hand, who):
    """
    Calculates the total for the current hand.
    \nIf total is over 21 and you have an Ace, total -= 10.
    \n  - If total over 21 and no Ace, return bust == true
    \n\nChecks for Blackjack: returns True or False.
    \n  - Blackjack value determined by only having two cards that equal 21.
    \nreturns the hand total with Blackjack and Bust status.
    """
    total = 0
    blackjack = False
    bust = False
    text = ""

    if who == "player":
        turn = "Player"
        not_turn = "Dealer"
    else:
        turn = "Dealer"
        not_turn = "Player"

    ace_count = 0
    for card in hand:
        total += cards[card]
        if card == "A":
            ace_count += 1
    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1

    if len(hand) == 2 and total == 21:
        blackjack = True
        text = f"\n{turn} Has Blackjack!!  -  {turn} Wins!"
    elif total > 21:
        bust = True
        text = f"\n{turn} is Bust!!  -  {not_turn} Wins!"

    return total, blackjack, bust, text


def display_cards(status):
    """
    Displays the cards using the global variables 'dealer_hand' and 'player_hand'.
    If the status is "initial", Dealer's first card is hidden.
    """
    if status == "initial":
        # Display the initial hands; dealer's first card is hidden as "??"
        print(f"Dealer Hand: ?? {dealer_hand[1]}")
        print(f"Player Hand: {'  '.join(player_hand)}")
    else:
        # Display both hands
        print(f"Dealer Hand: {'  '.join(dealer_hand)}")
        print(f"Player Hand: {'  '.join(player_hand)}")


def display_winner(winner, dealer_total, player_total):
    """Displays the Winner"""
    print(f"\nDealer has: {dealer_total}")
    print(f"Player has: {player_total}")
    print(f"\n- {winner} Wins -")


###########  Variables  ##############
# Dictionary for cards
cards = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}
# Initial set game_over to False
game_over = False


while not game_over:
    # Set the initial player choices to an empty string
    choice = ""
    # Clear the screen & Display the logo
    clear_screen()

    # Deal the initial 2 cards
    dealer_hand, player_hand, game_over = initial_setup()

    # Get the hand totals
    dealer_tot, dealer_bj, dealer_bust, dealer_text = card_totals(dealer_hand, "dealer")
    player_tot, player_bj, player_bust, player_text = card_totals(player_hand, "player")

    # Get initial Display (hides dealer's first card)
    display_cards("initial")

    # check for Blackjack
    if dealer_bj:
        clear_screen()
        display_cards("all")
        print(f"\n{dealer_text}")
        game_over = True
    elif player_bj:
        clear_screen()
        display_cards("all")
        print(f"\n{player_text}")
        game_over = True

    else:
        # Player's Turn
        while True:
            # Player Input: Hit, Stand, or Quit
            print(f"\nPlayer has : {player_tot}\n")
            choice = input("Would you like to H)it, S)tand, or Q)uit? ").lower()
            # Player Hits another card
            if choice in ("h", "hit"):
                player_hand.append(deal_card())
                player_tot, player_bj, player_bust, player_text = card_totals(
                    player_hand, "player"
                )
                clear_screen()
                if not player_bust:
                    display_cards("initial")
                else:
                    display_cards("all")
                    print(f"\n{player_text}")
                    game_over = True
                    break
            # Player Stands
            elif choice in ("s", "stand"):
                break
            # Player Quits
            elif choice in ("q", "quit"):
                print("\n\n- Game Over -")
                game_over = True
                break
            # Invalid Input (not h, s, q)
            else:
                print("\nInvalid Input!!")
                input("Press any key to continue...")
                clear_screen()
                display_cards("initial")

        # Dealer's Turn
        if not game_over:
            while True:
                clear_screen()
                display_cards("all")
                # Dealer takes a card
                if dealer_tot < 17:
                    dealer_hand.append(deal_card())
                    dealer_tot, dealer_bj, dealer_bust, dealer_text = card_totals(
                        dealer_hand, "dealer"
                    )
                    clear_screen()
                    display_cards("all")
                    print(f"\nDealer draws: {dealer_hand[-1]}")
                    # Pauses play so player can see the new card
                    input("\nPress any key to continue...")
                # Dealer Bust
                elif dealer_bust:
                    print(f"\n{dealer_text}")
                    game_over = True
                    break

                else:
                    # check for tie or winner
                    if dealer_tot > player_tot:
                        display_winner("Dealer", dealer_tot, player_tot)
                    elif dealer_tot < player_tot:
                        display_winner("Player", dealer_tot, player_tot)
                    else:
                        print(f"\nGame ends in a tie at {dealer_tot}")

                    game_over = True
                    break

    # Play Again Loop
    if game_over and choice not in ("q", "quit"):
        again = input("\nPlay Again>  (Y/N) ")
        if again in ("y", "yes"):
            game_over = False
        else:
            # End the app
            print("\n\n\n--  End of Line --\n")
            break
