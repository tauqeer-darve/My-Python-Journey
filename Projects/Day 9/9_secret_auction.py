#Secret Auction
import art
print(art.logo)
# Initialize an empty dictionary to store bidder names and their bid amounts
auction = {}
# Flag to control the bidding loop
flag = True


def winner(bidding_dict):
    # Initialize variables to track the highest bid and the winner's name
    winner = ""
    highest_bid = 0

    # Loop through each bidder in the dictionary to find the highest bid
    for bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]
        # Update highest bid and winner if the current bid is higher
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    # Display the winner's name and their bid amount
    print(f"The winner of this bidding is '{winner}' with a bid of ${highest_bid}")


# Start the bidding process
while flag:
    # Prompt for bidder's name and bid amount, and add to the auction dictionary
    name = input("Enter your name: ")
    bid = int(input("Enter bid amount: $"))
    auction[name] = bid

    # Ask if there are more bidders and decide whether to continue
    cont = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if cont == "no":
        # If no more bidders, end the loop and determine the winner
        flag = False
        winner(auction)
    else:
        # Clear the screen to keep each bidder's information private
        print("\n" * 100)
