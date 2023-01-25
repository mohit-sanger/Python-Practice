
bid = {}
bidding_finish = False

def heighst_bid(bidding_amount):
    highest_bid = 0
    winner = ""
    for bidder in bidding_amount:
        bid_value = bidding_amount[bidder]
        if bid_value > highest_bid:
            highest_bid = bid_value
            winner = bidder
    print(f"the winner is {winner} with a bid of ${highest_bid}")




while not bidding_finish:
    name = input('Enter your full name: ')
    price = int(input('Enter bidding amount: $'))

    bid[name] = price

    condition = input('is there another bidder? please enter yes or no')
    if condition == 'no':
        bidding_finish = True
        heighst_bid(bid)

