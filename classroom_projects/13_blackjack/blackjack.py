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
        print(f"Dealer Cards:  XX  {dealer_hand[1]}")

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


# Reset variables for new game
def game_reset():
    dealer_hand = []
    player_hand = []
    round = "initial"
    game_over = False

    return dealer_hand, player_hand, round, game_over


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
dealer_hand, player_hand, round, game_over = game_reset()

while not game_over:
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

        if dealer_total == 21:
            clear_screen()
            display_cards("dealer")
            print(f"\nDealer Wins!!  -  Dealer has Blackjack!!")
            game_over = True
            break
        elif player_total == 21:
            clear_screen()
            display_cards("player")
            print(f"\nPlayer Wins!!  -  Player has Blackjack!!")
            game_over = True
            break
        else:
            while True:
                player_turn = input("\nPlayer's Turn: Q)uit, H)it or P)ass? ").lower()
                if player_turn == "q" or player_turn == "quit":
                    print("Player Quit...")
                    game_over = True
                    break
                elif player_turn == "h" or player_turn == "hit":
                    # clear_screen()
                    # deal_cards("player")
                    # display_cards(round)
                    # dealer_total, player_total = card_totals()
                    # if player_total > 21:
                    #     # clear_screen()
                    #     # display_cards(round)
                    #     print(f"\nPlayer Bust: {player_total}")
                    #     game_over = True
                    #     break
                    print(f"\nPlayer Hits...")
                    game_over = True
                    break
                elif player_turn == "p" or player_turn == "pass":
                    print("Dealer's turn...")
                    game_over = True
                    break
                else:
                    print("\nERROR: Invalid Input!!")
                    input("Press any key to continue...")
                    clear_screen()
                    display_cards("player")

    if game_over:
        again = input("\nPlay Again?  (Y/N) ").lower()
        if again == "y":
            dealer_hand, player_hand, round, game_over = game_reset()
        else:
            game_over = True


# End the app
print("\n\n--  End of Line --\n")
