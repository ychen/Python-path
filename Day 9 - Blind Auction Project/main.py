import art
print(art.logo)

def find_winner(bid_dictionary):
    winner = ""
    highest_price = 0
    for bidder in bid_dictionary:
        if bid_dictionary[bidder] > highest_price:
            highest_price = bid_dictionary[bidder]
            winner = bidder

    print(f"The winner is: {winner}!")

bid = True
bid_deal = {}
while bid:

    name = input("What is your name? \n")
    bid_amount = int(input("What's your bid? \n"))
    bid_deal[name] = bid_amount
    more_biders = input("Are there any other biders? Type 'Yes' or 'No': \n")
    if more_biders == "Yes":
        bid = True
        print("\n" * 20)

    if more_biders == "No":
        bid = False
        print(bid_deal)
        find_winner(bid_dictionary = bid_deal)



# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


