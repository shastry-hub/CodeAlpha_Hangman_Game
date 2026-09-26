import random

# List of unique mythology-inspired words
words = [
    "krishna",
    "garuda",
    "hanuman",
    "indra",
    "trishula"
]

print("===================================")
print("       WELCOME TO HANGMAN GAME")
print("===================================")
print("Guess the mythology-inspired word!")
print("You can make up to 6 incorrect guesses.\n")

while True:

    # Select a random word
    word = random.choice(words)

    guessed_letters = []
    wrong_guesses = 0
    max_wrong_guesses = 6

    print("\nA new word has been selected!")
    print("The word has", len(word), "letters.")

    # Main game loop
    while wrong_guesses < max_wrong_guesses:

        # Display the current word
        display_word = ""

        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word)
        print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

        # Check if the complete word has been guessed
        if all(letter in guessed_letters for letter in word):
            print("\n🎉 Congratulations!")
            print("You guessed the word:", word)
            break

        # Ask the player for a letter
        guess = input("Enter a letter: ").lower()

        # Check whether input is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet letter.")
            continue

        # Check for repeated guesses
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        # Add the letter to guessed letters
        guessed_letters.append(guess)

        # Check whether the guess is correct
        if guess in word:
            print("✅ Correct guess!")

        else:
            wrong_guesses += 1
            print("❌ Wrong guess!")
            print("You have", max_wrong_guesses - wrong_guesses,
                  "wrong guesses left.")

    else:
        # Runs when 6 wrong guesses are reached
        print("\n💀 Game Over!")
        print("The correct word was:", word)

    # Ask whether the player wants another round
    while True:
        play_again = input("\nDo you want to play again? (yes/no): ").lower()

        if play_again == "yes" or play_again == "y":
            print("\nStarting a new game...")
            break

        elif play_again == "no" or play_again == "n":
            print("\nThank you for playing Hangman!")
            print("Goodbye!")
            exit()

        else:
            print("Please enter yes or no.")
