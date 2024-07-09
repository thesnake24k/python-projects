#from replit import clear
#HINT: You can call clear() to clear the output in the console.
import os
from art import logo


"""******************SCHOOL VERSION***********************
bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()
  
"""



print(logo)
bid_list={}
more="yes"
while more=="yes":
    name_b=input("what is your name \n")
    bid_b=int(input("how much you want to bid \n$"))
    bid_list[name_b]=bid_b
    test=False
    while test==False:
        more =input("is there anymore bidder yes/no \n ")
        if more =="yes" or more=="no":
            test=True
        else:
            print("please chose yes or no")
    os.system('cls')
win_name=""
max_bid=0
for name in bid_list:
    if bid_list[name]> max_bid:
        win_name=name
        max_bid=bid_list[name]
print(bid_list)
print(f"the winner is {win_name} with a bid of ${max_bid}")