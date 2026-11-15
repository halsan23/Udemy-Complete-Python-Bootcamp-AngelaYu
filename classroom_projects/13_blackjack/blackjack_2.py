#######################
# Blackjack Card Game
# badDoggy | 11/15/26
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
    """Resets game data for initial start or replay and returns their initial values."""
    dealer_hand = []
    player_hand = []
    turn = "initial"
    game_over = False

    for _ in range(2):
        dealer_hand.append(deal_card())
        player_hand.append(deal_card())

    return dealer_hand, player_hand, turn, game_over


def deal_card():
    """Pulls a single random card from the deck. Must assign this card to a player when calling the function.
    \nReturns the card by dictionary "key" name."""
    card = random.choice(list(cards))
    return card


def card_totals(hand):
    """Calculates the total for the current hand.
    \nDetermines if total is over 21 and you have an Ace, make Ace value = 1.
    \nChecks for Blackjack: returns True or False.
    \n  - Blackjack value determined by only having two cards that equal 21.
    \nreturns the hand total and Blackjack status."""
    hand_total = 0
    for card in hand:
        hand_total += cards[card]

    for card in hand:
        if card == "A" and hand_total > 21:
            hand_total -= 10

    if len(hand == 2) and hand_total == 21:
        blackjack = True
    else:
        blackjack = False

    return hand_total, blackjack


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


dealer_hand, player_hand, turn, game_over = initial_setup()
print(dealer_hand)
print(card_totals(dealer_hand))
print()
print(player_hand)
print(card_totals(player_hand))
print()
print(turn)
print(game_over)
