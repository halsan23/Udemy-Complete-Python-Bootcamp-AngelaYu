#######################
# Blackjack Card Game
# badDoggy | 11/16/26
#######################


# ##########  Imports  ##############
import subprocess
import os
import random
from logo import logo


# #########  Functions  ##############
def clear_screen():
    """Clears the screen and displays the logo art."""
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    command = "cls" if os.name == "nt" else "clear"
    subprocess.run(command, shell=True, check=False)
    print(logo)


def initial_setup():
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


def card_totals(hand):
    """Calculates the total for the current hand.
    \nIf total is over 21 and you have an Ace, total -= 10.
    \n  - If total over 21 and no Ace, return bust == true
    \n\nChecks for Blackjack: returns True or False.
    \n  - Blackjack value determined by only having two cards that equal 21.
    \nreturns the hand total with Blackjack and Bust status."""

    total = 0
    blackjack = False
    bust = False

    if hand == "player":
        hand = player_hand
    else:
        hand = dealer_hand

    for card in hand:
        total += cards[card]
        if card == "A" and total > 21:
            total -= 10

    if len(hand) == 2 and total == 21:
        blackjack = True
    elif total > 21:
        bust = True

    return total, blackjack, bust


def is_bust(turn):
    """
    If the current player is bust, display who the winner is.
    """
    if turn == "dealer":
        return f"\nDealer is Bust!!  -  Dealer Wins!"
    else:
        return f"\nPlayer is Bust!!  -  Player Wins!"


def display_initial():
    """
    Displays the hands.
    \nDealers first card is hidden.
    """
    # Display the initial hands
    print(f"Dealer Hand: XX  {dealer_hand[-1]}")
    print(f"Player Hand: {"  ".join(player_hand)}")


def display_all():
    """
    Displays the hands.
    \nAll cards are shown.
    """
    # Display the initial hands
    print(f"Dealer Hand: {"  ".join(dealer_hand)}")
    print(f"Player Hand: {"  ".join(player_hand)}")


###########  Variables  ##############
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
game_over = False


while not game_over:
    choice = ""
    # Clear the screen & Display the logo
    clear_screen()

    # Deal the initial 2 cards
    dealer_hand, player_hand, game_over = initial_setup()

    # Get the hand totals
    dealer_tot, dealer_bj, dealer_bust = card_totals("dealer")
    player_tot, player_bj, player_bust = card_totals("player")

    # Get initial Display (hides dealer's first card)
    display_initial()

    # check for Blackjack
    if dealer_bj:
        clear_screen()
        display_all()
        print("\nDealer Has Blackjack!!  -  Dealer Wins!")
        game_over = True
    elif player_bj:
        clear_screen()
        display_all()
        print("\nPlayer Has Blackjack!!  -  Player Wins!")
        game_over = True
    else:
        game_over = True

    # Player's Turn
    # while True:
    #     print(f"\nPlayer has : {player_tot}\n")
    #     choice = input("Would you like to H)it, S)tand, or Q)uit? ").lower()
    #     if choice == "q" or choice == "quit":
    #         print("\n\nPlayer quit   - Game Over -")
    #         game_over = True
    #         break
    #     elif choice == "s" or choice == "stand":
    #         break
    #     elif choice == "h" or choice == "hit":
    #         player_hand.append(deal_card())
    #         player_tot, player_bj, player_bust = card_totals("player")
    #         clear_screen()
    #         display_initial()

    #         if player_bust:
    #             print("\nPlayer is Bust!!  -  Dealer Wins!")
    #             game_over = True
    #             break
    #         else:
    #             clear_screen()

    #     else:
    #         print("Invalid Input!!")

    # Dealer's Turn
    # debug code
    # print(f"\nDealer: {dealer_tot}  |  Blackjack: {dealer_bj}")
    # choice = input("Dealer's Turn - press any key to continue: ")

    # Play Again Loop
    if game_over and (choice != "q" and choice != "quit"):
        again = input("\nPlay Again>  (Y/N) ")
        if again == "y" or again == "yes":
            game_over = False
        else:
            break

# End the app
print("\n\n\n--  End of Line --\n")
