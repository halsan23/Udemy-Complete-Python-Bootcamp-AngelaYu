"""
Blackjack Card Game

Author: badDoggy
Date: 11/18/2026
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


def initial_setup():
    """Sets initial variables\n
    Deals the first hand."""
    game_over = False

    dealer_hand = []
    player_hand = []

    for _ in range(2):
        dealer_hand.append(deal_card())
        player_hand.append(deal_card())

    return dealer_hand, player_hand, game_over


def deal_card():
    """Deals a single card from the deck to the player that called the function.
    \nFormat to call function is:
    \n  (player_hand or dealer_hand).append(deal_card())"""
    card = random.choice(list(cards))
    return card


def card_totals(hand, who):
    """
    Calculates the hand totals.
    \nChecks if current player has Blackjack or is Bust.
    \n  Builds a text string for output display if the current player is Blackjack or Bust.
    \nCalculates if an Ace should be worth 1 or 11.
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


def display_cards(status, dealer, player):
    """
    Displays the current card hands.
    \nIf the status is "initial", hides the dealers first card.
    """
    if status == "initial":
        # Display the initial hands; dealer's first card is hidden as "??"
        print(f"Dealer Hand: ?  {dealer[1]}")
        print(f"Player Hand: {'  '.join(player)}")
    else:
        # Display both hands
        print(f"Dealer Hand: {'  '.join(dealer)}")
        print(f"Player Hand: {'  '.join(player)}")


def display_winner(winner, dealer_total, player_total):
    """Displays the hand totals.
    \nDisplays the Winner"""
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

# Initial setup - Deal the first 2 cards
dealer_hand, player_hand, game_over = initial_setup()


while not game_over:
    # Set the initial player choices to an empty string
    choice = ""
    # Clear the screen & Display the logo
    clear_screen()

    # Get the hand totals
    dealer_tot, dealer_bj, dealer_bust, dealer_text = card_totals(dealer_hand, "dealer")
    player_tot, player_bj, player_bust, player_text = card_totals(player_hand, "player")

    # Get initial Display (hides dealer's first card)
    display_cards("initial", dealer_hand, player_hand)

    # check for Blackjack
    if dealer_bj:
        clear_screen()
        display_cards("all", dealer_hand, player_hand)
        print(f"\n{dealer_text}")
        game_over = True
    elif player_bj:
        clear_screen()
        display_cards("all", dealer_hand, player_hand)
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
                clear_screen()
                display_cards("all", dealer_hand, player_hand)
                # Dealer takes a card
                if dealer_tot < 17:
                    # deal a new card
                    dealer_hand.append(deal_card())
                    # get total and status
                    dealer_tot, dealer_bj, dealer_bust, dealer_text = card_totals(
                        dealer_hand, "dealer"
                    )
                    # redraw the screen
                    clear_screen()
                    display_cards("all", dealer_hand, player_hand)
                    print(f"\nDealer draws: {dealer_hand[-1]}")
                    print(f"Dealer has: {dealer_tot}")
                    if dealer_tot < 22:
                        # Pauses play so player can see the new card
                        time.sleep(3)
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

    # Play Again Prompt
    if game_over and choice not in ("q", "quit"):
        again = input("\nPlay Again>  (Y/N) ").strip().lower()
        if again in ("y", "yes"):
            # Reset Variables and Deal the first 2 cards
            dealer_hand, player_hand, game_over = initial_setup()
        else:
            break

# End the app
print("\n\n\n--  End of Line --\n")
