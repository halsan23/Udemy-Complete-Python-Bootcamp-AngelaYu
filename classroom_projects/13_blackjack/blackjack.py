#######################
# Blackjack Card Game
# badDoggy | 11/12/26
#######################


# ##########  Imports  ##############
import subprocess
import os
import random
from logo import logo


# #########  Functions  ##############
# Clear Screen & Display Logo
def clear_screen():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    command = "cls" if os.name == "nt" else "clear"
    subprocess.run(command, shell=True, check=False)
    print(logo)


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


# Display the cards
def display_cards(turn):
    if turn == "initial":
        print(f"Dealer Cards:  XX  {dealer_hand[1]}")
        print(f"Player Cards:  {"  ".join(player_hand)}")
    else:
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

    for card in dealer_hand:
        if card == "A" and dealer_total > 21:
            dealer_total -= 10

    for card in player_hand:
        if card == "A" and player_total > 21:
            player_total -= 10

    return dealer_total, player_total


# Reset variables for new game
def game_reset():
    dealer_hand = []
    player_hand = []
    turn = "initial"
    game_over = False

    return dealer_hand, player_hand, turn, game_over


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
dealer_hand, player_hand, turn, game_over = game_reset()

while not game_over:
    # Clear Screen & Display Logo
    clear_screen()

    # deal initial cards, calculate the card totals
    deal_cards(turn)
    display_cards(turn)
    dealer_total, player_total = card_totals()

    # debug code : display card totals
    # print(f"\nDealer has: {dealer_total}")
    # print(f"Player has: {player_total}")
    # dealer_total = 21
    # player_total = 21

    # if Dealer has BlackJack - Dealer Wins
    if dealer_total == 21:
        clear_screen()
        display_cards("dealer")
        print(f"\nDealer Wins!!  -  Dealer has Blackjack!!")
        game_over = True
    # if Player has BlackJack - Player Wins
    elif player_total == 21:
        clear_screen()
        display_cards("player")
        print(f"\nPlayer Wins!!  -  Player has Blackjack!!")
        game_over = True
    else:
        while True:
            turn = "player"
            print(f"\nPlayer has {player_total}:")
            choice = input(f"Do you want to H)it, S)tand, or Q)uit? ").lower()
            if choice == "q" or choice == "quit":
                print("\nPlayer quit...")
                game_over = True
                break
            elif choice == "h" or choice == "hit":
                clear_screen()
                deal_cards(turn)
                display_cards("initial")
                dealer_total, player_total = card_totals()
                if player_total > 21:
                    print(f"\nPlayer is BUST with {player_total}  -  Dealer Wins!")
                    game_over = True
                    break
            elif choice == "s" or choice == "stand":
                break
            else:
                print("\nERROR: Invalid Input!")
                input("Press any key to continue...")
                clear_screen()
                display_cards("initial")

        if not game_over:
            turn = "dealer"
            if dealer_total < 17:
                clear_screen()
                deal_cards(turn)
                display_cards("dealer")
                dealer_total, player_total = card_totals()

                # debug code
                print(f"Dealer Total: {dealer_total}")

            if dealer_total > 21:
                print(f"\nDealer is BUST with {dealer_total}  -  Player Wins!")
            else:
                if dealer_total == player_total:
                    print(f"\nGame is a draw at {dealer_total}  -  Dealer wins!")
                elif dealer_total > player_total:
                    print(f"\nDealer wins with {dealer_total}")
                else:
                    print(f"\nPlayer Wins with {player_total}")
        game_over = True

    if game_over:
        again = input("\nPlay Again?  (Y/N) ").lower()
        if again == "y":
            dealer_hand, player_hand, turn, game_over = game_reset()


# End the app
print("\n\n--  End of Line --\n")
