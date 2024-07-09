""""############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
import random
from replit import clear
from art import logo

def deal_card():
 Returns a random card from the deck.
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(cards):
  Take a list of cards and return the score calculated from the cards

  #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
  #Bug fix. If you and the computer are both over, you lose.
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"


  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():

  print(logo)

  #Hint 5: Deal the user and computer 2 cards each using deal_card()
  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

  while not is_game_over:
    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
"""




import random
import os
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def check_w(pl,cp):
    if pl > cp:
        return "You win"
    elif pl<cp:
        return "you lose"
    else:
        return "it's a draw"
def add_card(list,cards):
    list.append(random.choice(cards))

def replace_ace(list):
    test=True
    i=0
    while test==True and i<= len(list)-1:
        if list[i]==11:
            list[i]=1
            test=False
        i+=1

def score(list):
    f=0
    for s in list:
        f+=s
    return f



def print_cards(pl_cp):
    print(f"Your cards are {pl_cp['player']} = {score(pl_cp['player'])}")
    print(f"dealer first card = {pl_cp['computer'][0]} ")


def final_score(pl_cp):
    print(f"Your final hand : {pl_cp['player']} = {score(pl_cp['player'])}")
    print(f"Computer's final hand {pl_cp['computer']} = {score(pl_cp['computer'])}")

def loser(n):
    if n > 21:
        print("you went over 21, you lose   LOSER LOSER LOSER LOSER !!!!!!😤😤😤😤")
    else:
        print("you lost, Dealer scored higher than you   LOSER LOSER LOSER LOSER !!!!!!😭😭😭😭")


def winner():
    print("you won !!!!! WINER WINER WINER WINER!!!!!!!😎😎😎😎😎😎")


def replace_ace(list):
    test=True
    i=0
    while test==True and i<= len(list)-1:
        if list[i]==11:
            list[i]=1
            test=False
        i+=1
            
def ace_condition(pl_list,pl_cp):
    if score(pl_list)>21 and 11 in pl_list:
        replace_ace(pl_list)
        print_cards(pl_cp)
#        print(f"testt =====Condition===== {pl_cp}")
#       ace_condition(pl_list,pl_cp)
        

def pl_choice_loop(pl_cp,cards):
    choice=input("would you like to add a card? Type 'y' for yes and 'n' for no: ")
    if choice=="y":
        add_card(pl_cp['player'],cards)
        print_cards(pl_cp)
        ace_condition(pl_cp["player"],pl_cp)
        
#        if score(pl_cp['player'])>21 and 11 in pl_cp['player']:
#            replace_ace(pl_cp["player"])
#            print_cards(pl_cp)
#            print(f"testt ========== {pl_cp}")
#            pl_choice_loop(pl_cp,cards)
        
        
        if score(pl_cp['player'])>21:
            loser(score(pl_cp['player']))
            final_score(pl_cp)
            main()
        else:
            pl_choice_loop(pl_cp,cards)
#    else:
#        final_score(pl_cp)   


def cp_choice_loop(pl_cp,cards):
    ace_condition(pl_cp["computer"],pl_cp)

#    if score(pl_cp['computer'])>21 and 11 in pl_cp['computer']:
#        print(f"testt ======cpchoice==== {pl_cp}")
#        replace_ace(pl_cp["computer"])
#        cp_choice_loop(pl_cp,cards)


    if score(pl_cp['computer'])>21:
        winner()
        final_score(pl_cp)
        main()
    elif score(pl_cp['computer'])>score(pl_cp["player"]):
        loser(score(pl_cp["player"]))
        final_score(pl_cp)
        main()
        
    elif score(pl_cp['computer'])<17:
        add_card(pl_cp["computer"],cards)
        cp_choice_loop(pl_cp,cards)
    elif score(pl_cp['player'])==score(pl_cp['computer']):
            print("You can keep your money, but you win nothing it is a draw !!!!")
            final_score(pl_cp)
            main()
    elif score(pl_cp['computer'])>17 and score(pl_cp['computer']) <score(pl_cp['player']):
        winner()
        final_score(pl_cp)
        main()
    else:
        cp_choice_loop(pl_cp,cards)
def main():
    
    
    if input("Do you want to play a game of Black Jack? Type 'y' for yes and 'n' for no: ") == "y":
        start=True
    else:
        start=False
    os.system('cls')
    print(logo)
    pl_cp={
        "player":[],
        "computer":[]
    }
    if start:
        add_card(pl_cp['player'],cards)
        add_card(pl_cp['player'],cards)
        add_card(pl_cp['computer'],cards)
        add_card(pl_cp['computer'],cards)
        ace_condition(pl_cp["player"],pl_cp)
        print_cards(pl_cp)
        pl_choice_loop(pl_cp,cards)
        cp_choice_loop(pl_cp,cards)
        


main()