from random import randint

def choose_level():
    print("Choose difficulty:")
    print("1 - Easy   (1 to 50)")
    print("2 - Medium (1 to 100)")
    print("3 - Hard   (1 to 500)")

    while True:
        choice = input("Enter 1, 2 or 3: ").strip()
        if choice == "1":
            return 1, 50
        elif choice == "2":
            return 1, 100
        elif choice == "3":
            return 1, 500
        else:
            print("Invalid choice, please try again.")

def play_game(low, high):
    target = randint(low, high)
    attempts = 0

    print(f"\nI'm thinking of a number between {low} and {high}.")

    while True:
        guess_input = input("Your guess: ")

        if not guess_input.isdigit():
            print("Please enter a valid number!")
            continue

        guess = int(guess_input)
        attempts += 1

        if guess < low or guess > high:
            print(f"Remember, the number is between {low} and {high}.")
        elif guess < target:
            print("Too low! Try a higher number.")
        elif guess > target:
            print("Too high! Try a lower number.")
        else:
            print(f"Correct! You guessed it in {attempts} tries.")
            return attempts

def main():
    print("=== Number Guessing Game ===")
    best_score = None

    while True:
        low, high = choose_level()
        attempts = play_game(low, high)

        if best_score is None or attempts < best_score:
            best_score = attempts
            print(f"🎉 New best score: {best_score} attempts!")

        again = input("\nDo you want to play again? (y/n): ").strip().lower()
        if again != "y":
            print("\nThanks for playing!")
            if best_score is not None:
                print(f"Your best score was {best_score} attempts.")
            break

if __name__ == "__main__":
    main()