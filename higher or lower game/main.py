from art import logo
from art import vs
from game_data import data
import random
import os
def compare (guess, next_guess):
    """ function to comare who has more followers"""
    if guess>= next_guess:
        return True
    else:
        return False 

def main(choice_first,choice_second,score):
    os.system('cls')
    print(logo)
    print(f"Compare A: {choice_first['name']}, {choice_first['description']}, from {choice_first['country']}")
#    print(choice_first["follower_count"])
    print(vs)
    print(f"Against B: {choice_second['name']}, {choice_second['description']}, from {choice_second['country']}")
#    print(choice_second["follower_count"])
    guess=input("who has more followers ").lower()
    print(guess)

    if guess=="a":
        if compare(choice_first["follower_count"],choice_second["follower_count"]):
            score+=1
            print(f"You're right! current score: {score}")
            choice_second=random.choice(data)
            main(choice_first,choice_second,score)
            

        else:
            os.system('cls')
            print(logo)
            print(f"Wrong guess, your socre {score}")
    elif guess=="b":
        if compare(choice_second["follower_count"],choice_first["follower_count"]):
            score+=1
            print(f"You're right! current score: {score}")
            choice_first=choice_second
            choice_second=random.choice(data)
            main(choice_first,choice_second,score)            
        else:
            os.system('cls')
            print(logo)
            print(f"Wrong guess, your socre {score}")




score=0
choice_first= random.choice(data)
choice_second=random.choice(data)
main(choice_first,choice_second,score)