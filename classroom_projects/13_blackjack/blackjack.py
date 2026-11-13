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


# Deal the cards
def deal_cards(turn):
    if turn == "initial":
        for card in range(0, 2):
            dealer_hand.append(random.choice(list(cards)))
            player_hand.append(random.choice(list(cards)))
    elif turn == "player":
        player_hand.append(random.choice(list(cards)))
    else:
        dealer_hand.append(random.choice(list(cards)))

    return turn


# Display the cards
def display_cards(turn):
    if turn == "initial":
        print(f"Dealer Cards:  {dealer_hand[1]}  Hidden")

        # print the player card ant it's value
        # print(f"Player Card:   {player_hand[0]}  {player_hand[1]}")
        print(f"Player Cards:  {"  ".join(player_hand)}")
    else:
        print()
        print("Dealer Cards:  " + "  ".join(dealer_hand))
        print("Player Cards:  " + "  ".join(player_hand))


# Determine hand totals
def card_totals():
    dealer_total = 0
    player_total = 0
    for card in dealer_hand:
        dealer_total += cards[card]
    for card in player_hand:
        player_total += cards[card]

    for card in player_hand:
        if card == "A" and player_total > 21:
            player_hand[card] = 1

    return dealer_total, player_total


# #########  Variables  ##############
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
dealer_hand = []
player_hand = []
end_game = False
game_over = False


while not end_game:
    round = "initial"
    # Clear Screen & Display Logo
    clear_screen()

    # deal initial cards
    while round == "initial":
        deal_cards(round)
        display_cards(round)
        dealer_total, player_total = card_totals()
        print()
        if round != "initial":
            print(f"Dealer has: {dealer_total}")
        print(f"Player has: {player_total}")
        round = "player"

        if dealer_total == 21:
            clear_screen()
            display_cards(round)
            print(f"\nDealer Wins!!  -  Dealer has Blackjack!!")
            game_over = True
        elif player_total == 21:
            clear_screen()
            display_cards(round)
            print(f"\nPlayer Wins!!  -  Player has Blackjack!!")
            game_over = True

        if game_over:
            play_again(): ## need to define this function
    end_game = True


# End the app
print("\n\n--  End of Line --\n")
