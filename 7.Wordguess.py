word_list = ["brilliant", "ballon", "camel"]

import random
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
print(placeholder)    

chances = word_length + 2
print(f"You have {chances} chances to guess the word.")


game_over = False
correct_letters = []

while not game_over:
    guess =input("Guess a letter:").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
           display += letter
           correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter   
        else:
            display += "_"

    print(display)   

    if guess not in chosen_word:
        chances -= 1
        print(f"Wrong guess! You have {chances} chances left.") 

    if "_" not in display:
        game_over=True
        print("You win!")

if chances == 0 and "_" in display:
    print("You lose! The correct word was:", chosen_word)        