#######################
# Blackjack Card Game
# badDoggy | 11/12/26
#######################


# ##########  Imports  ##############
import subprocess
import os
import random


# #########  Functions  ##############
# Clear Screen & Display Logo
def clear_screen():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    command = "cls" if os.name == "nt" else "clear"
    subprocess.run(command, shell=True, check=False)

    print("---------------------------")
    print("  Blackjack   Card   Game")
    print("---------------------------\n")


# Deal cards and display the results
def deal_card(player):
    dealer_total = 0
    player_total = 0
    if player == "initial":
        # get initial cards

        # debug code
        dealer_hand.append(11)
        dealer_hand.append(10)
        for x in range(0, 2):

            # dealer_hand.append(random.choice(cards))
            player_hand.append(random.choice(cards))

        # debug code
        dealer_total = card_totals(dealer_hand)
        print(
            f"Dealer has {dealer_hand[0]}, {dealer_hand[1]} - -  total: {dealer_total}"
        )
        print(f"Dealer is showing: {dealer_hand[0]}\n")

        # get player total
        player_total = card_totals(player_hand)
        # display player cards
        print(
            f"Player has {player_hand[0]}, {player_hand[1]} - -  total: {player_total}"
        )

    elif player == "dealer":
        # dealer gets a card
        dealer_hand.append(random.choice(cards))
        # get dealer total
        dealer_total = card_totals(dealer_hand)
        # display dealer cards
        print(f"Dealer has {" ".join(dealer_hand)} - -  total: {dealer_total}\n")
    else:
        # player gets a card
        player_hand.append(random.choice(cards))
        # get player total
        player_total = card_totals(player_hand)
        # display player cards
        print(
            f"Player has {player_hand[0]}, {player_hand[1]} - -  total: {player_total}"
        )

    return dealer_total, player_total


def card_totals(hand):
    total = 0
    for amt in range(0, len(hand)):
        total += hand[amt]
    return total


# #########  Variables  ##############
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_hand = []
player_hand = []
end_game = False


while not end_game:
    # Clear Screen & Display Logo
    clear_screen()

    # deal initial cards
    dealer_total, player_total = deal_card("initial")

    if dealer_total == 21:
        print(f"Dealer has BLACKJACK!!  - - Dealer Wins")
        print(f"{" ".join(dealer_hand)} - -  total: {dealer_total}\n")

    end_game = True


# End the app
print("\n\n--  End of Line --\n")
