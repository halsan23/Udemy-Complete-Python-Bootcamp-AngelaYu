#####################################
# Blind Auction - Hidden Bids
# Created by - badDoggy | 11/09/26
#####################################


# ##########  Imports  ##############
import subprocess
import os
from gavel import logo


# #########  Functions  ##############
# Clear Screen
def clear_screen():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    command = "cls" if os.name == "nt" else "clear"
    subprocess.run(command, shell=True, check=False)


# Determine the highest bid and the winner
# Display the results
def get_winner(bid_dict):
    # find the max value in a dictionary
    # return key and value
    # https://www.geeksforgeeks.org/python/python-get-key-with-maximum-value-in-dictionary/
    winner = max(bid_dict, key=bid_dict.get).capitalize()
    win_amt = max(bid_dict.values())

    # Display the results
    clear_screen()
    print(logo)
    print(f"\n{winner} wins this fabulous item with a bid of ${win_amt:.2f}")


# #########  Variables  ##############
current_bids = {}
end_app = False


while not end_app:
    # clear the screen and display the logo
    clear_screen()
    print(logo)

    # Input a bidder name
    bidder = input("Q)uit or enter Bidder name? ")
    if bidder == "q" or bidder == "Q":
        end_app = True
        break

    # Input the bid amount
    # Bid amount must be a currency value (floating point number)
    while True:
        try:
            bid_amt = float(
                input("\nHow much would you like to bid on this fabulous item? ")
            )
            # Add the bidder name and bid amount to the current_bids{} dictionary
            current_bids[bidder] = bid_amt
            break
        except:
            print("\nERROR! : Input must be a dollar amount.\n")

    # Are there any other bidders
    again = input("\nAre there any other bidders? (Y/N) ").lower()
    if again == "n" or again != "":
        # Determine the highest bid and the winner
        # Display the results
        get_winner(current_bids)
        end_app = True


# End the app
print("\n\n--  End of Line --\n")
