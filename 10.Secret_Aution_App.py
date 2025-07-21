import os
def find_highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


print("Welcome to the Secret Auction!")
bids = {}
bidding_finished = False

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if should_continue == "no":
        bidding_finished = True
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen for secrecy

find_highest_bidder(bids)

