"""
Blackjack Card Game

Author: badDoggy
Date: 11/19/2026
"""

# ##########  Imports  ##############
import os
import subprocess
import random
import time

# If 'logo.py' is missing, a default logo will be used.
try:
    from logo import logo
except ImportError:
    logo = "#############\n  Blackjack\n#############"


def clear_screen():
    """Clear the terminal screen.
    \nDisplays the Game Logo"""
    command = "cls" if os.name == "nt" else "clear"
    subprocess.run(command, shell=True, check=False)
    print(logo)


def deal_cards(turn):
    """
    Deals the cards.
    \nIf turn is "initial, deals both hands the first 2 cards each
    \n otherwise, deals 1 card only, to dealer or player
    """
    if turn == "initial":
        for _ in range(2):
            dealer_hand.append(random.choice(list(cards)))
            player_hand.append(random.choice(list(cards)))
        return dealer_hand, player_hand
    else:
        card = random.choice(list(cards))
        return card


def hand_total(hand):
    """
    Calculates the hand total
    \nReturns the total value
    """
    total = 0
    ace_count = 0
    for card in hand:
        total += cards[card]
        if card == "A":
            ace_count += 1
    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1

    return total


def is_bj(turn, hand, total):
    """
    Checks if either player has a Blackjack.
    \nWhen this function is called, it checks the dealer first,
    \n  if both players have a Blackjack, the Dealer wins the tie.
    """
    blackjack = False
    text = ""

    if len(hand) == 2 and total == 21:
        blackjack = True
        text = f"{turn} Has Blackjack!!  -  {turn} Wins!"

    return blackjack, text


def is_bust(turn, total):
    """
    Checks if the current player is Bust
    """
    bust = False
    text = ""

    if turn == "Player":
        not_turn = "Dealer"
    else:
        not_turn = "Player"

    if total > 21:
        bust = True
        text = f"\n{turn} is Bust!!  -  {not_turn} Wins!"

    return bust, text


def display_cards(status, dealer, player):
    """
    Displays the hands for output.
    \n if status == "initial", hides the dealer's first card.
    """
    if status == "initial":
        # Display the initial hands; dealer's first card is hidden as "??"
        print(f"Dealer Hand: ?  {dealer[1]}")
        print(f"Player Hand: {'  '.join(player)}")
    else:
        # Display both hands
        print(f"Dealer Hand: {'  '.join(dealer)}")
        print(f"Player Hand: {'  '.join(player)}")


def display_winner(dealer_tot, player_tot):
    """
    Determines if the game is a tie, or if there is a winner.
    \nDisplays the results
    """
    # check for tie or winner
    if dealer_tot == player_tot:
        print(f"\nGame ends in a tie at {dealer_tot}")
    else:
        if dealer_tot > player_tot:
            winner = "Dealer"
        else:
            winner = "Player"

        print(f"\nDealer has: {dealer_tot}")
        print(f"Player has: {player_tot}")
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
# Initial Variables
game_over = False
dealer_hand = []
player_hand = []
choice = ""

# Play the game
while not game_over:
    # Clear the screen & Display the logo
    clear_screen()

    # Initial setup - Deal the first 2 cards
    deal_cards("initial")

    # Get initial Display (hides dealer's first card)
    display_cards("initial", dealer_hand, player_hand)

    # Get the hand totals
    dealer_total = hand_total(dealer_hand)
    player_total = hand_total(player_hand)

    # check for Blackjack
    # have to check dealer first : if they both have bj, dealer wins
    dealer_bj, dealer_text = is_bj("Dealer", dealer_hand, dealer_total)
    player_bj, player_text = is_bj("Player", player_hand, player_total)
    if dealer_bj or player_bj:
        clear_screen()
        display_cards("all", dealer_hand, player_hand)
        if dealer_bj:
            print(f"\n{dealer_text}")
            if player_bj:
                print("Player also has a Blackjack but the Dealer wins the tie.")
            else:
                print(f"Player has: {player_total}")
        else:
            print(f"\nDealer has: {dealer_total}")
            print(f"{player_text}")
        game_over = True

    # Player's Turn
    else:
        while True:
            # Player Input: Hit, Stand, or Quit
            print(f"\nPlayer has : {player_total}\n")
            choice = input("Would you like to H)it, S)tand, or Q)uit? ").lower()

            # Player Hits another card
            if choice in ("h", "hit"):
                player_hand.append(deal_cards("player"))
                player_total = hand_total(player_hand)

                # check if player is bust
                player_bust, player_text = is_bust("Player", player_total)
                clear_screen()
                if not player_bust:
                    display_cards("initial", dealer_hand, player_hand)
                else:
                    display_cards("all", dealer_hand, player_hand)
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
                display_cards("initial", dealer_hand, player_hand)

        # Dealer's Turn
        if not game_over:
            while True:
                # Clear the screen to display ALL of the cards
                clear_screen()
                display_cards("all", dealer_hand, player_hand)

                # Dealer takes a card
                if dealer_total < 17:
                    # deal a new card
                    dealer_hand.append(deal_cards("dealer"))

                    # get total and status
                    dealer_total = hand_total(dealer_hand)

                    # redraw the screen
                    clear_screen()
                    display_cards("all", dealer_hand, player_hand)

                    # Display output
                    print(f"\nDealer draws: {dealer_hand[-1]}")
                    print(f"Dealer has: {dealer_total}")

                    # Pauses play so player can see the new card
                    time.sleep(2)

                # Dealer Bust
                elif dealer_total > 21:
                    dealer_bust, dealer_text = is_bust("Dealer", dealer_total)
                    print(f"Dealer has: {dealer_total}")
                    print(f"\n{dealer_text}")
                    game_over = True
                    break

                # check for tie or winner
                else:
                    display_winner(dealer_total, player_total)
                    game_over = True
                    break

    # Play Again Prompt
    if game_over and choice not in ("q", "quit"):
        again = input("\nPlay Again>  (Y/N) ").strip().lower()
        if again in ("y", "yes"):
            # Reset Variables and Deal the first 2 cards
            game_over = False
            dealer_hand = []
            player_hand = []
            choice = ""
        else:
            break


# End the app
print("\n\n\n--  End of Line --\n")
