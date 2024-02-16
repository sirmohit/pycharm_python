import os
def find_winner(bidder_details):
    highest_bid = 0
    winner  = ""
    for bidder in bidder_details:
        bidding_price=bidder_details[bidder]
        if bidding_price>highest_bid:
            highest_bid = bidding_price
            winner = bidder
    print(f'Winner is {winner} with highest price is : {highest_bid}')

bidder_data = {}
end_of_bidding = False
while not end_of_bidding:
    name = input("Enter your name : ")
    bid_prize = int(input("What is your bid? : "))
    bidder_data[name] = bid_prize
    #bidder_data["price"] =bid_prize
    check = input("anybody want to bid (yes/no) :").lower()
    if(check == 'no'):
        end_of_bidding = True
        find_winner(bidder_data)
    elif(check == 'yes'):
        os.system("cls")
