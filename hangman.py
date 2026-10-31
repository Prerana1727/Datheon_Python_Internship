
import random

# ASCII Hangman stages
HANGMAN_STAGES = [
    """
     +---+
     |   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]

# Word collection
WORDS = [
    "python",
    "computer",
    "programming",
    "developer",
    "keyboard",
    "internet",
    "software",
    "database",
    "technology",
    "function"
]


def display_game(secret_word, guessed_letters, wrong_guesses):

    print(HANGMAN_STAGES[wrong_guesses])

    print("Word: ", end="")

    for letter in secret_word:
        if letter in guessed_letters:
            print(letter.upper(), end=" ")
        else:
            print("_", end=" ")

    print("\n")

    print("Guessed letters:", " ".join(sorted(guessed_letters)))
    print("Attempts remaining:", 6 - wrong_guesses)


def play_game():

    secret_word = random.choice(WORDS)

    guessed_letters = set()
    wrong_guesses = 0
    max_attempts = 6

    print("\n================================")
    print("       HANGMAN WORD GAME")
    print("================================")

    while wrong_guesses < max_attempts:

        display_game(secret_word, guessed_letters, wrong_guesses)

        guess = input("Guess a letter: ").lower().strip()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.")
            continue

        # Prevent duplicate guesses
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        # Check the guessed letter
        if guess in secret_word:
            print("Correct guess!")
        else:
            wrong_guesses += 1
            print("Wrong guess!")

        # Check victory
        if all(letter in guessed_letters for letter in secret_word):
            print("\n================================")
            print("       YOU WIN!")
            print("================================")
            print("The word was:", secret_word.upper())
            return

    # Game over
    display_game(secret_word, guessed_letters, wrong_guesses)

    print("\n================================")
    print("       GAME OVER!")
    print("================================")
    print("The correct word was:", secret_word.upper())


def main():

    while True:

        play_game()

        choice = input("\nDo you want to play again? (yes/no): ").lower().strip()

        if choice != "yes":
            print("\nThank you for playing Hangman!")
            break


if __name__ == "__main__":
    main()
