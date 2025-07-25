# # If cards total is more than 21 you lose the game
# #if one has 10 and other has queen
# #if both get same score it draws
# #if <17 then they must take another card

# cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]


import random

# ---------------------------
# Function to deal a card
# ---------------------------
def deal_card():
    """Return a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # Ace is 11, face cards = 10
    return random.choice(cards)

# ---------------------------
# Function to calculate score
# ---------------------------
def calculate_score(cards):
    """Take a list of cards and return the score."""
    # If blackjack (Ace + 10) in 2 cards
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Represent blackjack as 0
    # If Ace is in the hand and score > 21, change Ace from 11 to 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# ---------------------------
# Compare player and dealer
# ---------------------------
def compare(user_score, dealer_score):
    if user_score == dealer_score:
        return "Draw 🙃"
    elif dealer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif dealer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > dealer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

# ---------------------------
# Main game function
# ---------------------------
def play_game():
    print("\n===== Blackjack Game =====")

    user_cards = []
    dealer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    # Dealer draws until score >= 17
    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
    print(compare(user_score, dealer_score))

# ---------------------------
# Loop to play again
# ---------------------------
while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
