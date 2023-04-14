from random import randint
from guess_number_art import logo 


EASY_LEVEL = 10
HARD_LEVEL = 5

 

def check_answer(guess, answer,turns):
    if guess>answer:
        
        print("Too High.")
        return turns -1
    elif guess<answer :
        
        print("Too Low.")
    else:
        
        print(f"You got the answer . The answer is {answer}")
        
def set_difficulty():
    
    level=input("choose a difficulty level . Type 'easy' or 'hard' :")
    if level=="easy":
        
        return EASY_LEVEL
    else:
        
        return HARD_LEVEL        
def game():
    print(logo)
    print("Welcome to the number guessing game!")
    print("I am thinking of a number between 1 and 100.")
    answer = randint(1,100)
   # print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()
    print(f"You have {turns} attempts remaining to guess the number.")

    guess= 0
    while guess!= answer:
        guess = int(input("Make a guess: "))
        check_answer(guess , answer,turns )
        
game()        


        
                  

    



