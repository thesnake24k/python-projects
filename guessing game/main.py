import random
print("welcome to the guessing game")
if input("choose deficulty easy ot hard ")=="easy":
    attempt=5
else:
    attempt=10
resu=random.randint(1,101)
print(f"You have {attempt}")
#print(resu)
def main():
    global attempt
    test=False
    finish=False
    while test==False and finish==False:
        num=int(input("guess a number "))
        if num == resu:
            test=True
        elif num>resu:
            print(f"too hightd {attempt-1} left")
        else:
            print (f"too low {attempt-1} left")
        attempt-=1
        if attempt==0:
            finish=True
#            break

    if test==True:
        print ("you guessed the right number")
    else:
        print("you lost")


main()


"""
from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
 
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}") 

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()
"""