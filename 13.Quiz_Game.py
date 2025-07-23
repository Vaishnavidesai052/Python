questions = {
    "What is the capital of France?": "Paris",
    "What is 5 + 7?": "12",
    "Who wrote 'Harry Potter'?": "J.K. Rowling"
}

score = 0

for q, a in questions.items():
    ans = input(q + " ")
    if ans.lower() == a.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {a}")

print(f"Your final score is {score}/{len(questions)}")
