# Problem 3: Number Guessing Game
def number_guessing_game():
    secret_number = 57
    attempts = 0

    while attempts < 7:
        guess = int(input("Enter your guess: "))

        if guess < 0:
            print("Negative numbers ignored.")
            continue

        attempts += 1

        if guess == secret_number:
            print("Correct! You guessed the number.")
            break
        elif guess < secret_number:
            print("Too Low!")
        else:
            print("Too High!")

    print("Attempts Used:", attempts)

number_guessing_game()
