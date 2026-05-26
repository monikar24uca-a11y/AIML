# Simple AI Guessing Game

print("Think of a number between 1 and 100.")
input("Press Enter when ready...")

low = 1
high = 100

while True:
    guess = (low + high) // 2
    print(f"My guess is: {guess}")

    response = input("Is it high, low, or correct? ").lower()

    if response == "correct":
        print("Yay! I guessed your number.")
        break
    elif response == "high":
        high = guess - 1
    elif response == "low":
        low = guess + 1
    else:
        print("Please type: high, low, or correct.")