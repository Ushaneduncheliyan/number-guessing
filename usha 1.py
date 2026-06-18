import random

while True:
    number_to_guess = random.randint(1, 100)

    while True:
        user_guess = int(input("Guess a number between 1 and 100: "))

        if user_guess == number_to_guess:
            print("Congratulations! You guessed it right!")
            break
        elif user_guess < number_to_guess:
            print("Too low, try again.")
        else:
            print("Too high, try again.")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
import random

number_to_guess = random.randint(1, 100)
attempts = 7

while attempts > 0:
    user_guess = int(input(f"You have {attempts} guesses left. Guess a number: "))

    if user_guess == number_to_guess:
        print("Congratulations! You guessed it right!")
        break
    elif user_guess < number_to_guess:
        print("Too low.")
    else:
        print("Too high.")

    attempts -= 1

if attempts == 0:
    print(f"Sorry, you ran out of attempts. The number was {number_to_guess}.")
difficulty = input("Choose difficulty (easy/medium/hard): ").lower()

if difficulty == "easy":
    number_to_guess = random.randint(1, 50)
    attempts = 10
elif difficulty == "medium":
    number_to_guess = random.randint(1, 100)
    attempts = 7
else:
    number_to_guess = random.randint(1, 150)
    attempts = 5
