from random import randint
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5



#Function to check users' guess against actual number
def check_answer(user_guess,actual_answer,turns):
    """Check answer against guess,returns the number of turns remaining"""
    if user_guess >actual_answer:
        print("Too High.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too Low.")
        return turns - 1
    else:
        print(f"Congratulations!! You got the correct answer {actual_answer}")  

#Function to set difficulty   
def set_difficulty():
    level=input("Choose a difficulty.Type 'easy' or 'hard':")
    if level =="easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS    
    
#Repeat the gussing functionality if they got it wrong.

def game():
    #Choosing a random number between 1 and 100.
    answer = randint(a=1,b=100)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    # print(f"Psst,the correct answer is {answer}")

    turns = set_difficulty()
    

    guess=0
    while guess!=answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        #Let the user guess a number
        guess=int(input("Make a guess:"))
        turns=check_answer(guess,answer,turns)
        if turns == 0:
            print("You have run out of guesses,you lose.")
            return
        elif guess!=answer:
            print("Guess again.")

#Track the number of turns and reduce by 1 if they got it wrong

game()